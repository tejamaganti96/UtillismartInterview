import csv
import sqlite3
from email.headerregistry import Address
#from typing_extensions import Self

reading_list = []

class Meter:
    def __init__(self,SN, Manu_name, Manu_model, Install_date, Address, Latitude, Longitude, TotalDailyUsage,UnitOfMeasure, reading_timestamp, reading_value):
        self.SN = SN
        self.Manu_name = Manu_name
        self.Manu_model= Manu_model
        self.Install_date = Install_date
        self.Address = Address
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.TotalDailyUsage = TotalDailyUsage
        self.UnitOfMeasure = UnitOfMeasure
        self.reading_timestamp = reading_timestamp
        self.reading_value = reading_value

with open('inputs/sample_readings.csv', 'r') as readings:
    lines = csv.reader(readings, delimiter=',')
    for row in lines:
        curr = Meter(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        reading_list.append(curr)

reading_list.sort(key = lambda x: x.SN)
reading_list.sort(key = lambda x: x.Manu_name)

conn = sqlite3.connect('Readings.db')
cur = conn.cursor()

for i in range(len(reading_list)):
    cur.execute("Insert into Readings Values(?,?,?,?,?,?,?,?,?,?,?)", 
        (reading_list[i].SN, 
        reading_list[i].Manu_name, 
        reading_list[i].Manu_model, 
        reading_list[i].Install_date, 
        reading_list[i].Address, 
        reading_list[i].Latitude, 
        reading_list[i].Longitude, 
        reading_list[i].TotalDailyUsage,
        reading_list[i].UnitOfMeasure,
        reading_list[i].reading_timestamp,
        reading_list[i].reading_value))
conn.commit



for row in cur.execute("Select Count (*), Manu_Name ,Max(reading_value), Min(reading_value), avg(reading_value) from Readings where Manu_Name = ? group by Manu_Name", ('WindWindWind',) ):
    print(row)
# for i in range(20):
#     print(reading_list[i].SN, reading_list[i].Manu_name, reading_list[i].TotalDailyUsage)
#print(reading_list.SN for reading_list in x)

