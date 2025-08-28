import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from actors.models import Actor


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str, help="Actors file name")

    def handle(self, *args, **options):
        file_name = options["file_name"]
        print(f"file name: {file_name}")

        with open("actors.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                first_name = row["first_name"]
                last_name = row["last_name"]
                birthday = datetime.strptime(
                    row["birthday"], "%Y-%m-%d"
                ).date()
                nationality = row["nationality"]

                Actor.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    birthday=birthday,
                    nationality=nationality,
                )
        self.stdout.write(self.style.SUCCESS("Atores importados com sucesso!"))
