from django.core.management.base import BaseCommand, CommandError

import sqlite3


class LoadUSDA(BaseCommand):
    help = "Loads items from USDA sqlite database."

    def add_arguments(self, parser):
        parser.add_argument('db_file', type=str, required=True)


    def handle(self, *args, **options):
        conn = sqlite3.connect(options['db_file'])
        c = conn.cursor()
        for row in c.execute('SELECT * FROM food_des'):
            print(row)
        conn.close()
