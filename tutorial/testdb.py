# # import mysql.connector

# # # MySQL database settings
# # MYSQL_SETTINGS = {
# #     'host': 'localhost',
# #     'port': 3306,
# #     'database': 'etiapt',
# #     'user': 'root',
# #     'password': '7777',
# # }

# # def main():
# #     try:
# #         # Connect to MySQL database
# #         conn = mysql.connector.connect(**MYSQL_SETTINGS)
# #         if conn.is_connected():
# #             print("Connected to MySQL database")
# #         cursor = conn.cursor() 
# #         cursor.execute("select * from etiapt.sub_id")
# #         rows=cursor.fetchall()
# #         for row in rows:
# #             print(row)
# #         # Perform database operations here...

# #         # Close connection
# #         # conn.close()
# #         print("Connection closed")
# #     except mysql.connector.Error as error:
# #         print("Error connecting to MySQL database:", error)

# # if __name__ == "__main__":
# #     main()

# from elasticsearch import Elasticsearch

# es = Elasticsearch(['http://localhost:9200'])

# mapping = {
#     "mappings": {
#         "properties": {
#             "join_field": {
#                 "type": "join",
#                 "relations": {
#                     "apt_group": [
#                         "attack_campaign",
#                         "apt_group_attack_campaigns",
#                         "apt_group_countries",
#                         "apt_group_sectors",
#                         "apt_group_techniques",
#                         "software_used"
#                     ],
#                     "attack_campaign": [
#                         "alias",
#                         "attack_campaign_countries",
#                         "attack_campaign_sectors"
#                     ],
#                     "apt_group_techniques": [
#                         "software_used",
#                         "mitigations",
#                         "detections",
#                         "procedure_example",
#                         "references"
#                     ],
#                     "user_preference": [
#                         "region_preference",
#                         "sector_preference"
#                     ]
#                 }
#             },
#             "apt_group": {
#                 "properties": {
#                     "mitre_name": {"type": "keyword"},
#                     "group_name": {"type": "keyword"},
#                     "summary": {"type": "text"},
#                     "associated_groups": {"type": "text"},
#                     "group_url": {"type": "keyword"}
#                 }
#             },
#             "attack_campaign": {
#                 "properties": {
#                     "id": {"type": "keyword"},
#                     "name": {"type": "keyword"},
#                     "first_seen": {"type": "date"},
#                     "last_seen": {"type": "date"},
#                     "references": {"type": "text"},
#                     "techniques": {"type": "text"}
#                 }
#             },
#             "apt_group_techniques": {
#                 "properties": {
#                     "techniques_id": {"type": "keyword"},
#                     "description": {"type": "text"},
#                     "domain_name": {"type": "keyword"},
#                     "sub_id": {"type": "keyword"}
#                 }
#             },
#             "software_used": {
#                 "properties": {
#                     "software_id": {"type": "keyword"},
#                     "name": {"type": "keyword"},
#                     "techniques": {"type": "text"}
#                 }
#             },
#             "mitigations": {
#                 "properties": {
#                     "m_id": {"type": "keyword"},
#                     "mitigation": {"type": "text"},
#                     "description": {"type": "text"}
#                 }
#             },
#             "detections": {
#                 "properties": {
#                     "id": {"type": "keyword"},
#                     "data_source": {"type": "keyword"},
#                     "data_component": {"type": "keyword"},
#                     "detects": {"type": "text"}
#                 }
#             },
#             "procedure_example": {
#                 "properties": {
#                     "procedure_example_id": {"type": "keyword"},
#                     "name": {"type": "keyword"},
#                     "description": {"type": "text"}
#                 }
#             },
#             "references": {
#                 "properties": {
#                     "reference_id": {"type": "keyword"},
#                     "url": {"type": "keyword"}
#                 }
#             }
#         }
#     }
# }

# # Create the index with the mapping
# index_name =  pt"
# try:
#    es.indices.create(index=index_name, body=mapping)
# except :
#  print(f"Index {index_name} failed to create .",)
# # else:
# #     print(f"Index {index_name} already exists.")


