import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import subprocess as sp
import warnings
warnings.filterwarnings('ignore')
import os
import subprocess as sp

# Check if 'results.csv' exists in the directory
if not os.path.exists('results.csv'):
    # If 'results.csv' does not exist, download the parts
    sp.call('wget -nc https://github.com/y-takefuji/water/raw/main/results.csv_part0', shell=True)
    sp.call('wget -nc https://github.com/y-takefuji/water/raw/main/results.csv_part1', shell=True)
    sp.call('wget -nc https://github.com/y-takefuji/water/raw/main/results.csv_part2', shell=True)
    sp.call('wget -nc https://github.com/y-takefuji/water/raw/main/results.csv_part3', shell=True)
    sp.call('wget -nc https://github.com/y-takefuji/water/raw/main/results.csv_part4', shell=True)

    # Concatenate the parts
    def concatenate_files(filename, num_parts):    
        with open(f'{filename}', 'wb') as outfile:        
            for i in range(num_parts):            
                with open(f'{filename}_part{i}', 'rb') as infile:                
                    outfile.write(infile.read())
    concatenate_files('results.csv', 5)

# Load the data
df = pd.read_csv('results.csv', encoding='ISO-8859-1')

# Replace 'NULL' with NaN
df = df.replace('NULL', np.nan)

# Filter the data
df = df[df['Medium'] == 'Water']
df['Activity_Start_Date'] = pd.to_datetime(df['Activity_Start_Date'])

# Convert 'Result_Text' to numeric and handle errors
df['Result_Text'] = pd.to_numeric(df['Result_Text'], errors='coerce')

# Drop rows with NaN values in 'Result_Text'
df = df.dropna(subset=['Result_Text'])

# User selects location
print("Select a location by number:")
locations = df['Location_ID'].unique()
for i, loc in enumerate(locations):
    print(f"{i+1}. {loc}")
location_id = locations[int(input()) - 1]
df = df[df['Location_ID'] == location_id]

# User selects characteristics
characteristics = df['Characteristic_Name'].unique()
print("Select up to 2 characteristics by number:")
for i, char in enumerate(characteristics):
    print(f"{i+1}. {char}")
selected_chars = [characteristics[int(i)-1] for i in input().split()[:2]]

# Filter the DataFrame based on the selected characteristics
filtered_df = df[df['Characteristic_Name'].isin(selected_chars)]

# Save the filtered DataFrame to a CSV file
filtered_df.to_csv(location_id + '_used_variables_results.csv', index=False)

# Prepare the plot
fig, ax1 = plt.subplots()

# Line styles and widths
linestyles = ['-', '--', '-.', ':']
linewidths = [1, 2]

# Plot the data
for i, char in enumerate(selected_chars):
    char_df = df[df['Characteristic_Name'] == char]
    monthly_avg = char_df.groupby(char_df['Activity_Start_Date'].dt.month)['Result_Text'].mean()
    char_df['month'] = char_df['Activity_Start_Date'].dt.month
    char_df['anomaly'] = np.abs(char_df['Result_Text'] - char_df['month'].map(monthly_avg)) > 2 * char_df['Result_Text'].std()
    if i == 0:
        ax1.plot(char_df['Activity_Start_Date'], char_df['Result_Text'], label=char, linestyle=linestyles[i%4], linewidth=linewidths[i%2], color='black')
        ax1.scatter(char_df[char_df['anomaly']]['Activity_Start_Date'], char_df[char_df['anomaly']]['Result_Text'], color='red')
        ax1.set_ylabel(location_id + ' for ' + char, color='black')
    else:
        ax2 = ax1.twinx()
        ax2.plot(char_df['Activity_Start_Date'], char_df['Result_Text'], label=char, linestyle=linestyles[i%4], linewidth=linewidths[i%2], color='blue')
        ax2.scatter(char_df[char_df['anomaly']]['Activity_Start_Date'], char_df[char_df['anomaly']]['Result_Text'], color='red')
        ax2.set_ylabel(location_id + ' for ' + char, color='blue')

# Format the x-axis
date_form = DateFormatter("%Y/%m/%d")
ax1.xaxis.set_major_formatter(date_form)

# Set labels and title
ax1.set_xlabel('Activity_Start_Date')
ax1.set_title('Water Quality Over Time')
fig.legend()

def main():
# Show the plot
 plt.xticks(rotation=90)
 plt.tight_layout()
 plt.savefig(location_id + '_result.png',dpi=300)
 plt.show()

if __name__ == "__main__":
 main()
