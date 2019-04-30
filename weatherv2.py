

import requests
import calendar
from bs4 import BeautifulSoup
file = open("data.txt","w")
url = 'https://www.usclimatedata.com/climate/morgantown/west-virginia/united-states/uswv0507/'
startYear = int(input("Enter your start year: "))
endYear = int(input("Enter your end year: "))
selectedYear = startYear
while (selectedYear <= endYear):
    urls = []
    count = 0
    while count < 12:
        urls.append(url + str(selectedYear) + "/" + str(count+1))
        count+=1
        
    ccc = 0
    yearHighs = []
    yearLows = []
    for url in urls:
        ccc +=1
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
        table = soup.find('table', class_ = 'daily_climate_table')
        highs = []
        lows = []
        sumHighs = 0.0
        sumLows = 0.0
        for row in table.find_all("tr"):
             for cell in row.find_all('td', class_ = 'temperature_red'):
                 try:
                     highs.append(float(cell.text))
                     yearHighs.append(float(cell.text))
                 except:
                     pass
                
        for row in table.find_all("tr"):
             for cell in row.find_all('td', class_ = 'temperature_blue'):
                 try:
                     lows.append(float(cell.text))
                     yearLows.append(float(cell.text))
                 except:
                    pass
        for num in highs:
            sumHighs = sumHighs + num
        for num in lows:
            sumLows = sumLows + num
        try:
            file.write(str(selectedYear) + ","+ str(ccc) + "," + str(sumLows/len(lows)))
            file.write(str(selectedYear) + ","+ str(ccc) + "," + + str(sumHighs/len(highs)))
        except:
            file.write("Bad data for: " + str(selectedYear))
            pass
    for num in yearHighs:
            sumHighs = sumHighs + num
    for num in yearLows:
            sumLows = sumLows + num
    print("The average low for the year " + str(selectedYear) + " is: " + str(sumLows/len(yearLows)))
    print("The average high for the year " + str(selectedYear) + " is: " + str(sumHighs/len(yearHighs)))
    selectedYear = selectedYear + 1
