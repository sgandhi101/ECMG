import sys
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def import_data(service_account_key_path, data_file, collection_name, name_of_document):
    try:
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        data = make_json(data_file)
        db.collection(collection_name).document(name_of_document).set(data)

    except Exception as error:
        print("\nERROR: {}".format(str(error)))
    else:
        print("\nImport complete")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            service_account_path = sys.argv[1]
            data_file_path = sys.argv[2]
            name_of_collection = sys.argv[3]
        else:
            service_account_path = input("Path to serviceAccountKey.json: ")
            data_file_path = input("Path to data file: ")
            name_of_collection = input("Name of collection: ")
            name_of_document = input("Name of document: ")

        import_data(service_account_path, data_file_path, name_of_collection,name_of_document)
    except KeyboardInterrupt as keyboard_error:
        print("\nProcess interrupted")
    finally:
        print("\nFinished!")