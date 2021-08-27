from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    help = 'Puebla la base de datos con registros fake.'

    def add_arguments(self, parser):
        parser.add_argument('cantidad', type=int, default=100)

    def handle(self, *args, **options):
        """ Do something """
        self.stdout.write(
            self.style.SUCCESS(f'Aquí un comando chido: {options["cantidad"]}')
        )
