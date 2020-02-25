# 1.Replacing dashes and NAs
for col in objcols:
    data[col] = data[col].replace('-', 0)
#     data[col] = data[col].replace('NA', 0)

#2. Remove comma from numeric
for col in sales_cols:
    data[col] = data[col].str.replace(',',"").astype(float)
    
#3. Replacing percentage suffix
for col in objcols:
    data[col] = (pd.to_numeric(data[col].str[:-1]).div(100).mask(data[col] == '%', 0))
    
#4. Replacing Nans with zeros
for col in objcols:
    data[col] = data[col].replace(np.nan, 0)
    
#5. Missing Values 
    def missing_values(data):
    
    # getting the sum of null values and ordering
    total = data.isnull().sum().sort_values(ascending = False) 
    
    #getting the percent and order of null
    percent = (data.isnull().sum() / data.isnull().count() * 100 ).sort_values(ascending = False) 
    
    # Concatenating the total and percent
    df = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) 
    print("Total columns with at least one NULL Values: ")
    
    # Returning values of nulls different of 0
    print (df[~(df['Total'] == 0)]) 
    
    return df

#6. Get columns with specific string
def get_cols(string_list, data):
    cols_all = []
    for string in string_list:
        cols = [col for col in data.columns if string in col]
        print(cols)
        cols_all.extend(cols)
    return(cols)

#7. Categorise Data
def create_groups(row):
    if row in [0,1,2,3,4]:
        return "Low"
    elif row in [5,6,7]:
        return "Med"
    elif row in [8,9,10]:
        return "High"
    else:
        return "others"
    
#8. Create empty Dataset
def df_empty(columns, dtypes, index=None):
    assert len(columns)==len(dtypes)
    df = pd.DataFrame(index=index)
    for c,d in zip(columns, dtypes):
        df[c] = pd.Series(dtype=d)
    return df

