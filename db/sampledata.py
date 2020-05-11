import sqlite3
import json
#import pdb

connection = sqlite3.connect('data.db')
parkingdatas = json.load(open('sample.json'))
cursor = connection.cursor()
# pdb.set_trace()

create_table = "CREATE TABLE parkingdata (id int, address text, totalspace int, freespace int, latitude real , longitude real, name text)"
cursor.execute(create_table)
converintojson = json.dumps(parkingdatas)
parsedDatas = json.loads(converintojson)

for parsedData in parkingdatas:
    id = parsedData["ParkingStationId"]
    address = parsedData["Address"]
    totalspace = parsedData["Totalspace"]
    freespace = parsedData["Freespace"]
    lat = parsedData["Coordinates"][1]
    lon = parsedData["Coordinates"][0]
    name = parsedData["Name"]
    print("processing data...")
    cursor.execute("INSERT INTO parkingdata (id, address, totalspace, freespace, latitude, longitude, name) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, address, totalspace, freespace, lat, lon, name))
    connection.commit()
connection.close()
print("Processing sample data complete.")
