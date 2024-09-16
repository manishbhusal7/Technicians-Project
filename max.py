# I have worked in a conda environment named max so I will activate it first and install required dependencies like pandas

import pandas as pd

df_repair_types = pd.read_csv('repair_types.csv', encoding='UTF-8-SIG')
df_upcoming_repairs = pd.read_csv('upcoming_repairs.csv', encoding='UTF-8-SIG')

df_merged = pd.merge(df_upcoming_repairs, df_repair_types, on='repair_name')

df_merged['calculated_value'] = df_merged['repair_value'] * df_merged['severity']

# Sort the dataframe by calculated_value per minute in descending order
df_merged['value_per_minute'] = df_merged['calculated_value'] / df_merged['time_in_minutes']
df_sorted = df_merged.sort_values('value_per_minute', ascending=False)

# Calculating the number of minutes in 2 weeks
two_weeks_minutes = 2 * 7 * 24 * 60

# Initialize variables
total_value = 0
total_time = 0
repairs_completed = []

# Iterate through the sorted repairs
for _, repair in df_sorted.iterrows():
    if total_time + repair['time_in_minutes'] <= two_weeks_minutes:
        total_time += repair['time_in_minutes']
        total_value += repair['calculated_value']
        repairs_completed.append(repair['repair_name'])

print(f"Maximum value provided over 2 weeks: {total_value:.2f}")
print(f"Number of repairs completed: {len(repairs_completed)}")
print("Top 10 repairs completed:")
for repair in repairs_completed[:10]:
    print(f"- {repair}")
print(f"Total time used: {total_time} minutes out of {two_weeks_minutes} minutes")



## Qn 2 

# Find the repair ID for 'Earth Switch Maintenance and Repair'
earth_switch_repair_id = df_repair_types[df_repair_types['repair_name'] == 'Earth Switch Maintenance and Repair']['repair_id'].values[0]

print(f"Repair ID for 'Earth Switch Maintenance and Repair': {earth_switch_repair_id}")