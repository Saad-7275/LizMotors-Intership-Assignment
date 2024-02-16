#!/usr/bin/env python
# coding: utf-8

# ### Canoo's Financial Performance

# ### Income Statement -:

# In[6]:


import requests

from bs4 import BeautifulSoup


# In[7]:


response = requests.get('https://investors.canoo.com/financial-information/income-statement')

response


# In[23]:


soup = BeautifulSoup(response.content, 'html.parser')

income_statement_table = soup.find('table', {'class' :'report'})

print(income_statement_table.prettify())


# In[35]:


rows = income_statement_table.find_all('tr')

for row in rows:
    cells = row.find_all(['th', 'td'])
    for cell in cells:
        print(cell.text.strip())
        



# In[36]:


from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://investors.canoo.com/financial-information/income-statement')

response

#Parse HTML 

soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
income_statement_table = soup.find('table', {'class': 'report'})

# Extract table headers
headers = []
for th in income_statement_table.find_all('th'):
    headers.append(th.text.strip())

# Extract table rows
rows = []
for tr in income_statement_table.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all(['td', 'th'])]
    if row:
        rows.append(row)

print(rows)


# In[38]:


import pandas as pd

df = pd.DataFrame(rows, columns = ['Condensed Consolidated Statements of Operations - USD, $ in Thousands', 'Sep. 30, 2023', 'Sep. 30, 2022', 'Sep. 30, 2023', 'Sep. 30, 2022'])
df


# In[39]:


df.to_csv('income_statement_table.csv')


# ### Balance Sheet

# In[41]:


response = requests.get("https://investors.canoo.com/financial-information/balance-sheet")
response.status_code


# In[42]:


data = BeautifulSoup(response.content, 'html.parser')
print(data.prettify())


# In[43]:


balance_sheet = data.find('table', {'class': 'report'})

headers = []
for th in balance_sheet.find_all('th'):
    headers.append(th.text.strip())
    
rows = []
for tr in balance_sheet.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all(['td', 'th'])]
    rows.append(row)
print(rows)


# In[46]:


import pandas as pd
df = pd.DataFrame(rows, columns = ['Current assets', 'Sep. 30, 2023', 'Dec. 31, 2022'])
df

