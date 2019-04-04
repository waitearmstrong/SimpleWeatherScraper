import requests
from bs4 import BeautifulSoup
file = open("data.txt","a+")
url = 'https://www.usclimatedata.com/climate/morgantown/west-virginia/united-states/uswv0507/2018/12'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
table = soup.find('table', class_ = 'daily_climate_table')
highs = []
lows = []
sumHighs = 0.0
sumLows = 0.0
for row in table.find_all("tr"):
     for cell in row.find_all('td', class_ = 'temperature_red'):
         highs.append(float(cell.text))
for row in table.find_all("tr"):
     for cell in row.find_all('td', class_ = 'temperature_blue'):
         lows.append(float(cell.text))
for num in highs:
    sumHighs = sumHighs + num
for num in lows:
    sumLows = sumLows + num
print("The average high is: " + str(sumHighs/len(highs)))
print("The average low is: " + str(sumLows/len(lows)))

