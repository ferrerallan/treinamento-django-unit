from django.urls import path
from presentation.controllers.list_heroes_controller import (
    ListHeroesController)

urlpatterns = [
    path("heroes", ListHeroesController.as_view()),
]
