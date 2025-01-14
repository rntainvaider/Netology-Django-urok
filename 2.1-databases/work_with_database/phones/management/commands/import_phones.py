import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv", "r") as file:
            phones = list(csv.DictReader(file, delimiter=";"))
            for row in phones:
                phone = Phone(
                    id=row["id"],
                    name=row["name"],
                    image=row["image"],
                    price=row["price"],
                    release_date=row["release_date"],
                    lte_exists=row["lte_exists"].lower() == "true",
                )
                phone.save()
        self.stdout.write(self.style.SUCCESS("Импорт телефонов завершён!"))
