import matplotlib.pyplot as plt
import csv

open_file = open("P:\Spring 2020\Advanced Python\CSV_Project\matplotlib_csv\sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

#print(type(header_row))

#for index,column_header in enumerate(header_row):
    #print(index,column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs[:10])


plt.plot(highs, color = 'red')
plt.title("daily high temps, July 2018", fontsize=16)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which="major",labelsize=16)

plt.show()