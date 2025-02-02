import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from convert import make_json

def getData(collection,document,ticker):
    cred = credentials.Certificate("./ServiceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    data = (db.collection(collection).document(document).get().to_dict())

    ticker = " " + ticker
    results={}
    for key in data:
        if data[key]["Symbol"] in results:
            results[data[key]["Symbol"]].append(data[key])
        else:
            results[data[key]["Symbol"]]=[data[key]]
    print(results[ticker])
    return(results[ticker])

whatCollection = input("What is the collection: ")
whatDocument = input("what is the document: ")
whatTicker = input("What is the ticker: ")

getData(whatCollection,whatDocument,whatTicker)