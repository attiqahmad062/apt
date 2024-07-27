# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import re
# import scrapy
# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import mysql.connector
# import scrapy.itemedewd
# from itemadapter import ItemAdapter
# import mysql.connector

# MYSQL_SETTINGS = {

#     'host': 'localhost',
#     'port': 3306,
#     'database': 'etiapt',
#     'user': 'root',
#     'password': '1234',  # 7777:1234
# }

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

# class CompainsTable(scrapy.Item):
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
#     ID = scrapy.Field()
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
#         self.conn = mysql.connector.connect(**MYSQL_SETTINGS)
#         self.cursor = self.conn.cursor()
#         print("Connection established")

#     def close_spider(self, spider):
#         self.conn.close()
#     def process_item(self, item, spider):
#         if isinstance(item, GroupTable): 
#             try:
#                 sql = "INSERT INTO apt_group (mitre_name, group_name, summary, associated_groups, group_url) VALUES (%s, %s, %s, %s, %s)"
#                 values = (item.get('MittreName'), item.get('GroupName'), item.get('Summary'), item.get('AssociatedGroups'), item.get('Url'))
#                 self.cursor.execute(sql, values)
#                 self.conn.commit()
#             except mysql.connector.Error as err:
#                 if err.errno == 1062:  # MySQL error code for duplicate entry
#                     print("Duplicate entry found for the provided values in apt_group table.")
#                 else:
#                     print("An error occurred:", err)

#         elif isinstance(item, TechniquesTable):
#                 technique_id = item.get('ID')
#                 if not technique_id:
#                     raise ValueError("TechniquesTable item is missing the 'ID' field")
                
#                 sql = "INSERT INTO apt_group_techniques (techniques_id, description, domain_name, sub_id) VALUES (%s, %s, %s, %s)"
#                 values = (technique_id, item.get('Use'), item.get('Domain'), item.get('SubId'))

#                 input_string = item.get('References')
#                 links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_string)
#                 try:
#                     self.cursor.execute(sql, values)
#                     self.conn.commit()
#                 except (mysql.connector.Error, ValueError) as err:
#                     if isinstance(err, mysql.connector.Error) and err.errno == 1062:  # MySQL error code for duplicate entry
#                         print("Duplicate entry found for the provided values in apt_group_techniques table.")
#                     else:
#                         print("An error occurred:", err)
#                 for link in links:
#                     query = "INSERT INTO apt_technique_references (reference_link, apt_group_techniques_techniques_id,software_used_software_Id) VALUES (%s, %s,0)"
#                     ref_values = (link, technique_id)
#                     self.cursor.execute(query, ref_values)
                
#             #    software_used_software_Id
           

#         elif isinstance(item, SoftwareTable):
           
#                 sql = "INSERT INTO software_used(software_Id, name, techniques) VALUES (%s, %s, %s)"
#                 values = (item.get('ID'), item.get('Name'), item.get('Techniques'))
#                 software_Id = item.get('ID')
#                 links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', item.get('References'))
#                 try: 
#                     self.cursor.execute(sql, values)
#                     self.conn.commit()
#                 except mysql.connector.Error as err:
#                     if err.errno == 1062:  # MySQL error code for duplicate entry
#                         print("Duplicate entry found for the provided values in software_used table.")
#                     else:
#                         print("An error occurred:", err)
#                 for link in links:
#                     ref_values = (link, software_Id)
#                     # query = "INSERT INTO apt_technique_references (reference_link, software_used_software_Id) VALUES (%s, %s)"
#                     query="INSERT INTO apt_technique_references (reference_link, software_used_software_Id,apt_group_techniques_techniques_id) VALUES (%s, %s,0)"
#                     self.cursor.execute(query, ref_values)
               
           

#         elif isinstance(item, CompainsTable):
#             try:
#                 sql = "INSERT INTO CompainsTable(id, name, reference, techniques) VALUES (%s, %s, %s, %s)"
#                 values = (item.get('ID'), item.get('Name'), item.get('References'), item.get('Techniques'))
#                 self.cursor.execute(sql, values)
#                 self.conn.commit()
#             except mysql.connector.Error as err:
#                 if err.errno == 1062:  # MySQL error code for duplicate entry
#                     print("Duplicate entry found for the provided values in CompainsTable.")
#                 else:
#                     print("An error occurred:", err)

#         elif isinstance(item, SubTechniques):
#             try:
#                 sql = "INSERT INTO sub_id(id, name) VALUES (%s, %s)"
#                 values = (item.get('ID'), item.get('Name'))
#                 self.cursor.execute(sql, values)
#                 self.conn.commit()
#             except mysql.connector.Error as err:
#                 if err.errno == 1062:  # MySQL error code for duplicate entry
#                     print("Duplicate entry found for the provided values in sub_id table.")
#                 else:
#                     print("An error occurred:", err)

#         elif isinstance(item, ProcedureExamples):
#             try:    
#                 sql = "INSERT INTO procedure_example(id, name, description, reference) VALUES (%s, %s, %s, %s)"
#                 values = (item.get('ID'), item.get('Name'), item.get('Description'), item.get('Reference'))
#                 self.cursor.execute(sql, values)
#                 self.conn.commit()
#             except mysql.connector.Error as err:
#                 if err.errno == 1062:  # MySQL error code for duplicate entry
#                     print("Duplicate entry found for the provided values in procedure_example table.")
#                 else:
#                     print("An error occurred:", err)

#         elif isinstance(item, Mitigations):
#             try:    
#                 sql = "INSERT INTO mitigations(id, name, description, reference) VALUES (%s, %s, %s, %s)"
#                 values = (item.get('ID'), item.get('Name'), item.get('Description'), item.get('Reference'))
#                 self.cursor.execute(sql, values)
#                 self.conn.commit()
#             except mysql.connector.Error as err:
#                 if err.errno == 1062:  # MySQL error code for duplicate entry
#                     print("Duplicate entry found for the provided values in mitigations table.")
#                 else:
#                     print("An error occurred:", err)

#         return item

# Define yo ur item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import re
# import scrapy
# from itemadapter import ItemAdapter
# from elasticsearch import Elasticsearch

# ELASTICSEARCH_SETTINGS = {
#     'hosts': ['localhost:9200'],
# }

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

# class CompainsTable(scrapy.Item):
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
#     ID = scrapy.Field()
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

# class ElasticsearchPipeline:
#     def open_spider(self, spider):
#         self.es = Elasticsearch(**ELASTICSEARCH_SETTINGS)
#         self.index_name = 'cyber_security'

#         # Create index with parent-child relationship mappings
#         if not self.es.indices.exists(index=self.index_name):
#             self.es.indices.create(index=self.index_name, body={
#                 'mappings': {
#                     'properties': {
#                         'group_table': {
#                             'type': 'join',
#                             'relations': {
#                                 'group': ['technique', 'software', 'compain']
#                             }
#                         },
#                         'technique_table': {
#                             'type': 'join',
#                             'relations': {
#                                 'technique': ['software', 'mitigation', 'detection']
#                             }
#                         },
#                         'software_table': {
#                             'type': 'join',
#                             'relations': {
#                                 'software': ['mitigation']
#                             }
#                         },
#                         'references': {
#                             'type': 'nested',
#                             'properties': {
#                                 'url': {'type': 'text'}
#                             }
#                         }
#                     }
#                 }
#             })

#     def close_spider(self, spider):
#         pass

#     def process_item(self, item, spider):
#         item_type = type(item).__name__
#         document = ItemAdapter(item).asdict()
        
#         # Extract and process references as nested documents
#         if 'References' in document and document['References']:
#             references = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', document['References'])
#             document['References'] = [{'url': ref} for ref in references]

#         if item_type == 'GroupTable':
#             self.es.index(index=self.index_name, id=document['MittreName'], body={
#                 'group_table': 'group',
#                 **document
#             })
#         elif item_type == 'TechniquesTable':
#             self.es.index(index=self.index_name, id=document['ID'], routing=document['GroupId'], body={
#                 'group_table': {
#                     'name': 'technique',
#                     'parent': document['GroupId']
#                 },
#                 **document
#             })
#         elif item_type == 'SoftwareTable':
#             self.es.index(index=self.index_name, id=document['ID'], body={
#                 'group_table': 'software',
#                 **document
#             })
#         elif item_type == 'CompainsTable':
#             self.es.index(index=self.index_name, id=document['ID'], body={
#                 'group_table': 'compain',
#                 **document
#             })
#         elif item_type == 'SubTechniques':
#             self.es.index(index=self.index_name, id=document['ID'], body=document)
#         elif item_type == 'ProcedureExamples':
#             self.es.index(index=self.index_name, id=document['ID'], body=document)
#         elif item_type == 'Mitigations':
#             self.es.index(index=self.index_name, id=document['ID'], body=document)
#         elif item_type == 'Detections':
#             self.es.index(index=self.index_name, id=document['ID'], body=document)

#         return item



# import re
# import scrapy
# from itemadapter import ItemAdapter
# from elasticsearch import Elasticsearch, helpers

# ELASTICSEARCH_SETTINGS = {
#     'hosts': ['localhost:9200'],
# }
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
# ok#?
# class SoftwareTable(scrapy.Item):
#     ID = scrapy.Field()
#     Name = scrapy.Field()
#     References = scrapy.Field()
#     Techniques = scrapy.Field()
# dddd
# class CompainsTable(scrapy.Item):
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
#     ID = scrapy.Field()
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

# class ElasticsearchPipeline:
    # def open_spider(self, spider):
    #     self.es = Elasticsearch(**ELASTICSEARCH_SETTINGS)
    #     self.indexes = {
    #         'GroupTable': 'group_table',
    #         'TechniquesTable': 'techniques_table',
    #         'SoftwareTable': 'software_table',
    #         'CompainsTable': 'compains_table',
    #         'SubTechniques': 'sub_techniques',
    #         'ProcedureExamples': 'procedure_examples',
    #         'Mitigations': 'mitigations',
    #         'Detections': 'detections',
    #     }

#     def close_spider(self, spider):
#         pass

