from django.core.management import BaseCommand

from coffee_shop.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Create product")
        import random

        coffee_names = ["Капучино", "Эспрессо", "Американо", "Мокка", "Флэт Уайт", "Раф", "Макиато", "Лунго",
                        "Аффогато"]

        coffee_categories = ["goods", "drinks", "hot", "iced"]

        coffee_images = ["coffee1.jpg", "coffee2.jpg", "coffee3.jpg", "coffee4.jpg", "coffee5.jpg", "coffee6.jpg",
                         "coffee7.jpg", "coffee8.jpg", "coffee9.jpg", "coffee10.jpg"]

        coffee_descriptions = [
            "Классический напиток с молоком",
            "Крепкий эспрессо",
            "Кофе с водой",
            "Кофе с шоколадом",
            "Кофе с молоком и тонкой пенкой",
            "Кофе с молоком и ванильным сиропом",
            "Кофе с добавлением вспененого молока",
            "Длинный кофе",
            "Шарлотка с кофейным ароматом"
        ]

        for _ in range(9):
            coffee_name = random.choice(coffee_names)
            coffee_category = random.choice(coffee_categories)
            coffee_image = random.choice(coffee_images)
            coffee_description = random.choice(coffee_descriptions)
            coffee_price = random.randint(500, 1500)
            coffee_discount = random.randint(50, 200)
            coffee_archived = False

            product, created = Product.objects.get_or_create(
                name=coffee_name,
                category=coffee_category,
                image=coffee_image,
                description=coffee_description,
                price=coffee_price,
                discount=coffee_discount,
                archived=coffee_archived
            )
            self.stdout.write(f"{product}")
        self.stdout.write(self.style.SUCCESS("Products created"))
