# myapp/application/useCases/ListHeroes/ListHeroes.py
from app.models import Hero
from application.use_cases.list_heroes.protocols.list_heroes_request import (
    ListHeroesRequest,
)
from application.use_cases.list_heroes.protocols.list_heroes_response import (
    ListHeroesResponse,
)


class ListHeroes:
    def execute(self, inbound: ListHeroesRequest) -> list[ListHeroesResponse]:
        heroes = Hero.objects.filter(canFly=inbound.canFly,
                                     genre=inbound.genre)
        response = [
            ListHeroesResponse(
                id=hero.id,
                name=hero.name,
                canFly=hero.canFly,
                genre=hero.genre
            )
            for hero in heroes
        ]
        return response
    
    def sum(self, a: int, b: int) -> int:
        return a + b
