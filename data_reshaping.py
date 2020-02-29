#######################################Borrowed from stackoverflow##############################################

################ VlookUp values of one column based on another dataframe 
# Create sample DataFrames (data = delivery information, bands = lookup volume band, tariff = lookup cost by band):
data = pd.DataFrame(columns = ['Customer', 'Zip', 'Volume'], 
                    data = [['A', 'RG', 0.7], ['B', 'KT', 1.3], ['C', 'NN', 1.8], ['D', 'PO', 2.4]])
bands = pd.DataFrame(columns = ['Volume', 'Band'], 
                    data = [[0.5, '1'], [1, '2'], [1.5, '3'], [2, '4'], [2.5, '5']])
tariff = pd.DataFrame(columns = ['Zip', '1', '2', '3', '4', '5'], 
                    data = [['RG', 10, 20, 30, 40, 50], ['KT', 12, 24, 36, 48, 60],
                            ['NN', 14, 28, 42, 56, 70], ['PO', 16, 32, 48, 64, 80]])

# Create DataFrame that has delivery data and the respective volume band each line falls into:
data_banded = pd.merge_asof(data, bands, on = 'Volume', direction = 'forward')

# Lookup the cost from the tariff table and apply to a new column called 'Cost' in the delivery data:
data_banded['Cost'] = tariff.set_index('Zip').lookup(data_banded['Zip'], data_banded['Band'])


################ Reanme Columns based on another #################
df = df.rename(columns=dict(zip(feature_lib['old_val'],
                             feature_lib['new_val'])))

################ Comning multiple features #####################
df = pd.DataFrame([['001', 'a', 1, 10, 100, 1000], ['002', 'b', 2, 20, 200, 2000]], columns=['id', 'name', 'c1', 'c2', 'c2', 'c3'], index=list('AB'))
df = df.set_index(['id', 'name'])
df = df.groupby(by=df.columns, axis=1).mean()
df = df.reset_index()

df
