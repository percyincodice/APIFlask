from flask import jsonify
import json
import os
import uuid

class PersonDA:

    @staticmethod
    def createPerson(body):
        try:
            if os.path.exists("database_temp.json"):
                with open("database_temp.json", "r", encoding="utf-8") as fh:
                    try:
                        data = json.load(fh)
                    except Exception as e1:
                        data = []
            else:
                data = []


            body["id"] = str(uuid.uuid4())
            data.append(body)

            with open("database_temp.json", "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2)

            return jsonify({"message": "Person created!!!!!!", "id": body["id"]}), 201

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error in person DA."}), 500

    @staticmethod
    def listPerson():
        try:
            if os.path.exists("database_temp.json"):
                with open("database_temp.json", "r", encoding="utf-8") as fh:
                    try:
                        data = json.load(fh)
                    except Exception as e1:
                        data = []
            else:
                data = []       

            return jsonify(data), 200

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error in list person."}), 500


    @staticmethod
    def getPersonById(person_id):
        try:
            if os.path.exists("database_temp.json"):
                with open("database_temp.json", "r", encoding="utf-8") as fh:
                    try:
                        data = json.load(fh)
                    except Exception as e1:
                        data = []
            else:
                data = [] 


            person = next((p for p in data if p.get("id") == person_id), None)

            if person:
                return jsonify(person), 200
            else:
                return jsonify({"message": "Person not found."}), 404

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error in list person."}), 500



    @staticmethod
    def updatePersonById(person_id, body):
        try:
            if os.path.exists("database_temp.json"):
                with open("database_temp.json", "r", encoding="utf-8") as fh:
                    try:
                        data = json.load(fh)
                    except Exception as e1:
                        data = []
            else:
                return jsonify({"message": "Person not found."}), 404

            person_found = False

            for index, person in enumerate(data):
                if person.get("id") == person_id:
                    body["id"] = person_id
                    data[index] = body
                    person_found = True
                    break

            if not person_found:
                return jsonify({"message": "Person not found."}), 404

            
            with open("database_temp.json", "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2)

            return jsonify({"message": "Person updated."}), 200

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error in update person."}), 500