# import mysql.connector

# # MySQL database settings
# MYSQL_SETTINGS = {
#     'host': 'localhost',
#     'port': 3306,
#     'database': 'etiapt',
#     'user': 'root',
#     'password': '7777',
# }

# def main():
#     try:
#         # Connect to MySQL database
#         conn = mysql.connector.connect(**MYSQL_SETTINGS)
#         if conn.is_connected():
#             print("Connected to MySQL database")
#         cursor = conn.cursor() 
#         cursor.execute("select * from etiapt.sub_id")
#         rows=cursor.fetchall()
#         for row in rows:
#             print(row)
#         # Perform database operations here...

#         # Close connection
#         # conn.close()
#         print("Connection closed")
#     except mysql.connector.Error as error:
#         print("Error connecting to MySQL database:", error)

# if __name__ == "__main__":
#     main()

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

mapping = {
    "mappings": {
        "properties": {
            "join_field": {
                "type": "join",
                "relations": {
                    "apt_group": [
                        "attack_campaign",
                        "apt_group_attack_campaigns",
                        "apt_group_countries",
                        "apt_group_sectors",
                        "apt_group_techniques",
                        "software_used"
                    ],
                    "attack_campaign": [
                        "alias",
                        "attack_campaign_countries",
                        "attack_campaign_sectors"
                    ],
                    "apt_group_techniques": [
                        "software_used",
                        "mitigations",
                        "detections",
                        "procedure_example",
                        "references"
                    ],
                    "user_preference": [
                        "region_preference",
                        "sector_preference"
                    ]
                }
            },
            "apt_group": {
                "properties": {
                    "mitre_name": {"type": "keyword"},
                    "group_name": {"type": "keyword"},
                    "summary": {"type": "text"},
                    "associated_groups": {"type": "text"},
                    "group_url": {"type": "keyword"}
                }
            },
            "attack_campaign": {
                "properties": {
                    "id": {"type": "keyword"},
                    "name": {"type": "keyword"},
                    "first_seen": {"type": "date"},
                    "last_seen": {"type": "date"},
                    "references": {"type": "text"},
                    "techniques": {"type": "text"}
                }
            },
            "apt_group_techniques": {
                "properties": {
                    "techniques_id": {"type": "keyword"},
                    "description": {"type": "text"},
                    "domain_name": {"type": "keyword"},
                    "sub_id": {"type": "keyword"}
                }
            },
            "software_used": {
                "properties": {
                    "software_id": {"type": "keyword"},
                    "name": {"type": "keyword"},
                    "techniques": {"type": "text"}
                }
            },
            "mitigations": {
                "properties": {
                    "m_id": {"type": "keyword"},
                    "mitigation": {"type": "text"},
                    "description": {"type": "text"}
                }
            },
            "detections": {
                "properties": {
                    "id": {"type": "keyword"},
                    "data_source": {"type": "keyword"},
                    "data_component": {"type": "keyword"},
                    "detects": {"type": "text"}
                }
            },
            "procedure_example": {
                "properties": {
                    "procedure_example_id": {"type": "keyword"},
                    "name": {"type": "keyword"},
                    "description": {"type": "text"}
                }
            },
            "references": {
                "properties": {
                    "reference_id": {"type": "keyword"},
                    "url": {"type": "keyword"}
                }
            }
        }
    }
}

# Create the index with the mapping
index_name = "etiapt"
try:
   es.indices.create(index=index_name, body=mapping)
except:
 print(f"Index {index_name} created with mapping.")
# else:
#     print(f"Index {index_name} already exists.")

