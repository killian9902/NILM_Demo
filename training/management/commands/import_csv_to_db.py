import pandas as pd
from django.core.management.base import BaseCommand
from training.models import Appliance, MeterReading 

class Command(BaseCommand):
    help = 'Import meter readings from CSV file to Django DB'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')
        

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']

        df = pd.read_csv(csv_file_path, dtype={'DateTime': 'object'})
        
        # Now convert the 'datetime' column to datetime format, addressing the format directly
        df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y-%m-%d %H:%M:%S')

        for _, row in df.iterrows():
            appliance_name = row['Name']
            datetime = row['DateTime']
            Wh = row['Wh']

            appliance, _ = Appliance.objects.get_or_create(name=appliance_name)
            MeterReading.objects.create(appliance=appliance, datetime=datetime, Wh=Wh)

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {appliance_name} reading'))