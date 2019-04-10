import requests
import calendar
from bs4 import BeautifulSoup
url = 'https://www.usclimatedata.com/climate/morgantown/west-virginia/united-states/uswv0507/'
urls = []
count = 0
while count < 12:
    urls.append(url + "2017/" + str(count+1))
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
    print("The average low for " + calendar.month_name[ccc] + " is: " + str(sumLows/len(lows)))
    print("The average high is: " + calendar.month_name[ccc] + " is: " + str(sumHighs/len(highs)))
for num in yearHighs:
        sumHighs = sumHighs + num
for num in yearLows:
        sumLows = sumLows + num
print("The average low for the year is: " + str(sumLows/len(yearLows)))
print("The average high for the year is: " + str(sumLows/len(yearHighs)))
