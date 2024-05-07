import sys
from django.apps import AppConfig
from django.core.management import call_command

class YourAppNameConfig(AppConfig):
    name = 'DjangoProject'  

    def ready(self):
        if 'runserver' in sys.argv:
            call_command('import_accounts', 'consumers_balances.csv')
