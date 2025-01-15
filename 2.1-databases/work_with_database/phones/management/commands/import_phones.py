import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    help = "Импорт телефонов из CSV"

    def handle(self, *args, **options):
        with open("phones.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
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
