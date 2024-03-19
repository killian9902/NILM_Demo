import pandas as pd
from django.core.management.base import BaseCommand
from testing.models import Feature


# Command: py manage.py import_features PATH/labels.csv

class Command(BaseCommand):
    help = 'Imports data from AI Features in CSV into the DB'


    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')


    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']

        features_df = pd.read_csv(csv_file_path)
        features = [
            Feature(
                feature1=row[0],
                feature2=row[1],
                feature3=row[2],
                feature4=row[3],
                feature5=row[4],
                feature6=row[5],
                feature7=row[6],
                feature8=row[7],
                feature9=row[8],
                feature10=row[9],
                feature11=row[10],
                feature12=row[11],
                feature13=row[12],
                feature14=row[13],
                feature15=row[14],
                feature16=row[15],
                feature17=row[16],
                feature18=row[17],
                feature19=row[18],
                feature20=row[19],
                feature21=row[20],
                feature22=row[21],
                feature23=row[22],
                feature24=row[23],
                feature25=row[24],
            )
            for index, row in features_df.iterrows()
        ]

        Feature.objects.bulk_create(features)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported features from "{csv_file_path}"'))
        print(features_df.head())


