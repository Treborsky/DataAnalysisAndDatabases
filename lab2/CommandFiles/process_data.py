import pandas as pd
import numpy as np
from numpy.core.fromnumeric import shape
import os
import glob

# clean output directory
files = glob.glob('../AnalysisData/*')
for f in files:
    os.remove(f)

original_data = pd.read_csv('../OriginalData/earthquake_data.csv')
# original_data.info() # DEBUG

old_column_names = list(original_data.columns)
new_column_names = np.array([
    'WorryLevel',
    'BigOneWorryLevel',
    'BigOneInLifetimePred',
    'EverExperiencedEarthquake',
    'BigOnePrecautions',
    'SanAndreasFaultLineFamiliarity',
    'YellowstoneSupervolcanoFamiliarity',
    'AgeRange',
    'Gender',
    'TotalHouseholdLastYearEarnings',
    'UsRegion',
])

column_names_dict = {old_column_names[i] : new_column_names[i] for i in range(len(old_column_names))}

renamed_data = original_data.rename(columns=column_names_dict)
# print(renamed_data.head(), '\n\n', renamed_data.tail()) # DEBUG

selected_columns = ['Gender', 'AgeRange', 'BigOneInLifetimePred']

selected_data = renamed_data[selected_columns]
print(selected_data)

selected_data.to_csv('../AnalysisData/selected_earthquake_data.csv', index=False)