#     def process_item(self, item, spider):
#         index_name = self.indexes[type(item).__name__]
#         document = ItemAdapter(item).asdict()
        
#         # Optional: Process references as separate documents linked to the main document
#         if 'References' in document and document['References']:
#             references = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', document['References'])
#             document['References'] = references

#         self.es.index(index=index_name, body=document)
#         return item




import re
import scrapy
from elasticsearch import Elasticsearch, helpers

# Elasticsearch settings
ELASTICSEARCH_SETTINGS = {
    'hosts': 'http://localhost:9200',
    'index': 'etiapt',
    # 'timeout': 1500000000000,  # Increase the timeout value
    # 'max_retries': 3,
    # 'retry_on_timeout': True,
    
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

class SoftwareTable(scrapy.Item):
    ID = scrapy.Field()
    Name = scrapy.Field()
    References = scrapy.Field()
    Techniques = scrapy.Field()

class CompainsTable(scrapy.Item):
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
        self.es = Elasticsearch(["http://localhost:9200"])
        print
        self.actions = []
    # def index_action(self, action):
    #     try:
    #         if action:
    #             self.es.index(index='etiapt', body=action)
    #             print(f"Indexed action: {action}")
    #     except Exception as e:
    #         print(f"Error indexing action: {e}")
    def close_spider(self, spider):
        if self.actions:
        #     helpers.bulk(self.es, self.actions)
        # print("Connection closed")
            try:
                 for action in self.actions:
                    print("action is index", action["_index"])

                    try:
                        self.es.index(index='etiapt', body=action["_source"])
                    except Exception as e:
                        print(f"Error indexing document: {e}")
 
                 print("All actions have been indexed")
            except Exception as e:
                print(f"Error while indexing actions: {e}")
        # try:
        #     if self.actions:
        #         helpers.bulk(self.es, self.actions)
        #         print("All actions have been indexed")
        # except Exception as e:
        #     print(f"Error while closing spider and indexing actions: {e}")

    def process_item(self, item, spider):
        if isinstance(item, GroupTable):
            doc = {
                "join_field": "apt_group",
                "group_name": item.get('GroupName'),
                "summary": item.get('Summary'),
                "associated_groups": item.get('AssociatedGroups'),
                "group_url": item.get('Url')
            }
            action = {
                "_index": 'etiapt',
                "_source": doc
            }
            self.actions.append(action)

        elif isinstance(item, TechniquesTable):
            doc = {
                "join_field": "apt_group_techniques",
                "techniques_id": item.get('ID'),
                "description": item.get('Use'),
                "domain_name": item.get('Domain'),
                "sub_id": item.get('SubId')
            }
            action = {
                "_index": 'etiapt',
                "_source": doc
            }
            self.actions.append(action)
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', item.get('References'))
            for link in links:
                ref_doc = {
                    "join_field": "references",
                    "url": link,
                    "t_id": item.get('ID')
                }
                ref_action = {
                    "_index": ELASTICSEARCH_SETTINGS['index'],
                    "_source": ref_doc
                }
                self.actions.append(ref_action)

        elif isinstance(item, SoftwareTable):
            doc = {
                "join_field": "software_used",
                "s_id": item.get('ID'),
                "name": item.get('Name'),
                "technique": item.get('Techniques')
            }
            action = {
                "_index": 'etiapt',
                "_source": doc
            }
            self.actions.append(action)
            links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', item.get('References'))
            for link in links:
                ref_doc = {
                    "join_field": "references",
                    "url": link,
                    "s_id": item.get('ID')
                }
                ref_action = {
                    "_index": ELASTICSEARCH_SETTINGS['index'],
                    "_source": ref_doc
                }
                self.actions.append(ref_action)

        elif isinstance(item, CompainsTable):
            doc = {
                "join_field": "attack_campaign",
                "id": item.get('ID'),
                "case_name": item.get('Name'),
                "created_date": item.get('FirstSeen'),
                "modified_date": item.get('LastSeen'),
                "sources": item.get('References'),
                "method_tool_used": item.get('Techniques')
            }
            action = {
                "_index": 'etiapt',
                "_source": doc
            }
            self.actions.append(action)

        elif isinstance(item, SubTechniques):
            doc = {
                "join_field": "sub_techniques",
                "id": item.get('ID'),
                "name": item.get('Name')
            }
            action = {
                "_index": ELASTICSEARCH_SETTINGS['index'],
                "_source": doc
            }
            self.actions.append(action)

        elif isinstance(item, ProcedureExamples):
            doc = {
                "join_field": "procedure_example",
                "procedure_example_id": item.get('ID'),
                "name": item.get('Name'),
                "description": item.get('Description')
            }
            action = {
                "_index": ELASTICSEARCH_SETTINGS['index'],
                "_source": doc
            }
            self.actions.append(action)

        elif isinstance(item, Mitigations):
            doc = {
                "join_field": "mitigations",
                " m_id": item.get('ID'),
                "mitigation": item.get('Mitigation'),
                "description": item.get('Description')
            }
            action = {
                "_index": ELASTICSEARCH_SETTINGS['index'],
                "_source": doc
            }
            self.actions.append(action)

        return item
