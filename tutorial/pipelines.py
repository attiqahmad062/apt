# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

# class TutorialPipeline:
#     def process_item(self, item, spider):
#         return item
#group pipeline
MYSQL_SETTINGS = {
    'host': 'localhost',
    'port': 3306,
    'database': 'etiapt',
    'user': 'root',
    'password': '7777',
}

class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(**MYSQL_SETTINGS)
        self.cursor = self.conn.cursor()
        print("conection est ")
    
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        print("called")
        sql = "INSERT INTO apt_group (mitre_name, group_name,summary) VALUES (%s, %s,%s)"
        values = (item.get('MittreName'), item.get('GroupName'), item.get('Summary'))
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item
#group_name varchar(255) 
# mitre_name varchar(255) 
# summary longtext 
# created_date datetime 
# modified_date