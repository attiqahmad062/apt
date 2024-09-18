import os
import spacy
from SPARQLWrapper import SPARQLWrapper, JSON

GRAPHDB_SETTINGS = {
    'endpoint': 'http://localhost:7200/repositories/etiapt/statements',
    'prefix': 'https://attack.mitre.org/'
}

class NERPipeline:
    def open_spider(self, spider):
        self.sparql = SPARQLWrapper(GRAPHDB_SETTINGS['endpoint'])
        print("Connection to GraphDB established for NER")
    def close_spider(self, spider):
        # GraphDB connection does not need explicit closing
        pass
    def process_item(self, item, spider):
        # Step 1: Fetch Group data from GraphDB
        group_query = """
        PREFIX ex: <https://attack.mitre.org/>
        SELECT ?group ?description WHERE {
            ?group ex:description ?description .
        }
        """
        print("result are ",group_query) 
        self.sparql.setQuery(group_query)
        group_results = self.sparql.query().convert()
        print("result are ",group_results) 
        # Step 2: Perform NER on Group descriptions
        for result in group_results["results"]["bindings"]:
            group_uri = result["group"]["value"]
            description = result["description"]["value"]
            print("description is ",description)
            doc = self.nlp(description)
       
            group_entities = {
                "GroupName": "",
                "Date": "",
                "Country": "",
                "Motivation": "",
                "Aliases": []
            }

            # Extract entities based on labels
            for ent in doc.ents:
                if ent.label_ == "ORG":  # Organization or Group Name
                    group_entities["GroupName"] = ent.text
                    print("ORG",ent.text)
                elif ent.label_ == "DATE":  # Dates
                    group_entities["Date"] = ent.text
                elif ent.label_ == "GPE":  # Country/Location
                    group_entities["Country"] = ent.text
                elif ent.label_ == "MISC":  # Motivation
                    group_entities["Motivation"] = ent.text
                elif ent.label_ == "PERSON":  # Aliases
                    group_entities["Aliases"].append(ent.text)

            print(f"Extracted Group Entities: {group_entities}")
            self.store_group_entities(group_uri, group_entities)

        # Step 5: Fetch Technique data from GraphDB
        # technique_query = """
        # PREFIX ex: <https://attack.mitre.org/>
        # SELECT ?technique ?use WHERE {
        #     ?technique ex:use ?use .
        # }
        # """
        # self.sparql.setQuery(technique_query)
        # technique_results = self.sparql.query().convert()

        # # Step 6: Perform NER on Technique "use" field
        # for result in technique_results["results"]["bindings"]:
        #     technique_uri = result["technique"]["value"]
        #     use_description = result["use"]["value"]
        #     doc = self.nlp(use_description)

        #     technique_entities = {
        #         "ORG": "",
        #         "Malware": "",
        #         "GroupNames": [],
        #         "Tools": [],
        #         "Tactics": ""
        #     }

        #     # Extract entities from the "use" field
        #     for ent in doc.ents:
        #         if ent.label_ == "ORG":  # Organizations involved
        #             technique_entities["ORG"] = ent.text
        #         elif ent.label_ == "MALWARE":  # Malware used
        #             technique_entities["Malware"] = ent.text
        #         elif ent.label_ == "PERSON":  # Group Names
        #             technique_entities["GroupNames"].append(ent.text)
        #         elif ent.label_ == "PRODUCT":  # Tools
        #             technique_entities["Tools"].append(ent.text)
        #         elif ent.label_ == "TACTIC":  # Tactics
        #             technique_entities["Tactics"] = ent.text

        #     print(f"Extracted Technique Entities: {technique_entities}")
        #     self.store_technique_entities(technique_uri, technique_entities)

        return item

    def  store_group_entities(self, group_uri, group_entities):
        """Store the NER results for Groups into GraphDB."""
        # Construct SPARQL UPDATE query for each property

        # Store Group Name (if exists)
        if group_entities["GroupName"]:
            group_name_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{group_uri}> ex:groupName ?oldName }}
            INSERT {{ <{group_uri}> ex:groupName "{group_entities['GroupName']}" }}
            WHERE {{ <{group_uri}> ex:description ?desc }}
            """
            self.sparql.setQuery(group_name_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Date (if exists)
        if group_entities["Date"]:
            date_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{group_uri}> ex:date ?oldDate }}
            INSERT {{ <{group_uri}> ex:date "{group_entities['Date']}" }}
            WHERE {{ <{group_uri}> ex:description ?desc }}
            """
            self.sparql.setQuery(date_query)
            self.sparql.method = 'POST'
            self.sparql.query()
        # Store Country (if exists)
        if group_entities["Country"]:
            country_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{group_uri}> ex:country ?oldCountry }}
            INSERT {{ <{group_uri}> ex:country "{group_entities['Country']}" }}
            WHERE {{ <{group_uri}> ex:description ?desc }}
            """
            self.sparql.setQuery(country_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Motivation (if exists)
        if group_entities["Motivation"]:
            motivation_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{group_uri}> ex:motivation ?oldMotivation }}
            INSERT {{ <{group_uri}> ex:motivation "{group_entities['Motivation']}" }}
            WHERE {{ <{group_uri}> ex:description ?desc }}
            """
            self.sparql.setQuery(motivation_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Aliases (if exists)
        for alias in group_entities["Aliases"]:
            alias_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{group_uri}> ex:alias ?oldAlias }}
            INSERT {{ <{group_uri}> ex:alias "{alias}" }}
            WHERE {{ <{group_uri}> ex:description ?desc }}
            """
            self.sparql.setQuery(alias_query)
            self.sparql.method = 'POST'
            self.sparql.query()

    def store_technique_entities(self, technique_uri, technique_entities):
        """Store the NER results for Techniques into GraphDB."""
        # Store ORG (if exists)
        if technique_entities["ORG"]:
            org_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{technique_uri}> ex:org ?oldOrg }}
            INSERT {{ <{technique_uri}> ex:org "{technique_entities['ORG']}" }}
            WHERE {{ <{technique_uri}> ex:use ?useDesc }}
            """
            self.sparql.setQuery(org_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Malware (if exists)
        if technique_entities["Malware"]:
            malware_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{technique_uri}> ex:malware ?oldMalware }}
            INSERT {{ <{technique_uri}> ex:malware "{technique_entities['Malware']}" }}
            WHERE {{ <{technique_uri}> ex:use ?useDesc }}
            """
            self.sparql.setQuery(malware_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Group Names (if exists)
        for group_name in technique_entities["GroupNames"]:
            group_name_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{technique_uri}> ex:groupName ?oldGroupName }}
            INSERT {{ <{technique_uri}> ex:groupName "{group_name}" }}
            WHERE {{ <{technique_uri}> ex:use ?useDesc }}
            """
            self.sparql.setQuery(group_name_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Tools (if exists)
        for tool in technique_entities["Tools"]:
            tool_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{technique_uri}> ex:tool ?oldTool }}
            INSERT {{ <{technique_uri}> ex:tool "{tool}" }}
            WHERE {{ <{technique_uri}> ex:use ?useDesc }}
            """
            self.sparql.setQuery(tool_query)
            self.sparql.method = 'POST'
            self.sparql.query()

        # Store Tactics (if exists)
        if technique_entities["Tactics"]:
            tactics_query = f"""
            PREFIX ex: <https://attack.mitre.org/>
            DELETE {{ <{technique_uri}> ex:tactics ?oldTactics }}
            INSERT {{ <{technique_uri}> ex:tactics "{technique_entities['Tactics']}" }}
            WHERE {{ <{technique_uri}> ex:use ?useDesc }}
            """
            self.sparql.setQuery(tactics_query)
            self.sparql.method = 'POST'
            self.sparql.query()
           
