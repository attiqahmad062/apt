# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

# class TutorialPipeline:
#     def process_item(self, item, spider):
#         return item
# group pipeline
MYSQL_SETTINGS = {
    'host': 'localhost',
    'port': 3306,
    'database': 'etiapt',
    'user': 'root',
    'password': '7777',#7777:1234
}
class GroupTable (scrapy.Item):
    MittreName=scrapy.Field()
    GroupName=scrapy.Field()
    Summary=scrapy.Field()
    AssociatedGroups=scrapy.Field()
    Url=scrapy.Field()
   
class TechniquesTable(scrapy.Item):
    ID=scrapy.Field()
    Use=scrapy.Field()
    Domain=scrapy.Field()
    References=scrapy.Field()
    SubId=scrapy.Field()
    GroupId= scrapy.Field()
   
class SoftwareTable(scrapy.Item):
    ID=scrapy.Field()
    Name=scrapy.Field()
    References=scrapy.Field()
    Techniques=scrapy.Field()
class CompainsTable(scrapy.Item):
    ID=scrapy.Field()
    Name=scrapy.Field()
    FirstSeen=scrapy.Field()
    LastSeen=scrapy.Field()
    References=scrapy.Field()
    Techniques=scrapy.Field()
class SubTechniques(scrapy.Item):
    ID=scrapy.Field()
    Name=scrapy.Field()
   
class ProcedureExamples(scrapy.Item):
    Id=scrapy.Field()
    Name=scrapy.Field()
    Description=scrapy.Field()
class Mitigations(scrapy.Item):
    ID=scrapy.Field()
    Mitigation=scrapy.Field()
    Description=scrapy.Field()
class Detections(scrapy.Item):
    ID=scrapy.Field()
    DataSource=scrapy.Field()
    DataComponent=scrapy.Field()
    Detects=scrapy.Field()
class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(**MYSQL_SETTINGS)
        self.cursor = self.conn.cursor()
        print("conection est ")
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, GroupTable): 
            try:
                sql = "INSERT INTO apt_group (mitre_name, group_name, summary, associated_groups, group_url) VALUES (%s, %s, %s, %s, %s)"
                values = (item.get('MittreName'), item.get('GroupName'), item.get('Summary'), item.get('AssociatedGroups'), item.get('Url'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        elif isinstance(item,TechniquesTable):
            try:
                
                sql = "INSERT INTO apt_group_techniques (groups_id ,techniques_id, description, domain_name,reference,sub_id ) VALUES (%s, %s, %s,%s,%s,%s)"
                values = (item.get('GroupId'),item.get('ID'), item.get('Use'), item.get('Domain'),item.get('References'),item.get('SubId'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        elif isinstance(item,SoftwareTable):
            try: 
                sql = "INSERT INTO software_used ( id, name, reference,techniques ) VALUES (%s, %s, %s,%s)"
                values = ( item.get('ID'), item.get('Name'), item.get('References',),item.get('Techniques'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        elif isinstance(item,CompainsTable):
            try:
                sql = "INSERT INTO CompainsTable ( id, name, reference,techniques ) VALUES (%s, %s, %s,%s)"
                values = ( item.get('ID'), item.get('Name'), item.get('References',),item.get('Techniques'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        elif isinstance(item,SubTechniques):
            try:
                sql = "INSERT INTO sub_id ( id, name) VALUES (%s, %s)"
                values = ( item.get('ID'), item.get('Name'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        elif isinstance(item,ProcedureExamples):
            try:    
                sql = "INSERT INTO procedure_example ( id, name,description,reference) VALUES (%s, %s,%s,%s)"
                values = ( item.get('ID'), item.get('Name'),item.get('Description'),item.get('Reference'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        elif isinstance(item,Mitigations):
            try:    
                sql = "INSERT INTO procedure_example ( id, name,description,reference) VALUES (%s, %s,%s,%s)"
                values = ( item.get('ID'), item.get('Name'),item.get('Description'),item.get('Reference'))
                self.cursor.execute(sql, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:  # MySQL error code for duplicate entry
                    print("------------Duplicate entry found for the provided values in apt_group table.--------------")
                else:
                    print("--------------An error occurred:-----------------", err)
                    print("An error occurred:", err)
        return item
        
#group_name varchar(255) 
# mitre_name varchar(255) 
# summary longtext 
# created_date datetime 
# modified_date
 