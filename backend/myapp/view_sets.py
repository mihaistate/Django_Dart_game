from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from django.apps import apps
from .serializers import PokemonSerializer, HelpRequestSerializer, UserSerializer

Pokemon = apps.get_model('myapp', 'Pokemon')
HelpRequest = apps.get_model('myapp', 'HelpRequest')

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class HelpRequestViewSet(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def submit_request(self, request):
        user = request.user
        description = request.data.get('description')
        print(f"User: {user}, Description: {description}")
        if not description:
            return Response({"error": "Description is required"}, status=status.HTTP_400_BAD_REQUEST)
        pokemon = self.get_next_pokemon()
        if pokemon is None:
            return Response({"error": "No Pokémon available"}, status=status.HTTP_400_BAD_REQUEST)
        help_request = HelpRequest.objects.create(user=user, pokemon=pokemon, description=description)
        return Response({'status': 'request submitted', 'help_request': HelpRequestSerializer(help_request).data})

    def get_next_pokemon(self):
        # Implement round-robin allocation logic
        last_request = HelpRequest.objects.order_by('-created_at').first()
        if last_request:
            last_pokemon = last_request.pokemon
            next_pokemon = Pokemon.objects.filter(id__gt=last_pokemon.id).first()
            if not next_pokemon:
                next_pokemon = Pokemon.objects.first()
        else:
            next_pokemon = Pokemon.objects.first()
        
        # Add logging to check the selected Pokémon
        if next_pokemon:
            print(f"Selected Pokémon: {next_pokemon.name} (ID: {next_pokemon.id})")
        else:
            print("No Pokémon found")
        
        return next_pokemon
    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer