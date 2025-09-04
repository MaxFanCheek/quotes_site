from django.core.management.base import BaseCommand
from quotes.models import Source, Quote


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаём источники
        sources_data = [
            "The Lord of the Rings", "Fight Club", "Alice in Wonderland",
            "Pulp Fiction", "1984", "Forrest Gump", "Harry Potter"
        ]

        sources = {}
        for title in sources_data:
            src, created = Source.objects.get_or_create(title=title)
            sources[title] = src

        # Добавляем цитаты
        quotes_data = [
            ("Even the smallest person can change the course of the future.", "The Lord of the Rings", 2),
            ("The things you own end up owning you.", "Fight Club", 2),
            ("We're all mad here.", "Alice in Wonderland", 2),
            ("Say 'what' again. I dare you!", "Pulp Fiction", 2),
            ("Big Brother is Watching You.", "1984", 2),
            ("Life is like a box of chocolates.", "Forrest Gump", 3),
            ("It does not do to dwell on dreams and forget to live.", "Harry Potter", 2),
        ]

        for text, source_title, weight in quotes_data:
            Quote.objects.get_or_create(
                text=text,
                defaults={'source': sources[source_title], 'weight': weight}
            )

        self.stdout.write('Тестовые данные загружены!')
