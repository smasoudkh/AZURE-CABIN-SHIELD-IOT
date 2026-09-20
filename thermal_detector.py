import pandas as pd
import numpy as np
import time

def detect_thermal_runaway(sensor_stream):
    CRITICAL_TEMP_CELSIUS = 65.0      
    CRITICAL_RISE_RATE_PER_SEC = 2.0  
    
    df = pd.DataFrame(sensor_stream)
    df['Temp_Change'] = df['Temperature_C'].diff().fillna(0)
    df['Time_Change'] = df['Timestamp_Sec'].diff().fillna(1)
    df['Temp_Rise_Rate'] = df['Temp_Change'] / df['Time_Change']
    
    return df

cabin_bin_12c = {
    'Timestamp_Sec': [0, 5, 10, 15, 20, 25, 30, 35, 40],
    'Temperature_C': [22.1, 22.4, 22.5, 24.1, 35.2, 51.0, 68.5, 85.0, 110.2]
}

print("=== Azure Cabin Shield IoT ===")
live_stream = detect_thermal_runaway(cabin_bin_12c)

for idx, row in live_stream.iterrows():
    time.sleep(0.1)
    print(f"[Time: {int(row['Timestamp_Sec'])}s] | Temp: {row['Temperature_C']}°C | Rate: {row['Temp_Rise_Rate']:.2f}°C/s")
    if row['Temp_Rise_Rate'] >= 2.0 or row['Temperature_C'] >= 65.0:
        print(" 🚨🚨 [CRITICAL EDGE TRIGGER] Thermal Runaway Detected in Bin 12C!")
        print(" -> Action: Dispatching emergency notification to Purser E-Tablet and Schiphol AOC.")
