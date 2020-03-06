import matplotlib.pyplot as plt
import csv
from datetime import datetime

def main():
    open_file = open('P:\Spring 2020\Advanced Python\CSV_Project\matplotlib_csv\death_valley_2018_simple.csv', "r")  
    open_file2 = open("P:\Spring 2020\Advanced Python\CSV_Project\matplotlib_csv\sitka_weather_2018_simple.csv", "r") 

    DV_file = csv.reader(open_file, delimiter=",")  
    SA_file = csv.reader(open_file2, delimiter=',')  

    dates_D, highs_D, lows_D, station_name_D = get_attributes(DV_file)   
    dates_S, highs_S, lows_S, station_name_S = get_attributes(SA_file) 

    fig, (death, sitka) = plt.subplots(2)

    
    fig.subplots_adjust(hspace=0.5)

    death.set_title(station_name_D , fontsize =16) 
    
    death.plot(dates_D, highs_D, color='red', alpha= 0.8) 
    death.plot(dates_D, lows_D, color='blue', alpha = 0.8)

    sitka.plot(dates_S, highs_S, color='red', alpha= 0.8)
    sitka.plot(dates_S, lows_S, color='blue', alpha = 0.8)

    death.fill_between(dates_D, highs_D, lows_D, facecolor = "blue", alpha = 0.3) 
    sitka.fill_between(dates_S, highs_S, lows_S, facecolor = "blue", alpha = 0.3) 

    death.set_title(station_name_D , fontsize =16) 
    sitka.set_title(station_name_S , fontsize =16) 

    death.set_xlabel("", fontsize=8)
    sitka.set_xlabel("", fontsize=8)

    death.set_ylabel("Temperature in (F)",fontsize = 12)
    sitka.set_ylabel("Temperature in (F)",fontsize = 12)

    death.tick_params(axis="both", which="major" , labelsize= 12)
    sitka.tick_params(axis="both", which="major" , labelsize= 12)

    fig.autofmt_xdate()

    title_text = "Temperature comparison between" , station_name_D, "and", station_name_S
    title_text = str(title_text)
    new_title_text = convert(title_text)   
    fig.suptitle(new_title_text, fontsize = 15)  
    
    plt.show() 

def get_attributes(csv_file):
    header_row = next(csv_file)
    first_row = next(csv_file)  

    print(type(header_row))

    for index, column_header in enumerate(header_row):
        if column_header == "TMIN":
            TMIN_index = index
        if column_header == "TMAX":
            TMAX_index = index
        if column_header == "NAME":
            station_name_index = index

    station_name = first_row[station_name_index]  

    highs = []
    lows = []
    dates = []

    for row in csv_file:
        try:
            high = int(row[TMAX_index])
            low = int(row[TMIN_index])
            current_date = datetime.strptime(row[2], "%Y-%m-%d") 
        except ValueError:
            print(f"Missing data for {current_date}") 
        else: 
            highs.append(high)     
            lows.append(low)
            dates.append(current_date)
    

    return dates, highs, lows, station_name

def convert(weird_list): 
    symbols = [",", "(" , ")", "'"]
    converted_into_list = [x for x in weird_list if x not in symbols]    
    new = ""     
    for x in converted_into_list: 
        if x not in symbols:
            new += x        
    
    return new 

#print(highs[:10])

main()