import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

#####
# https://www.kaggle.com/code/ismaeldwikat/predict-trip-duration/notebook
csv.field_size_limit(sys.maxsize)
file = 'nyc_taxi_trip.csv'
datetime_format = '%m/%d/%Y %I:%M:%S %p'
license_num = dict()
base_num = dict()
pick_up = dict()
drop_off = dict()
#####

def get_time_difference(t1, t2):
    datetime_obj1 = datetime.strptime(t1, datetime_format)
    datetime_obj2 = datetime.strptime(t2, datetime_format)
    return datetime_obj1 - datetime_obj2
    # print(datetime_obj1, datetime_obj2)


if __name__ == "__main__":
    with open(file, newline="") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            try:
                dif = str(get_time_difference(row[3], row[2]))
                lic = row[0].strip()
                base = row[1].strip()
                pick = row[4].strip()
                drop = row[5].strip()
                if lic in license_num:
                    license_num[lic].append(dif)
                else:
                    license_num[lic] = [dif]

                if base in base_num:
                    base_num[base].append(dif)
                else:
                    base_num[base] = [dif]
                
                if pick in pick_up:
                    pick_up[pick] = pick_up[pick]+1
                else:
                    pick_up[pick] = 1
                
                if drop in drop_off:
                    drop_off[drop] = drop_off[drop]+1
                else:
                    drop_off[drop] = 1
                            
            except ValueError as e:
                print(f"Error parsing datetime string '{ row[2]}': {e}")
                print(row)
        # print(license_num)
        val = []
        val2 = []
        val3 = []
        val4 = []
        for key in license_num:
            # print(key, len(license_num[key]))
            val.append(len(license_num[key]))
        print("------------")
        for key in base_num:
            # print(key, len(base_num[key]))
            val2.append(len(base_num[key]))
        license = list(license_num.keys())

        for key in pick_up:
            val3.append(pick_up[key])
        pick_up_location = list(pick_up.keys())

        for key in drop_off:
            val4.append(drop_off[key])
        drop_off_location = list(drop_off.keys())

        # value = list(license_num.values())
        plt.figure(1)
        plt.bar(license, val)
        plt.xlabel('License Number')
        plt.ylabel('Number of Trips')
        plt.title('License Number v/s Trips')
        # plt.show()

        base = list(base_num.keys())
        plt.figure(2)
        plt.bar(base, val2)
        plt.xlabel('Base Number')
        plt.ylabel('Number of Trips')
        plt.title('Base Number v/s Trips')
        

        plt.figure(3)
        plt.bar(pick_up_location, val3)
        plt.xlabel('Pick up location')
        plt.ylabel('Count')
        plt.title('Pick up location v/s Count')

        plt.figure(4)
        plt.bar(drop_off_location, val4)
        plt.xlabel('Drop off location')
        plt.ylabel('Count')
        plt.title('Drop off location v/s Count')

        plt.show()

        