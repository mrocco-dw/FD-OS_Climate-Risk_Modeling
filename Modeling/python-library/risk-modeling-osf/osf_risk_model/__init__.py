
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from osf_risk_model.floodabilitydataclassifier import FloodabilityDataClassifier

class OsfRiskTrainingClass:
    
    def __init__(self):
        self._x = None
    
    def set_x(self, x):
        self._x = x
    
    def get_x(self):
        return self._x
    
    def model_loanbook_asset(source_json_file='osf_risk_model/data/sample-training-modeling-data.json'):
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
        print("DF after drops cols")
        print(df.describe())
        source_csv_file="osf_risk_model/data/sample-training-modeling-data.csv"
        df.to_csv(source_csv_file, encoding='utf-8', index=False, header=None)

        dataset = np.loadtxt(source_csv_file, delimiter=',')
        X = dataset[:,0:8]
        y = dataset[:,8]
        # create tensor out of Numpy arrays
        X = torch.tensor(X, dtype=torch.float32)
        y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
        #
        # Define Model Neural Networks
        model = FloodabilityDataClassifier()
        print(model)
        #
        # train the model
        loss_fn   = nn.BCELoss()  # binary cross entropy
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        n_epochs = 100
        batch_size = 10
        #
        # Training model based on load assets
        n_epochs = 100
        batch_size = 10
        for epoch in range(n_epochs):
            for i in range(0, len(X), batch_size):
                Xbatch = X[i:i+batch_size]
                y_pred = model(Xbatch)
                ybatch = y[i:i+batch_size]
                loss = loss_fn(y_pred, ybatch)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()    
            print(f'Finished epoch {epoch}, latest loss {loss}')
        #
        # Evaluate the model
        # compute accuracy
        y_pred = model(X)
        accuracy = (y_pred.round() == y).float().mean()
        print(f"Accuracy {accuracy}")
        #
        # Predictions
        # make probability predictions with the model
        predictions = model(X)
        for i in range(5):
            print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
        # round predictions
        rounded = predictions.round()
        # make class predictions with the model as 0 or 1
        predictions = (model(X) > 0.5).int()
        for i in range(25):
            print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
        # done
        print("experimentation done!")
        #
        return 0
