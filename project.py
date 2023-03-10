import requests
import plotext as plt
from tabulate import tabulate
import json
from tqdm import tqdm
import time

dict1 = { "Choose your number!" : ['1','2','3','4','5','6','7','8'],
            "Indicator" : ['GDP','GDP per Capita PPP','GDP Growth Rate','Inflation Rate','Unemployment Rate','Fertility rate',
            'CO2 Emissions per capita','Life expectancy'] }

def main():
    countries = input("Which countries do you want visually representated(seperate it with ,)? ").split(", ")
    print(table())
    y = input("Which indicator to graph? ")
    indicator = dict1['Indicator'][(int(y) - 1)]
    inputdata = {"indicator":indicator, "countries": countries}
    
    print()
    #with tqdm(total=delay_duration * 1000) as progress_bar:

    output = requests.post("http://127.0.0.1:8080/process", json = inputdata)
        
      #  for i in range(delay_duration * 1000):
     #       time.sleep(0.001)
     #       progress_bar.update(1)
    #print()

    output = output.json()
    
    plt.bar(countries, output["data"], orientation = "h", width = 0.3, marker = 'fhd') 
    plt.title(output["indicator"])
    plt.clc() 
    plt.plotsize(100, (2 * len(countries) - 1) + 4) 
    plt.show()
    
    
def table(): 
    table = tabulate(dict1, headers="keys", tablefmt="pretty")
    return table

main()