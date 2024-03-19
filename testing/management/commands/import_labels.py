import pandas as pd
from django.core.management.base import BaseCommand
from testing.models import Label, Feature


# Command: py manage.py import_labels PATH/labels.csv

class Command(BaseCommand):
    help = 'Imports data from AI Labels in CSV into the DB'


    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')


    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']

        labels_df = pd.read_csv(csv_file_path)



        labels = []
        for index, row in labels_df.iterrows():
            feature_instance = Feature.objects.get(id=index+1)  
            labels.append(Label(
                feature=feature_instance,
                label1=row[0], 
                label2=row[1],
                label3=row[2], 
                label4=row[3],
                label5=row[4], 
                label6=row[5],
            ))

        Label.objects.bulk_create(labels)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported features from "{csv_file_path}"'))
        print(labels_df.head())
