import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, input_size=25, output_size=6, dropout_rate=0.1):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.ln1 = nn.LayerNorm(128)
        self.dropout1 = nn.Dropout(dropout_rate)

        
        self.fc2 = nn.Linear(128, 64)
        self.ln2 = nn.LayerNorm(64)
        self.dropout2 = nn.Dropout(dropout_rate)

        
        self.fc3 = nn.Linear(64, output_size)

        self.init_weights()

    

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight, nonlinearity='leaky_relu')
                nn.init.constant_(m.bias, 0)


    
    def forward(self, x):
        x = self.fc1(x)
        x = F.leaky_relu(self.ln1(x), negative_slope=0.05)
        x = self.dropout1(x)

        x = self.fc2(x)
        x = F.leaky_relu(self.ln2(x), negative_slope=0.05)
        x = self.dropout2(x)
        
        x = self.fc3(x)
        return x
    

class RMSE(nn.Module):
    def __init__(self, eps=1e-6):
        super().__init__()
        self.mse = nn.MSELoss()
        self.eps = eps
        
    def forward(self,yhat,y):
        loss = torch.sqrt(self.mse(yhat,y) + self.eps)
        return loss