from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import json

#uniform resour indentifier
uri = "mongodb+srv://pwskills:Dipak20Bisht@cluster0.s9yqn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Create databse name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

# read the data as a dataframe
df = pd.read_csv("C:\\Users\\hh\\Desktop\\Sensor-Fault-Detection\\notebooks\\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)


# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())


#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

