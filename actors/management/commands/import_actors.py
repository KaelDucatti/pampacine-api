from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str, help="Actors file name")

    def handle(self, *args, **options):
        file_name = options["file_name"]
        print(f"file name: {file_name}")
