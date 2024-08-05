# # #group_name varchar(255) 
# # # mitre_name varchar(255) 
# # # summary longtext 
# # # created_date datetime 
# # # modified_date
# import re
# import scrapy
# from rdflib import Graph, URIRef, Literal, Namespace
# from rdflib.namespace import RDF, RDFS, XSD
# from SPARQLWrapper import SPARQLWrapper, POST

# # Define the RDF namespaces
# ETIAPT = Namespace("http://example.org/etiapt#")

# # Define the item classes
# class GroupTable(scrapy.Item):
#     MittreName = scrapy.Field()
#     GroupName = scrapy.Field()
#     Summary = scrapy.Field()
#     AssociatedGroups = scrapy.Field()
#     Url = scrapy.Field()

# class TechniquesTable(scrapy.Item):
#     ID = scrapy.Field()
#     Use = scrapy.Field()
#     Domain = scrapy.Field()
#     References = scrapy.Field()
#     SubId = scrapy.Field()
#     GroupId = scrapy.Field()

# class SoftwareTable(scrapy.Item):
#     ID = scrapy.Field()
#     Name = scrapy.Field()
#     References = scrapy.Field()
#     Techniques = scrapy.Field()

# class CampaignsTable(scrapy.Item):
#     ID = scrapy.Field()
#     Name = scrapy.Field()
#     FirstSeen = scrapy.Field()
#     LastSeen = scrapy.Field()
#     References = scrapy.Field()
#     Techniques = scrapy.Field()

# class SubTechniques(scrapy.Item):
#     ID = scrapy.Field()
#     Name = scrapy.Field()

# class ProcedureExamples(scrapy.Item):
#     Id = scrapy.Field()
#     Name = scrapy.Field()
#     Description = scrapy.Field()

# class Mitigations(scrapy.Item):
#     ID = scrapy.Field()
#     Mitigation = scrapy.Field()
#     Description = scrapy.Field()

# class Detections(scrapy.Item):
#     ID = scrapy.Field()
#     DataSource = scrapy.Field()
#     DataComponent = scrapy.Field()
#     Detects = scrapy.Field()

# class MySQLPipeline:
#     def open_spider(self, spider):
#         self.graph = Graph()
#         self.sparql_endpoint = "http://localhost:7200/repositories/etiapt/statements"  # Adjust the endpoint URL
#         self.sparql = SPARQLWrapper(self.sparql_endpoint)
#     def close_spider(self, spider):
#         self.upload_graph_to_repo()
#     def upload_graph_to_repo(self):
#         self.sparql.setMethod(POST)
#         self.sparql.setQuery(f"""
#         INSERT DATA {{
#             {self.graph.serialize(format='nt')}
#         }}
#         """)
#         self.sparql.query()

#     def process_item(self, item, spider):
#         if isinstance(item, GroupTable):
#             group = URIRef(ETIAPT[item.get('groupId')])
#             self.graph.add((group, RDF.type, ETIAPT.Group))
#             self.graph.add((group, RDFS.label, Literal(item.get('groupName'), datatype=XSD.string)))
#             self.graph.add((group, ETIAPT.summary, Literal(item.get('Summary'), datatype=XSD.string)))
#             self.graph.add((group, ETIAPT.associatedGroups, Literal(item.get('AssociatedGroups'), datatype=XSD.string)))
#             self.graph.add((group, ETIAPT.url, Literal(item.get('Url'), datatype=XSD.anyURI)))
#         elif isinstance(item, TechniquesTable):
#             technique = URIRef(ETIAPT[item.get('ID')])
#             self.graph.add((technique, RDF.type, ETIAPT.Technique))
#             self.graph.add((technique, RDFS.label, Literal(item.get('Use'), datatype=XSD.string)))
#             self.graph.add((technique, ETIAPT.domain, Literal(item.get('Domain'), datatype=XSD.string)))
#             self.graph.add((technique, ETIAPT.subId, Literal(item.get('SubId'), datatype=XSD.string)))
#             self.graph.add((technique, ETIAPT.groupId, Literal(item.get('GroupId'), datatype=XSD.string)))

#             input_string = item.get('References')
#             links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
#             for link in links:
#                 self.graph.add((technique, ETIAPT.reference, Literal(link, datatype=XSD.anyURI)))
#         elif isinstance(item, SoftwareTable):
#             software = URIRef(ETIAPT[item.get('ID')])
#             self.graph.add((software, RDF.type, ETIAPT.Software))
#             self.graph.add((software, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))

#             input_string = item.get('References')
#             links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
#             for link in links:
#                 self.graph.add((software, ETIAPT.reference, Literal(link, datatype=XSD.anyURI)))
            
#             self.graph.add((software, ETIAPT.techniques, Literal(item.get('Techniques'), datatype=XSD.string)))
#         elif isinstance(item, CampaignsTable):
#             campaign = URIRef(ETIAPT[item.get('ID')])
#             self.graph.add((campaign, RDF.type, ETIAPT.Campaign))
#             self.graph.add((campaign, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))
#             self.graph.add((campaign, ETIAPT.firstSeen, Literal(item.get('FirstSeen'), datatype=XSD.date)))
#             self.graph.add((campaign, ETIAPT.lastSeen, Literal(item.get('LastSeen'), datatype=XSD.date)))
            
#             input_string = item.get('References')
#             links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
#             for link in links:
#                 self.graph.add((campaign, ETIAPT.reference, Literal(link, datatype=XSD.anyURI)))
            
#             self.graph.add((campaign, ETIAPT.techniques, Literal(item.get('Techniques'), datatype=XSD.string)))
#         elif isinstance(item, SubTechniques):
#             sub_technique = URIRef(ETIAPT[item.get('ID')])
#             self.graph.add((sub_technique, RDF.type, ETIAPT.SubTechnique))
#             self.graph.add((sub_technique, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))
#         elif isinstance(item, ProcedureExamples):
#             procedure = URIRef(ETIAPT[item.get('Id')])
#             self.graph.add((procedure, RDF.type, ETIAPT.Procedure))
#             self.graph.add((procedure, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))
#             self.graph.add((procedure, ETIAPT.description, Literal(item.get('Description'), datatype=XSD.string)))
#         elif isinstance(item, Mitigations):
#             mitigation = URIRef(ETIAPT[item.get('ID')])
#             self.graph.add((mitigation, RDF.type, ETIAPT.Mitigation))
#             self.graph.add((mitigation, RDFS.label, Literal(item.get('Mitigation'), datatype=XSD.string)))
#             self.graph.add((mitigation, ETIAPT.description, Literal(item.get('Description'), datatype=XSD.string)))
#         elif isinstance(item, Detections):
#             detection = URIRef(ETIAPT[item.get('ID')])
#             self.graph.add((detection, RDF.type, ETIAPT.Detection))
#             self.graph.add((detection, ETIAPT.dataSource, Literal(item.get('DataSource'), datatype=XSD.string)))
#             self.graph.add((detection, ETIAPT.dataComponent, Literal(item.get('DataComponent'), datatype=XSD.string)))
#             self.graph.add((detection, ETIAPT.detects, Literal(item.get('Detects'), datatype=XSD.string)))

#         return item

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
            return f"""
            PREFIX ex: <{GRAPHDB_SETTINGS['prefix']}>
            INSERT DATA {{
                ex:{item.get('GroupName')} a ex:groups ;
                    ex:mitreName "{item.get('MittreName')}" ;
                    ex:summary "{item.get('Summary')}" ;
                    ex:associatedGroups "{item.get('AssociatedGroups')}" ;
                    ex:url "{item.get('Url')}" .
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
                {refs} 
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
