from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import Feature, Label
import random
from django.core.serializers import serialize
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import torch.nn.functional as F

from testing.NN import MLP, RMSE




def testingindex(request):
    template_name = 'testing/testingindex.html'
    return render(request, template_name)






def AI(request):
    if request.method =='POST':
        

        no_samples = 16

        all_IDs = list(Feature.objects.values_list('id', flat=True))
        random_IDs = random.sample(all_IDs, no_samples)

        Features = Feature.objects.filter(id__in=random_IDs)
        Labels = Label.objects.filter(feature__in=random_IDs)


       
        feature_list = []
        for i in range(no_samples):
            temp_list = []
            record = Features[i]
            
            temp_list.append(record.feature1)
            temp_list.append(record.feature2)
            temp_list.append(record.feature3)
            temp_list.append(record.feature4)
            temp_list.append(record.feature5)
            temp_list.append(record.feature6)
            temp_list.append(record.feature7)
            temp_list.append(record.feature8)
            temp_list.append(record.feature9)
            temp_list.append(record.feature10)
            temp_list.append(record.feature11)
            temp_list.append(record.feature12)
            temp_list.append(record.feature13)
            temp_list.append(record.feature14)
            temp_list.append(record.feature15)
            temp_list.append(record.feature16)
            temp_list.append(record.feature17)
            temp_list.append(record.feature18)
            temp_list.append(record.feature19)
            temp_list.append(record.feature20)
            temp_list.append(record.feature21)
            temp_list.append(record.feature22)
            temp_list.append(record.feature23)
            temp_list.append(record.feature24)
            temp_list.append(record.feature25)

            feature_list.append(temp_list)



        label_list = []
        for i in range(no_samples):
            temp_list = []
            record = Labels[i]
            
            temp_list.append(record.label1)
            temp_list.append(record.label2)
            temp_list.append(record.label3)
            temp_list.append(record.label4)
            temp_list.append(record.label5)
            temp_list.append(record.label6)

            label_list.append(temp_list)

        




        # Load AI model
        model = torch.jit.load('MLP_2.pt')
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model.to(device)
        model.eval()
        model.double()
        loss_function=RMSE()
        total_test_loss = 0
        


        input = torch.tensor(feature_list).double()
        target = torch.tensor(label_list).double()
        

        
        with torch.no_grad():
            data, targets = input.to(device), target.to(device)

            outputs = model(data)
            loss = loss_function(outputs, targets)
            total_test_loss += loss.item()



        
        target_export = []
        result_export = []

        for i in range(len(data)):
            target_export.append(targets[i].numpy().tolist())
            result_export.append(outputs[i].numpy().tolist())

        formatted_targets = [[round(float(num), 2) for num in sublist] for sublist in target_export]
        formatted_results = [[round(float(num), 2) for num in sublist] for sublist in result_export]
        formatted_loss = round(total_test_loss, 2)
        



        response_data = {
            'target': formatted_targets,
            'result': formatted_results,
            'loss': formatted_loss,
        }

        
        
        return JsonResponse(response_data, encoder=DjangoJSONEncoder)
    









