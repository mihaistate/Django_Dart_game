import requests
from django.core.management.base import BaseCommand
from myapp.models import Pokemon

class Command(BaseCommand):
    help = 'Fetch Pokémon data from PokeAPI'

    def handle(self, *args, **kwargs):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
        data = response.json()
        for item in data['results']:
            pokemon_response = requests.get(item['url'])
            pokemon_data = pokemon_response.json()
            Pokemon.objects.update_or_create(
                name=pokemon_data['name'],
                defaults={
                    'moves': pokemon_data['moves'],
                    'abilities': pokemon_data['abilities'],
                    'types': pokemon_data['types'],
                    'staff_id': f"staff_{pokemon_data['id']}"
                }
            )