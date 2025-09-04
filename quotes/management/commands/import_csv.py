import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from quotes.models import Source, Quote

class Command(BaseCommand):
    help = 'Импорт тестовых источников и цитат из CSV'

    def handle(self, *args, **kwargs):
        src_file   = Path('quotes/fixtures/import_sources.csv')
        quote_file = Path('quotes/fixtures/import_quotes.csv')

        with src_file.open(encoding='utf-8') as f:
            next(f)                         # пропуск заголовка
            for row in csv.reader(f):
                Source.objects.update_or_create(
                    id=row[0],
                    defaults={'title': row[1]}
                )

        with quote_file.open(encoding='utf-8') as f:
            next(f)
            for text, source_id, weight in csv.reader(f):
                Quote.objects.get_or_create(
                    text=text,
                    defaults={
                        'source_id': source_id,
                        'weight'   : weight
                    }
                )
        self.stdout.write(self.style.SUCCESS('Импорт завершён'))
