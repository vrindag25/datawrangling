# List of variables to be removed from analysis
xvar_rm = [ID]

#Remove columns with unknown and others
xvar_rm.extend([col for col in df.columns if(('unknown' in col) or ('others' in col) or 
                              ('None' in col) or ('unkown' in col) )])#or (col == 'age_lessthan65')

# df = df.set_index(ID)
df=df.drop(xvar_rm,axis=1)

## Step 1:
Remove rows based on condition

## Step 2:
Remove variables based on the proportion of data available

#Get sum of all null values
print(df.isnull().values.any())
print(df.isna().values.any())

#Proportion of zeroes column wise in data
df_col_zero = pd.DataFrame(df[df == 0].count(axis=0)/len(df.index)).reset_index().sort_values(by = 0, ascending = False)
print(df_col_zero)

#Remove 
x_vars_rm = df_col_zero[df_col_zero[0] >0.80]['index']
len(x_vars_rm)

# df.select_dtypes('object')

# Remove columns with zero values more than 98%
df = df.drop(columns = x_vars_rm)

# Step 3
Remove columns if variance within a column is very low

df_col_mean = pd.DataFrame(df.mean(axis = 0)).reset_index().sort_values(by = 0)
df_col_mean[0] = df_col_mean[0]*100

df_col_var = pd.DataFrame(df.var(axis = 0)).reset_index().sort_values(by = 0)
df_col_var[0] = sqrt(df_col_var[0])*100

df_col_mean.merge(df_col_var, how='inner', on='index', suffixes=('_mean', '_sd'))

## Step 4:
Remove rows based on correlation (Y with X cohort)

# Compute the correlation matrix
df_corr = df.corr().reset_index()
df_corr = df_corr.melt(id_vars=["index"], var_name="features", value_name="corr_value").sort_values(by = 'corr_value')
df_corr[((df_corr.corr_value>0.70) | (df_corr.corr_value<-0.70)) & (df_corr.corr_value!=1.0)]


# Compute the correlation matrix
df_corr = df.corr().reset_index()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(df_corr, dtype=np.bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
