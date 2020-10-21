import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from convert import make_json

cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

data = (db.collection("data").document("q1").get().to_dict())


results={}
for key in data:
    if data[key]["Symbol"] in results:
        results[data[key]["Symbol"]].append(data[key])
    else:
        results[data[key]["Symbol"]]=[data[key]]

print(results[" BEP"])