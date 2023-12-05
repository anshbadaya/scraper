import requests
import pymongo
import json
from datetime import datetime
import pytz

# MongoDB connection information
mongo_uri = "mongodb://localhost:27017/"
database_name = "tabodata"
collection_name = "processed"
client = pymongo.MongoClient(mongo_uri)
database = client[database_name]


def scrape_data():
    try:
        url = "https://api.tomorrow.io/v4/weather/history/recent?location=32.0933%2C78.3856&apikey=sxHAwNP8J1K91D9awHoyHkQE0UmH0I0c"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.text
        data_dict = json.loads(data)
        return data_dict
    except Exception as e:
        print(e)


def insert_unprocessed_data(data):
    try:
        collection_name = "unprocessed"
        collection = database[collection_name]
        result = collection.insert_one(data)
    except Exception as e:
        print(e)


def insert_processed_data(data):
    try:
        collection_name = "processed"
        collection = database[collection_name]
        result = collection.insert_one(data)
    except Exception as e:
        print(e)


def main():

    data = scrape_data()

    result = data.get("timelines").get("hourly")
    for datapoint in result:
        try:
            insert_unprocessed_data(datapoint)

            processed_data = {}
            datetime_string = datapoint.get("time")

            date_format = "%Y-%m-%dT%H:%M:%SZ"
            india_timezone = pytz.timezone('Asia/Kolkata')

            datetime_object = datetime.strptime(datetime_string, date_format)
            indian_datetime = datetime_object.replace(
                tzinfo=pytz.utc).astimezone(india_timezone)

            formatted_string = indian_datetime.strftime(date_format)

            processed_data["time"] = formatted_string
            processed_data["temperature"] = datapoint.get(
                "values").get("temperature")

            insert_processed_data(processed_data)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
