import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Filter the data
df = df[(df['LocationAbbr'] == 'US') & 
        (df['Indicator'].isin(["Adults aged 65+ who have lost all of their natural teeth due to tooth decay or gum disease", 
                              "Adults aged 65+ who have lost six or more teeth due to tooth decay or gum disease"])) &
        (df['Break_Out'].isin(["White", "Hispanic", "Black"])) &
        (df['Response'] == 'Yes') &
        (df['LocationID'] == 'US') &
        (df['Data_Value_Type'] == 'Crude Prevalence')]

# Sort the data
df = df.sort_values('Year')

# Save the filtered data to a new CSV file
df.to_csv('new.csv', index=False)

# Plot the data
fig, ax = plt.subplots()

for (indicator, race), group in df.groupby(['Indicator', 'Break_Out']):
    if indicator == "Adults aged 65+ who have lost all of their natural teeth due to tooth decay or gum disease":
        if race == "White":
            ax.plot(group['Year'], group['Data_Value'], label=f'lost all - {race}', linestyle='-', linewidth=2, color='black')
        elif race == "Hispanic":
            ax.plot(group['Year'], group['Data_Value'], label=f'lost all - {race}', linestyle=':', linewidth=2, color='black')
        elif race == "Black":
            ax.plot(group['Year'], group['Data_Value'], label=f'lost all - {race}', linestyle='-.', linewidth=2, color='black')
    else:
        if race == "White":
            ax.plot(group['Year'], group['Data_Value'], label=f'lost six or more - {race}', linestyle='-', linewidth=1, color='black')
        elif race == "Hispanic":
            ax.plot(group['Year'], group['Data_Value'], label=f'lost six or more - {race}', linestyle=':', linewidth=1, color='black')
        elif race == "Black":
            ax.plot(group['Year'], group['Data_Value'], label=f'lost six or more - {race}', linestyle='-.', linewidth=1, color='black')

plt.xlabel('Year')
plt.ylabel('Percent')
plt.title('Lost Teeth by race')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.3))
#ax.legend(loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('race.png',dpi=300)
plt.show()

