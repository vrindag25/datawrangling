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
