import pandas as pd
import numpy as np

component_metrics = {
    'Serial_Key': ['S01', 'S02', 'S03', 'S04', 'S05'],
    'Heat_Delta_K': [1.4, np.nan, 0.9, 4.2, np.nan],
    'Status_Code': ['Valid', 'Review', 'Valid', 'Review', 'Valid']
}

df = pd.DataFrame(component_metrics)
print(df)

df['Heat_Delta_K'] = df['Heat_Delta_K'].fillna(0.5)
df = df.rename(columns={'Heat_Delta_K': 'Thermal_Variance'})
df.to_csv("calibrated_metrics.csv", index=False)
print(df)
