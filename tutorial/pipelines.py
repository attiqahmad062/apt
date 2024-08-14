
import re
import scrapy
from itemadapter import ItemAdapter
from datetime import datetime
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
    GroupId = scrapy.Field()
    Name = scrapy.Field()
    References = scrapy.Field()
    Techniques = scrapy.Field()
class CampaignsTable(scrapy.Item):
    ID = scrapy.Field()
    Name = scrapy.Field()
    FirstSeen = scrapy.Field()
    GroupId = scrapy.Field() 
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
            elif isinstance(item, Detections):
                query = self.create_detections_query(item)
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
                mitre_name = item.get('MittreName', '').replace('"', '\\"')
                group_name = item.get('GroupName', '').replace(' ', '_')
                associated_groups = item.get('AssociatedGroups', '').replace('"', '\\"')
                summary = item.get('Summary', '').replace('"', '\\"')
               
                # url = item.get('Url', '').replace('"', '\\"')
 # ex:associatedGroups "{associated_groups}" ;
                        # ex:url "{url}" .
                return f"""
                PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
                INSERT DATA {{
                        ex:{mitre_name} a ex:groups ;
                        ex:groupId "{mitre_name}" ;
                        ex:groupName "{group_name}" ;
                        ex:description "{summary}" ;
                        ex:associatedGroups  "{associated_groups}" .
                }}
                """
            except Exception as e:
                print(f"An error occurred while creating GroupTable query: {e}")
                return ""
            
    def create_techniques_table_query(self, item):
     def escape_string(value):
            if value is None:
                return ""
            return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")

     try:
        technique_id = item.get('ID')
        if not technique_id:
            raise ValueError("Technique ID is missing or empty")

        refs = self.create_references(item.get('References'), technique_id, 'technique')

        technique_id = escape_string(technique_id)
        technique_name = escape_string(item.get('Name'))
        use = escape_string(item.get('Use'))
        domain = escape_string(item.get('Domain'))
        sub_id = escape_string(item.get('SubId'))
        group_id = escape_string(item.get('GroupId'))
        if not technique_id or not technique_name:
            raise ValueError("Essential fields are missing")
        if sub_id:
            # If subId exists, delete any existing data with the same technique_id and sub_id
            delete_existing = f"""
            DELETE WHERE {{
                ex:{technique_id} ex:subId "{sub_id}" .
            }};
            """
        else:
            # If subId does not exist, delete any existing data with the same technique_id and no subId
            delete_existing = f"""
            DELETE WHERE {{
                ex:{technique_id} a ex:techniques .
                FILTER(NOT EXISTS {{ ex:{technique_id} ex:subId ?subId }})
            }};
            """
        insert_new = f"""
        INSERT DATA {{
            ex:{technique_id} a ex:techniques ;
            ex:domain "{domain}" ;
            ex:subId "{sub_id}" ;
            ex:techniqueName "{technique_name}" ;
            ex:techniqueId "{technique_id}" ;
            ex:group_uses_techniques "{group_id}";
            ex:use "{use}" .
            {refs}     
        }} 
        """
        return f"""
        PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
        {delete_existing}
        {insert_new}
        """
     except Exception as e:
        print(f"An error occurred while creating TechniquesTable query: {e}")
        return "" 
    # def create_techniques_table_query(self, item):
    #     def escape_string(value):
    #         if value is None:
    #             return ""
    #         return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")

    #     try:
    #         technique_id = item.get('ID')
    #         if not technique_id:
    #             raise ValueError("Technique ID is missing or empty")

    #         refs = self.create_references(item.get('References'), technique_id, 'technique')

    #         technique_id = escape_string(technique_id)
    #         technique_name = escape_string(item.get('Name'))
    #         use = escape_string(item.get('Use'))
    #         domain = escape_string(item.get('Domain'))
    #         sub_id = escape_string(item.get('SubId'))
    #         group_id = escape_string(item.get('GroupId'))
        
    #         if not technique_id or not technique_name:
    #             raise ValueError("Essential fields are missing")

    #         return f"""
    #         PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
    #         INSERT DATA {{
    #             ex:{technique_id} a ex:techniques ;
    #             ex:domain "{domain}" ;
    #             ex:subId "{sub_id}" ;
    #             ex:techniqueName "{technique_name}" ;
    #             ex:techniqueId "{technique_id}" ;
    #             ex:group_uses_techniques "{group_id}";
    #             ex:use "{use}" .
    #             {refs}     
    #         }} 
    #         """
    #     except Exception as e:
    #         print(f"An error occurred while creating TechniquesTable query: {e}")
    #         return ""

    def create_software_table_query(self, item):
        try:
            #  ex:techniques "{item.get('Techniques')}" .
            software_id = item.get('ID')
            refs = self.create_references(item.get('References'), software_id, 'software')
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{software_id} a ex:softwares ;
                    ex:softwareName "{item.get('Name')}" ;
                    ex:softwareTechniques "{item.get('Techniques')}" ;
                    ex:group_uses_software "{item.get('GroupId')}";
                    ex:softwareId "{software_id}" .
                {refs}
            }}  
            """
        except Exception as e:
            print(f"An error occurred while creating SoftwareTable query: {e}")
            return ""
    #       ID = scrapy.Field()
    # Name = scrapy.Field()
    # FirstSeen = scrapy.Field()
    # LastSeen = scrapy.Field()
    # References = scrapy.Field()
    # Techniques = scrapy.Field()
    

    def create_compains_table_query(self, item):
        def escape_string(value):
            if value is None:
                return ""
            return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")

        def format_date(date_string):
            try:
                # Attempt to parse the date string (assuming the format is like 'June 2022')
                parsed_date = datetime.strptime(date_string, "%B %Y")
                # Return the date in xsd:date format (YYYY-MM-DD)
                return parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                # If parsing fails, return the original string, but this might still cause issues
                return date_string

        try:
            campaign_id = escape_string(item.get('ID'))
            first_seen = format_date(escape_string(item.get('FirstSeen')))
            last_seen = format_date(escape_string(item.get('LastSeen')))
            techniques = item.get('Techniques')
            
            refs = self.create_references(item.get('References'), campaign_id, 'campaign')

            techniques_triples = ""
            if techniques:
                techniques_triples = "\n".join(
                    [f'ex:{campaign_id} ex:campaignsTechniques "{escape_string(technique)}" .' for technique in techniques]
                )

            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            INSERT DATA {{
                    ex:{campaign_id} a ex:campaigns ;
                    ex:campaignName "{escape_string(item.get('Name'))}" ;
                    ex:campaignId "{campaign_id}" ;
                    ex:group_ispartof_campaigns "{escape_string(item.get('GroupId'))}" ;
                    ex:campaignsFirstseen "{first_seen}"^^xsd:date ;
                    ex:campaignsLastseen "{last_seen}"^^xsd:date .
                    {techniques_triples}
                    {refs}
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating CompainsTable query: {e}")
            return ""

    # def create_compains_table_query(self, item):
    #     def escape_string(value):
    #         if value is None:
    #             return ""
    #         return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")
    #     try:
    #         campaign_id=escape_string(item.get('ID'))
    #         first_seen=escape_string(item.get('FirstSeen')) 
    #         last_seen=escape_string(item.get('LastSeen')) 
    #         # techniques=escape_string(item.get('Techniques')) 
    #         refs = self.create_references(item.get('References'), campaign_id, 'campaign')
    #         return f"""
    #         PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
    #         INSERT DATA {{
    #                 ex:{campaign_id} a ex:campaigns ;
    #                 ex:campaignName "{item.get('Name')}" ;
    #                 ex:campaignId "{item.get('ID')}" ;
    #                 ex:group_ispartof_campaigns "{item.get('GroupId')}";
    #                 ex:campaignsTechniques "{item.get('Techniques')}" .
    #                 ex:campaignsFirstseen "{first_seen}" .
    #                 ex:campaignsLastseen "{last_seen}" .
    #                 {refs}
    #         }}
    #         """
    #     except Exception as e:
    #         print(f"An error occurred while creating CompainsTable query: {e}")
    #         return ""

    # def create_sub_techniques_query(self, item):
    #     try:
    #         return f"""
    #         PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
    #         INSERT DATA {{
    #             ex:{item.get('ID')} a ex:subtechniques ;
    #                 ex:name "{item.get('Name')}" .
    #         }}
    #         """
    #     except Exception as e:
    #         print(f"An error occurred while creating SubTechniques query: {e}")
    #         return ""
    def create_procedure_examples_query(self, item):
     def escape_string(value):
        if value is None:
            return ""
        return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")

     try:
        procedure_id = escape_string(item.get('ID'))
        name = escape_string(item.get('Name'))
        description = escape_string(item.get('Description'))
        refs = self.create_references(item.get('References'), procedure_id, 'procedure')
        return f"""
        PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
        INSERT DATA {{
            ex:{procedure_id} a ex:procedures ;
                ex:procedureName  "{name}" ;
                ex:description "{description}" .
            {refs}
        }}
        """
     except Exception as e:
        print(f"An error occurred while creating ProcedureExamples query: {e}")
        return ""


    def create_mitigations_query(self, item):
        def escape_string(value):
            if value is None:
                return ""
            return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")
        try:
            description = escape_string(item.get('Description'))
            mitigation_id = escape_string(item.get('ID'))
            refs = self.create_references(item.get('References'), mitigation_id, 'mitigation')
           
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{mitigation_id} a ex:mitigations ;
                    ex:mitigationName "{item.get('Mitigation')}" ;
                    ex:description "{description}" .
                    {refs}
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating Mitigations query: {e}")
            return ""
        
    def create_detections_query(self, item):
        def escape_string(value):
            if value is None:
                return ""
            return value.strip().replace("\\", "\\\\").replace("\"", "\\\"")
        try:
            detects = escape_string(item.get('Detects'))
            detection_id = escape_string(item.get('ID'))
            refs = self.create_references(item.get('References'), detection_id, 'detection')
            return f""" 
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{item.get('ID')} a ex:detections ;
                    ex:detectionId "{detection_id}";
                    ex:dataSource "{item.get('DataSource')}" ;
                    ex:detects "{detects}" ;
                    ex:dataComponent "{item.get('DataComponent')}" .
                    {refs} .
            }}
            """
        except Exception as e:
            print(f"An error occurred while creating Mitigations query: {e}")
            return ""

    def create_references(self, references, id, ref_type):
        try:
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', references)
            triples = ""
            for i, link in enumerate(links, start=1):
                triples += f'ex:{id}  a  ex:referenceUrl; ex:url "{link}" .\n'
            return triples
        except Exception as e:
            print(f"An error occurred while creating references: {e}")
            return ""
  