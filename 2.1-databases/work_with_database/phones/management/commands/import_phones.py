import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Импорт телефонов из CSV"

    def handle(self, *args, **options):
        with open("phones.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone, created = Phone.objects.get_or_create(
                    id=row["id"],
                    defaults={
                        "name": row["name"],
                        "price": row["price"],
                        "image": row["image"],
                        "release_date": row["release_date"],
                        "lte_exists": row["lte_exists"].lower() == "true",
                        "slug": slugify(row["name"]),
                    },
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Телефон {phone.name} добавлен")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Телефон {phone.name} уже существует")
                    )
