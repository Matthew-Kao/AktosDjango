from django.core.management.base import BaseCommand, CommandError
import csv
from DjangoProject.models import Account, Consumer

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):
        if not Account.objects.exists():
            try:
                with open(options['csv_file_path'], newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        consumer, created = Consumer.objects.get_or_create(
                            name=row['consumer name'], 
                            address=row['consumer address']
                        )
                        Account.objects.create(
                            consumer=consumer,
                            client_reference_no=row['client reference no'],
                            balance=row['balance'],
                            status=row['status']
                        )
                self.stdout.write(self.style.SUCCESS('Successfully imported accounts from CSV.'))
            except Exception as e:
                raise CommandError(f'Error importing CSV: {e}')
        else:
            self.stdout.write(self.style.WARNING('Import skipped: Accounts already imported.'))
        
        
