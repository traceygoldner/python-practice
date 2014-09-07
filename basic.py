import requests
import csv
from BeautifulSoup import BeautifulSoup

### Step 1: Open and read the URL ###

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Agency/Employees.aspx?letter=0&agency=350&year=2014'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)


### Step 2: Parse html with BeautifulSoup ###

results_table = soup.find('table', attrs={'id': 'grdEmployees'})

output = []

for row in results_table.findAll('tr'):

    output_row = []
	
    for cell in row.findAll('td'):
        output_row.append(cell.text)
      
    output.append(output_row)

csv_file = open('salaries.csv', 'w')
writer = csv.writer(csv_file)
writer.writerows(output)






