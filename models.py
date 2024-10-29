import requests
from django.core.management.base import BaseCommand
from models import Pokemon
import uuid

def generate_unique_staff_id():
    return str(uuid.uuid4)


class Command(BaseCommand):
    help = 'Fetch Pokemon data from PokeAPI'
    
    
    def handle(self, *args, **kwargs):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
        for pokemon in response.json()['results']:
            details = requests.get(pokemon['url']).json()
            Pokemon.objects.update_or_create(
                name=details['name'],
                defaults={
                    'moves': details['moves'],
                    'abilities': details['abilities'],
                    'types': details['types'],
                    'staff_id': generate_unique_staff_id(),
                }
            )
        