# from elasticsearch import Elasticsearch
# import logging
# # Enable logging
# # logging.basicConfig(level=logging.DEBUG)
# es = Elasticsearch(["http://localhost:9200/"], basic_auth=("elastic", "pMLWZ2_-+o6AN9-zsu7-"))
# # pMLWZ2_-+o6AN9-zsu7-
# #  basic_auth=("attiq ahmad afsar", "37101@Aa77")
# # es = Elasticsearch(cloud_id="73b989b904de434d8d06812890b4d853:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ4MDQzNDJmOWZmY2Y0MDQ5OWEyZjBjNzM4NGRlODQxZiQyMDc3Yzc0ZjBlOWI0YjE3YTk1ZGZhMmQzNGVlZjUzMg==", api_key="https://804342f9ffcf40499a2f0c7384de841f.us-central1.gcp.cloud.es.io",
#                 # )
# # print(es.info()) 

# try:
#     res=es.ping()
#     print("Connected to Elasticsearch",res)
# except Exception as e:
#     print(f"Could not connect to Elasticsearch: {e}")
# doc = {
#     "join_field": "apt_group",
#     "group_name": "ZIRCONIUM",
#     "summary": "A threat group operating out of China, active since at least 2017, targeting individuals associated with the 2020 US presidential election and prominent leaders in the international affairs community.",
#     "associated_groups": "APT31, Violet Typhoon",
#     "group_url": "https://attack.mitre.org/groups/G0128"
# }

# # Define the index name
# doc = {
# 	'title': 'The quick brown fox',
# 	'content': 'The quick brown fox jumps over the lazy dog'
# }

# # index the document
# es.index(index='my_index',  id=1, body=doc)
# index_name = "etiapt"
# query = {
# 	'query': {
# 		'match': {
# 			'content': 'quick brown fox'
# 		}
# 	}
# }

# # search for documents
# result = es.search(index='my_index', body=query)
# print(result)
# # Insert the document into the index
# # try:
# #     es.index(index=index_name, body=doc)
# #     print("Document inserted successfully.")
# # except Exception as e:
# #     print(f"Failed to insert document: {e}") 

# test graph db

# from rdflib import Graph, Literal, RDF, URIRef, Namespace
# from rdflib.namespace import XSD, FOAF
# from SPARQLWrapper import SPARQLWrapper, POST, DIGEST, JSON

# # Define your namespace
# EX = Namespace("https://attack.mitre.org/")

# # Initialize the graph
# g = Graph()

# # Bind namespace
# g.bind("ex", EX)

# # Add triples
# g.add((EX['Alice'], RDF.type, FOAF.Person))
# g.add((EX['Alice'], FOAF.name, Literal('Alice', datatype=XSD.string)))

# # Serialize graph to a format that can be sent to GraphDB
# data = g.serialize(format='turtle').decode("utf-8")

# # GraphDB SPARQL endpoint URL
# graphdb_endpoint = "http://DESKTOP-NR4PEU0:7200/repositories/apt"

# # Connect to GraphDB and insert data
# def insert_data(endpoint, data):
#     sparql = SPARQLWrapper(endpoint)
#     sparql.setMethod(POST)
#     sparql.setRequestMethod(DIGEST)  # Use DIGEST for Digest Auth (or BASIC for Basic Auth)
#     sparql.setQuery("""
#         INSERT DATA {
#             %s
#         }
#     """ % data)
#     sparql.setReturnFormat(JSON)
    
#     try:
#         response = sparql.query().convert()
#         print("Data inserted successfully.")
#         print(response)
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Insert data into the repository
# insert_data(graphdb_endpoint, data)

# # Query the data from the repository
# def query_data(endpoint, query):
#     sparql = SPARQLWrapper(endpoint)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
    
#     try:
#         results = sparql.query().convert()
#         for result in results["results"]["bindings"]:
#             print(result)
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # SPARQL query to fetch data
# query = """
#     SELECT ?s ?p ?o
#     WHERE {
#         ?s ?p ?o.
#     }
#     LIMIT 10
# """

# # Query data from the repository
# query_data(graphdb_endpoint, query)


