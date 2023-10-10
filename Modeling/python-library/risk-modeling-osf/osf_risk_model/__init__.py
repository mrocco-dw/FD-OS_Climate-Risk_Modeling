
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from osf_risk_model.floodabilitydataclassifier import FloodabilityDataClassifier
from osf_risk_model.datafunctions import clean_json_to_dataset

class OsfRiskTrainingClass:
    
    def __init__(self):
        self._x = None
    
    def set_x(self, x):
        self._x = x
    
    def get_x(self):
        return self._x
        
    def model_nn_floodability_loanbook_assets(source_json_file='osf_risk_model/data/sample-training-modeling-data.json'):
        #
        dataset = clean_json_to_dataset(source_json_file)
        # 53 columns
        X = dataset[:,0:52]
        y = dataset[:,50]  # var to predict y = floodscore_ud
        # y = dataset[:,52]  # var to predict y = unflood_value
        #
        # create tensor out of Numpy arrays
        X = torch.tensor(X, dtype=torch.float32) 
        y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1) # OVERFITING ALL DATAPOINTS # 25536
        #
        # Define Model Neural Networks
        model = FloodabilityDataClassifier()
        print(model)
        #
        # train the model
        loss_fn   = nn.BCELoss()  # binary cross entropy
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        #
        # Training model based on load assets
        n_epochs = 101
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
        # Prediction
        # make probability predictions with the mode
        print("- Predictions")
        print("-- make probability predictions with the model")
        predictions = model(X)
        for i in range(25):
            print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
        print("- Class predictions rounded ")
        rounded = predictions.round()
        # round
        # make class predictions with the model as 0 or 1
        print("-- round")
        print("-- make class predictions with the model as 0 or 1")
        #
        predictions = (model(X) > 0.5).int()
        for i in range(25):
            print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
        # done
        print("OSF Risk Model, experimentation done!")
        #
        return 0
