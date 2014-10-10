import code # code.interact(local=locals())
import pandas as pd
import numpy as np
file_path = '../../Desktop/movies.txt'
file_path_2 = '../../Desktop/amazon-meta.txt'

## terminal command
## head -n 10000 amazon-meta.txt > small-amazon-meta.txt

''' Manipulate DF '''
headers = ['product/productId', 'review/userId', 'review/profileName',
'review/helpfulness', 'review/score', 'review/time',
'review/summary','review/text']

## ^\s*$
## \n\s*\n
## df = pd.read_table(file_path, nrows=10000, delimiter=':', error_bad_lines=False, header=None, names=headers)
#df = pd.read_table(file_path, compression='gzip', nrows=10000)
## df = pd.read_table(file_path_2, nrows=10000, sep=':', error_bad_lines=False, comment='#', skiprow)

with open(file_path_2) as myFile:
  head = [next(myFile) for line in xrange(10000)]

full_set = []
obj_set = []
for line in head:
  if line == '\r\n':
    full_set.append(item)
    obj_set = []
  else:
    try:
      column, data = line.split(':')
      item = {column : data }
      obj_set.append(item)
    except:
      pass

''' Manipulate Lines '''
with open(file_path) as myFile:
  head = [next(myFile) for line in xrange(10000)]

table_data = []
product, userId = [ None, None ]
item = {}

for line in head:
  delim = line.find(':')
  column = line[:delim]
  data = line[delim+1:].strip()
  table_row = { column: data }

  if column == 'review/userId' and data != userId:
    if len(item.keys()) != 0:
      table_data.append(item)
      if not item['product/productId']:
        item['product/productId'] = product
    item = {}

  if column == 'review/userId':
    userId = data

  if column == 'product/productId' and data != product:
    if len(item.keys()) != 0:
      table_data.append(item)
    item = {}

  if column == 'product/productId':
    product = data
    item[column] = data

    try:
      table[product]
    except:
      table[product] = []

  else:
    try:
      table[product].append(table_row)
      item[column] = data
    except:
      pass

df = pd.DataFrame(table_data)
code.interact(local=locals())

# df.to_csv('~/Desktop/movies_small.csv',mode='w')

# some random notes
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')

# yearly
# map years
df_map = {}
for yr in df['Year'].unique():
  df_map[yr] = df[df['Year'] == yr]
xy_map = {}
for yr, df_values in df_map.items():
  y, X = dmatrices(regr, data=df_values, return_type='dataframe')
  xy_map[yr] = {'y': y, 'X': X}