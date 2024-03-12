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
    'password': '1234',
}

class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(**MYSQL_SETTINGS)
        self.cursor = self.conn.cursor()
        print("conection est ")
    
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
       
        try:
            sql = "INSERT INTO apt_group (mitre_name, group_name, summary, associated_groups, group_url) VALUES (%s, %s, %s, %s, %s)"
            values = (item.get('MittreName'), item.get('GroupName'), item.get('Summary'), item.get('AssociatedGroups'), item.get('Url'))
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            if err.errno == 1062:  # MySQL error code for duplicate entry
                print("Duplicate entry found for the provided values in apt_group table.")
            else:
                print("An error occurred:", err)
        

        return item
#group_name varchar(255) 
# mitre_name varchar(255) 
# summary longtext 
# created_date datetime 
# modified_date