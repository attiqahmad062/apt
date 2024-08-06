
import re
import scrapy
from itemadapter import ItemAdapter
from SPARQLWrapper import SPARQLWrapper, JSON, POST, URLENCODED

GRAPHDB_SETTINGS = {
    'endpoint': 'http://localhost:7200/repositories/etiapt/statements',
    'prefix': 'https://attack.mitre.org/'
}

class GroupTable(scrapy.Item):
    MittreName = scrapy.Field()
    GroupName = scrapy.Field() 
    Summary = scrapy.Field()
    AssociatedGroups = scrapy.Field()
    Url = scrapy.Field()

class TechniquesTable(scrapy.Item):
    ID = scrapy.Field()
    Use = scrapy.Field()
    Domain = scrapy.Field()
    References = scrapy.Field()
    SubId = scrapy.Field()
    GroupId = scrapy.Field()
    Name = scrapy.Field()
class SoftwareTable(scrapy.Item):
    ID = scrapy.Field()
    Name = scrapy.Field()
    References = scrapy.Field()
    Techniques = scrapy.Field()
class CampaignsTable(scrapy.Item):
    ID = scrapy.Field()
    Name = scrapy.Field()
    FirstSeen = scrapy.Field()
    LastSeen = scrapy.Field()
    References = scrapy.Field()
    Techniques = scrapy.Field()

class SubTechniques(scrapy.Item):
    ID = scrapy.Field()
    Name = scrapy.Field()

class ProcedureExamples(scrapy.Item):
    ID = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()

class Mitigations(scrapy.Item):
    ID = scrapy.Field()
    Mitigation = scrapy.Field()
    Description = scrapy.Field()

class Detections(scrapy.Item):
    ID = scrapy.Field()
    DataSource = scrapy.Field()
    DataComponent = scrapy.Field()
    Detects = scrapy.Field()
class MySQLPipeline:
    def open_spider(self, spider):
        self.sparql = SPARQLWrapper(GRAPHDB_SETTINGS['endpoint'])
        print("Connection to GraphDB established")
    def close_spider(self, spider):
        # GraphDB connection does not need explicit closing
        pass
    def process_item(self, item, spider):
        try:
            if isinstance(item, GroupTable):
                query = self.create_group_table_query(item)
            elif isinstance(item, TechniquesTable):
                query = self.create_techniques_table_query(item)
                print(query)
            elif isinstance(item, SoftwareTable):
                query = self.create_software_table_query(item)
            elif isinstance(item, CampaignsTable):
                query = self.create_compains_table_query(item)
            elif isinstance(item, SubTechniques):
                query = self.create_sub_techniques_query(item)
            elif isinstance(item, ProcedureExamples):
                query = self.create_procedure_examples_query(item)
            elif isinstance(item, Mitigations):
                query = self.create_mitigations_query(item)
            else:
                return item   
            self.execute_sparql(query)
        except Exception as e:
            print(f"An error occurred while processing item: {e}")
        return item
    def execute_sparql(self, query):
        try:
            self.sparql.setQuery(query)
            self.sparql.setMethod(POST)
            self.sparql.setRequestMethod(URLENCODED)
            self.sparql.query()
        except Exception as e:
            print(f"An error occurred while executing SPARQL query: {e}")
    def create_group_table_query(self, item):
        try:
            group_name = item.get('GroupName', '').replace(' ', '_')
            mitre_name = item.get('MittreName', '').replace('"', '\\"')
            summary = item.get('Summary', '').replace('"', '\\"')
            associated_groups = item.get('AssociatedGroups', '').replace('"', '\\"')
            url = item.get('Url', '').replace('"', '\\"')

            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{group_name} a ex:groups ;
                    ex:mitreName "{mitre_name}" ;
                    ex:summary "{summary}" ;
                    ex:associatedGroups "{associated_groups}" ;
                    ex:url "{url}" .
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating GroupTable query: {e}")
            return ""




    def create_techniques_table_query(self, item):
        def escape_string(value):
            if value is None:
                return ""
            return value.replace("\\", "\\\\").replace("\"", "\\\"")
        try:
            technique_id = item.get('ID')
            refs = self.create_references(item.get('References'), technique_id, 'technique')
#   ID = scrapy.Field()
    # Use = scrapy.Field()
    # Domain = scrapy.Field()
    # References = scrapy.Field() 
    # SubId = scrapy.Field()
    # GroupId = scrapy.Field()
            technique_id = escape_string(item.get('ID'))
            technique_name = escape_string(item.get('Name'))
            description = escape_string(item.get('Use'))
            # ex:description "{description}" ;   
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
             ex:{technique_id} a ex:techniques ;
            ex:techniqueName "{technique_name}" ;
            ex:description "{description}" .
            {refs} 
            }} 
            """
        except Exception as e:
            print(f"An error occurred while creating TechniquesTable query: {e}")
            return ""

    def create_software_table_query(self, item):
        try:
            software_id = item.get('ID')
            refs = self.create_references(item.get('References'), software_id, 'software')
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{software_id} a ex:softwares ;
                    ex:name "{item.get('Name')}" ;
                    ex:techniques "{item.get('Techniques')}" .
                  ex:referenceUrl "{refs} "
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating SoftwareTable query: {e}")
            return ""

    def create_compains_table_query(self, item):
        try:
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{item.get('ID')} a ex:campaigns ;
                    ex:name "{item.get('Name')}" ;
                    ex:references "{item.get('References')}" ;
                    ex:techniques "{item.get('Techniques')}" .
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating CompainsTable query: {e}")
            return ""

    def create_sub_techniques_query(self, item):
        try:
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{item.get('ID')} a ex:subtechniques ;
                    ex:name "{item.get('Name')}" .
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating SubTechniques query: {e}")
            return ""

    def create_procedure_examples_query(self, item):
        try:
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{item.get('ID')} a ex:procedures ;
                    ex:name "{item.get('Name')}" ;
                    ex:description "{item.get('Description')}" .
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating ProcedureExamples query: {e}")
            return ""

    def create_mitigations_query(self, item):
        try:
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{item.get('ID')} a ex:mitigations ;
                    ex:mitigation "{item.get('Mitigation')}" ;
                    ex:description "{item.get('Description')}" .
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating Mitigations query: {e}")
            return ""

    def create_references(self, references, id, ref_type):
        try:
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', references)
            triples = ""
            for link in links:
                triples += f'ex:{id} ex:hasReference "{link}" .\n'
            return triples
        except Exception as e:
            print(f"An error occurred while creating references: {e}")
            return ""
