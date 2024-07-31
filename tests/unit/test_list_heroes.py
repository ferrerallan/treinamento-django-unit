import pytest
from application.use_cases.list_heroes.list_heroes import ListHeroes
from application.use_cases.list_heroes.protocols.list_heroes_request import ListHeroesRequest
from app.models import Hero

@pytest.mark.django_db
def test_list_heroes_use_case():
    # Setup: Creating test data
    Hero.objects.create(name="Superman", canFly=True, genre="male")
    Hero.objects.create(name="Wonder Woman", canFly=False, genre="female")
    Hero.objects.create(name="Batman", canFly=False, genre="male")

    # Creating inbound request
    inbound = ListHeroesRequest()
    inbound.canFly = True
    inbound.genre = "male"

    # Executing use case
    use_case = ListHeroes()
    result = use_case.execute(inbound)

    # Assertions
    assert len(result) == 1
    assert result[0].name == "Superman"
    assert result[0].canFly is True
    assert result[0].genre == "male"
