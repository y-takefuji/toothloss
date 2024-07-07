import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Filter the data for the first indicator and 'Male'
df1 = df[(df['LocationAbbr'] == 'US') & 
         (df['Indicator'] == 'Adults aged 65+ who have lost all of their natural teeth due to tooth decay or gum disease') &
         (df['Response'] == 'Yes') &
         (df['LocationID'] == 'US') &
         (df['Break_Out'] == 'Male') &
         (df['Data_Value_Type'] == 'Crude Prevalence')]

# Filter the data for the second indicator and 'Male'
df2 = df[(df['LocationAbbr'] == 'US') & 
         (df['Indicator'] == 'Adults aged 65+ who have lost six or more teeth due to tooth decay or gum disease') &
         (df['Response'] == 'Yes') &
         (df['LocationID'] == 'US') &
         (df['Break_Out'] == 'Male') &
         (df['Data_Value_Type'] == 'Crude Prevalence')]

# Filter the data for the first indicator and 'Female'
df3 = df[(df['LocationAbbr'] == 'US') & 
         (df['Indicator'] == 'Adults aged 65+ who have lost all of their natural teeth due to tooth decay or gum disease') &
         (df['Response'] == 'Yes') &
         (df['LocationID'] == 'US') &
         (df['Break_Out'] == 'Female') &
         (df['Data_Value_Type'] == 'Crude Prevalence')]

# Filter the data for the second indicator and 'Female'
df4 = df[(df['LocationAbbr'] == 'US') & 
         (df['Indicator'] == 'Adults aged 65+ who have lost six or more teeth due to tooth decay or gum disease') &
         (df['Response'] == 'Yes') &
         (df['LocationID'] == 'US') &
         (df['Break_Out'] == 'Female') &
         (df['Data_Value_Type'] == 'Crude Prevalence')]

# Sort the data by 'Year'
df1 = df1.sort_values('Year')
df2 = df2.sort_values('Year')
df3 = df3.sort_values('Year')
df4 = df4.sort_values('Year')

# Combine the filtered data and save to a new CSV file
df_combined = pd.concat([df1, df2, df3, df4])
df_combined.to_csv('new.csv', index=False)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df1['Year'], df1['Data_Value'], color='black', linestyle='solid', label='lost all, Male')
plt.plot(df2['Year'], df2['Data_Value'], color='black', linestyle='dotted', label='lost six or more, Male')
plt.plot(df3['Year'], df3['Data_Value'], color='black', linestyle='dashed', label='lost all, Female')
plt.plot(df4['Year'], df4['Data_Value'], color='black', linestyle='dashdot', label='lost six or more, Female')

# Rotate x-axis labels
plt.xticks(rotation=90)

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Percent')
plt.title('Lost Teeth by sex')

# Show the legend in the graph
plt.legend()

# Show the plot
plt.savefig('teethsex.jpg',dpi=300)
plt.show()
