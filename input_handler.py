import csv

input_col_header = [
      "SN"
    , "Manu_name"
    , "Manu_model"
    , "Install_date"
    , "Address"
    , "Latitude"
    , "Longitude"
    , "TotalDailyUsage"
    , "UnitOfMeasure"
    , "reading_timestamp"
    , "reading_value"]

readings_list = []

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


def Readinput():
    with open('inputs/sample_readings.csv', 'r') as readings:
        lines = csv.reader(readings, delimiter=',')
        for row in lines:
            curr = Meter(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
            readings_list.append(curr)
    return readings_list
    
def sortInput():
    readings_list.sort(key = lambda x: x.SN)
    readings_list.sort(key = lambda x: x.Manu_name)

    return readings_list