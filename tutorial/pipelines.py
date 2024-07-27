# #group_name varchar(255) 
# # mitre_name varchar(255) 
# # summary longtext 
# # created_date datetime 
# # modified_date
import re
import scrapy
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD
from SPARQLWrapper import SPARQLWrapper, POST

# Define the RDF namespaces
ETIAPT = Namespace("http://example.org/etiapt#")

# Define the item classes
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
    Id = scrapy.Field()
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
        self.graph = Graph()
        self.sparql_endpoint = "http://localhost:7200/repositories/etiapt"  # Adjust the endpoint URL
        self.sparql = SPARQLWrapper(self.sparql_endpoint)
    def close_spider(self, spider):
        self.upload_graph_to_repo()
    def upload_graph_to_repo(self):
        self.sparql.setMethod(POST)
        self.sparql.setQuery(f"""
        INSERT DATA {{
            {self.graph.serialize(format='nt')}
        }}
        """)
        self.sparql.query()

    def process_item(self, item, spider):
        if isinstance(item, GroupTable):
            group = URIRef(ETIAPT[item.get('MittreName')])
            self.graph.add((group, RDF.type, ETIAPT.Group))
            self.graph.add((group, RDFS.label, Literal(item.get('GroupName'), datatype=XSD.string)))
            self.graph.add((group, ETIAPT.summary, Literal(item.get('Summary'), datatype=XSD.string)))
            self.graph.add((group, ETIAPT.associatedGroups, Literal(item.get('AssociatedGroups'), datatype=XSD.string)))
            self.graph.add((group, ETIAPT.url, Literal(item.get('Url'), datatype=XSD.anyURI)))
        elif isinstance(item, TechniquesTable):
            technique = URIRef(ETIAPT[item.get('ID')])
            self.graph.add((technique, RDF.type, ETIAPT.Technique))
            self.graph.add((technique, RDFS.label, Literal(item.get('Use'), datatype=XSD.string)))
            self.graph.add((technique, ETIAPT.domain, Literal(item.get('Domain'), datatype=XSD.string)))
            self.graph.add((technique, ETIAPT.subId, Literal(item.get('SubId'), datatype=XSD.string)))
            self.graph.add((technique, ETIAPT.groupId, Literal(item.get('GroupId'), datatype=XSD.string)))

            input_string = item.get('References')
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
            for link in links:
                self.graph.add((technique, ETIAPT.reference, Literal(link, datatype=XSD.anyURI)))
        elif isinstance(item, SoftwareTable):
            software = URIRef(ETIAPT[item.get('ID')])
            self.graph.add((software, RDF.type, ETIAPT.Software))
            self.graph.add((software, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))

            input_string = item.get('References')
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
            for link in links:
                self.graph.add((software, ETIAPT.reference, Literal(link, datatype=XSD.anyURI)))
            
            self.graph.add((software, ETIAPT.techniques, Literal(item.get('Techniques'), datatype=XSD.string)))
        elif isinstance(item, CampaignsTable):
            campaign = URIRef(ETIAPT[item.get('ID')])
            self.graph.add((campaign, RDF.type, ETIAPT.Campaign))
            self.graph.add((campaign, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))
            self.graph.add((campaign, ETIAPT.firstSeen, Literal(item.get('FirstSeen'), datatype=XSD.date)))
            self.graph.add((campaign, ETIAPT.lastSeen, Literal(item.get('LastSeen'), datatype=XSD.date)))
            
            input_string = item.get('References')
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
            for link in links:
                self.graph.add((campaign, ETIAPT.reference, Literal(link, datatype=XSD.anyURI)))
            
            self.graph.add((campaign, ETIAPT.techniques, Literal(item.get('Techniques'), datatype=XSD.string)))
        elif isinstance(item, SubTechniques):
            sub_technique = URIRef(ETIAPT[item.get('ID')])
            self.graph.add((sub_technique, RDF.type, ETIAPT.SubTechnique))
            self.graph.add((sub_technique, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))
        elif isinstance(item, ProcedureExamples):
            procedure = URIRef(ETIAPT[item.get('Id')])
            self.graph.add((procedure, RDF.type, ETIAPT.Procedure))
            self.graph.add((procedure, RDFS.label, Literal(item.get('Name'), datatype=XSD.string)))
            self.graph.add((procedure, ETIAPT.description, Literal(item.get('Description'), datatype=XSD.string)))
        elif isinstance(item, Mitigations):
            mitigation = URIRef(ETIAPT[item.get('ID')])
            self.graph.add((mitigation, RDF.type, ETIAPT.Mitigation))
            self.graph.add((mitigation, RDFS.label, Literal(item.get('Mitigation'), datatype=XSD.string)))
            self.graph.add((mitigation, ETIAPT.description, Literal(item.get('Description'), datatype=XSD.string)))
        elif isinstance(item, Detections):
            detection = URIRef(ETIAPT[item.get('ID')])
            self.graph.add((detection, RDF.type, ETIAPT.Detection))
            self.graph.add((detection, ETIAPT.dataSource, Literal(item.get('DataSource'), datatype=XSD.string)))
            self.graph.add((detection, ETIAPT.dataComponent, Literal(item.get('DataComponent'), datatype=XSD.string)))
            self.graph.add((detection, ETIAPT.detects, Literal(item.get('Detects'), datatype=XSD.string)))

        return item