from rdflib import Graph, Literal, RDF, Namespace, URIRef
from rdflib.namespace import XSD
from SPARQLWrapper import SPARQLWrapper, POST, DIGEST, JSON
query = """
PREFIX mitre: <http://example.org/mitre/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

INSERT DATA {
  GRAPH <http://example.org/graph> {
    mitre:T1234 rdf:type mitre:Technique ;
                rdfs:label "Example Technique" ;
                mitre:description "This is an example technique." ;
                 mitre:platform "Windows" .
  }
}
"""
graphdb_endpoint = "http://DESKTOP-NR4PEU0:7200/repositories/apt/statements"
sparql = SPARQLWrapper(graphdb_endpoint)
sparql.setCredentials("admin", "37101@Aa77")  # Add your credentials if required
# sparql.addParameter("add", data)
sparql.setReturnFormat(JSON)
sparql.setMethod(POST)
sparql.addParameter("infer", "true")
# Set the update query
sparql.setQuery(query)
# Execute the query and handle exceptions
try:
    sparql.query()
    print("Data inserted successfully.")
except Exception as e:
    print(f"Error inserting data: {e}")
# Define namespaces
# EX = Namespace("http://www.semanticweb.org/attiqahmad/ontologies/2024/6/untitled-ontology-5/techniques")

# # Initialize the graph
# g = Graph()

# # Bind namespace
# g.bind("ex", EX)

# # Define the resource
# technique = EX["T1087"]

# # Add triples to the graph
# g.add((technique, RDF.type, EX.Technique))
# # g.add((technique, EX.domain, Literal("Enterprise", datatype=XSD.string)))
# g.add((technique, EX.techniqueId, Literal("T1087", datatype=XSD.string)))
# g.add((technique, EX.techniquename, Literal("Account Discovery: Local Account", datatype=XSD.string)))
# # g.add((technique, EX.use, Literal("admin@338 actors used the following commands following exploitation of a machine with LOWBALL malware to enumerate user accounts: net user >> %temp%\\download net user /domain >> %temp%\\download[1]", datatype=XSD.string)))
# # Serialize the graph to Turtle format
# data = g.serialize(format='turtle')

# # GraphDB SPARQL endpoint URL
# graphdb_endpoint = "http://DESKTOP-NR4PEU0:7200/repositories/apt"
# query = """
# PREFIX mitre: <http://example.org/mitre/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# INSERT DATA {
#   GRAPH <http://example.org/graph> {
#     mitre:T1234 rdf:type mitre:Technique ;
#                 rdfs:label "Example Technique" ;
#                 mitre:description "This is an example technique." ;
#                 mitre:platform "Windows" .
#   }
# }
# """
# # Function to insert data into GraphDB
# def insert_data(endpoint, data):
#     sparql = SPARQLWrapper(endpoint)
#     sparql.setMethod(POST)
#     # sparql.setRequestMethod(DIGEST)  # Use DIGEST for Digest Auth (or BASIC for Basic Auth)
#     sparql.setCredentials("admin", "37101@Aa77")  # Add your credentials if required
#     # sparql.addParameter("add", data)
#     sparql.setReturnFormat(JSON)
#     # try:
#     #     response = sparql.query().convert()
#     #     print("Data inserted successfully.")
#     #     print("response is ",response)
#     # except Exception as e:
#     #     print(f"An error occurred: {e}")
#     sparql.setQuery(query)
#     try:
#         sparql.query()
#         print("Data inserted successfully.")
#     except Exception as e:
#         print(f"Error inserting data: {e}")

# # Insert data into the repository
# insert_data(graphdb_endpoint, data)

# # Function to query data from GraphDB
# def query_data(endpoint, query):
#     sparql = SPARQLWrapper(endpoint)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
    
#     try:
#         results = sparql.query().convert()
#         for result in results["results"]["bindings"]:
#             print(result)
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # SPARQL query to fetch data
# query = """
#     PREFIX ex: <http://www.semanticweb.org/attiqahmad/ontologies/2024/6/untitled-ontology-5/>
# SELECT ?techniqueId ?techniqueName
# WHERE {
#   ?techniqueId a ex:Technique .
#   ?techniqueId ex:techniqueName ?techniqueName .
# }
# """

# # Query data from the repository
# query_data("http://DESKTOP-NR4PEU0:7200/repositories/apt", query)
