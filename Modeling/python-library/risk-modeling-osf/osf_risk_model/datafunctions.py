#
# datafunctions.py
#
# Functions responsible for data preparation for ML/DL/NN feature creation
#
import pandas as pd
import numpy as np

def clean_json_to_dataset(source_json_file='osf_risk_model/data/sample-training-modeling-data.json'):
        #
        # load the dataset, split into input (X) and output (y) variables
        #
        with open(source_json_file, encoding='utf-8') as inputfile:
            df = pd.read_json(source_json_file, lines=True)
        # Fill Nulls
        df.fillna(0, inplace=True)
        # drop columns what are not numeric
        print("before drop DF")
        print(df.describe())
        drop_list = ['job_run_timestamp','address_line_1','address_line_2','address_line_3','address_line_4','address_line_5','address_line_6','ber_rating','model_river','model_coastal','model_sw','unflood_heightband','floodability_index_ud','floodability_index_def','product','Disbursment_Date','Closing_Date', 'location'] #'address_line_7','address_line_8','address_line_9' #'Completion_Date'] #,'Next_Payment_Due']
        df.drop(columns=drop_list)
        # Ugly force clean-up with positions because by name index doesn't work
        del df[df.columns[0]]
        del df[df.columns[2]]
        del df[df.columns[2]]
        del df[df.columns[2]]
        del df[df.columns[2]]
        del df[df.columns[2]]
        del df[df.columns[4]]
        del df[df.columns[22]]
        del df[df.columns[22]]
        del df[df.columns[22]]
        del df[df.columns[41]]
        del df[df.columns[41]]
        del df[df.columns[41]]
        del df[df.columns[42]]
        del df[df.columns[44]]
        del df[df.columns[44]]
        del df[df.columns[53]]
        del df[df.columns[53]]
        #
        # Re-Order Variables
        df1 = df[df.columns[0:40]]
        df2 = df[df.columns[41:52]]
        df=df.iloc[:,[41,42,43,44,45,46,47,48,49,50,51,52,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,3,38,39,40]]
        #
        print("DF after drops cols")
        print(df.describe())
        source_csv_file="osf_risk_model/data/sample-training-modeling-data.csv"
        df.to_csv(source_csv_file, encoding='utf-8', index=False, header=None)
        #
        dataset = np.loadtxt(source_csv_file, delimiter=',')
        #
        return dataset