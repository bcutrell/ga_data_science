# cleanup on the original data
df['DVOA'] = df['DVOA'].replace('%','',regex=True).astype('float')
df['DVAR'] = df['DVAR'].replace(',','',regex=True).astype('float')
df['Rating'] = df['Rating'].astype('float')
df['QBR'][df['Year'] == 2008] = np.nan
df['QBR'][df['Year'] == 2014] = np.nan
df['QBR'][df['Year'] == datetime(2013, 1, 1)] = np.nan
df['Year'] = df['Year'].astype('str')
df['Year'] = df['Year'].astype('datetime64')
