from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from .models import MeterReading
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404
from .models import MeterReading, Appliance
from datetime import datetime



def trainingindex(request):
    template_name = 'training/trainingindex.html'
    return render(request, template_name)



def create(request):
    if request.method == 'POST':


        start_datetime_str = request.POST.get('start_date')
        end_datetime_str = request.POST.get('end_date')


        start_datetime = parse_datetime(start_datetime_str)
        end_datetime = parse_datetime(end_datetime_str)

        print(start_datetime, end_datetime)

        mains_appliance = get_object_or_404(Appliance, name='Mains')


        request.session['start_date'] = start_datetime.strftime('%Y-%m-%dT%H:%M:%S')
        request.session['end_date'] = end_datetime.strftime('%Y-%m-%dT%H:%M:%S')
        
        readings = MeterReading.objects.filter(
                datetime__gte=start_datetime,
                datetime__lte=end_datetime,
                appliance = mains_appliance
            )
        

        graph_data = [
                {'time': reading.datetime.strftime('%Y-%m-%dT%H:%M:%S'), 'value': reading.Wh}
                for reading in readings
            ]
        


        response_data = {
            'message': 'Thank you! Your submission has been received!',
            'graph_data': graph_data
        }

        
        return JsonResponse(response_data, encoder=DjangoJSONEncoder)
        



def appliance(request):
    if request.method == 'POST':
        print(request.POST)
        
        


        appliance_str = request.POST.get('appliance')

        start_date_str = request.session.get('start_date')
        end_date_str = request.session.get('end_date')

        start_date = datetime.fromisoformat(start_date_str)
        end_date = datetime.fromisoformat(end_date_str)

        
        appliance = get_object_or_404(Appliance, name=appliance_str)




        print(appliance, type(start_date), type(end_date))

        readings = MeterReading.objects.filter(
                datetime__gte=start_date,
                datetime__lte=end_date,
                appliance = appliance
            )

        graph_data = [
                {'time': reading.datetime.strftime('%Y-%m-%dT%H:%M:%S'), 'value': reading.Wh}
                for reading in readings
            ]

        response_data = {
            'message': 'Thank you! Your submission has been received!',
            'graph_data': graph_data
        }

        
        return JsonResponse(response_data, encoder=DjangoJSONEncoder)
    

 
            
        




        

        

