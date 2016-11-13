from django.core.management.base import BaseCommand, CommandError

import sqlite3

from nutrition.models import Edible, Nutrient, WeightMeasure, NutrientContent


class Command(BaseCommand):
    help = "Loads items from USDA sqlite database."

    def add_arguments(self, parser):
        parser.add_argument('db_file', type=str)


    def handle(self, *args, **options):
        conn = sqlite3.connect(options['db_file'])
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # load nutrients
        for row in c.execute('SELECT * FROM nutr_def'):
            n = Nutrient(
                id=row['Nutr_No'],
                name=row['NutrDesc'],
                description=row['Tagname'],
                unit=row['Units']
            )
            n.save()

        # load edibles
        for row in c.execute('SELECT * FROM food_des'):
            e = Edible(
                id=row['NDB_no'],
                name=row['Long_Desc'],
                description=row['Shrt_Desc'],
            )
            e.save()

        # load weight
        for row in c.execute('SELECT * FROM weight'):
            w = WeightMeasure(
                amount=row['Amount'],
                description=row['Msre_Desc'],
                weight=row['Gm_Wgt'],
            )
            w.edible_id = row['NDB_No']
            w.save()

        # load nut_data
        for row in c.execute('SELECT * FROM nut_data'):
            nc = NutrientContent(
                content=row['Nutr_val'],
            )
            nc.edible_id = row['NDB_No']
            nc.nutrient_id = row['Nutr_No']
            nc.save()

        conn.close()
