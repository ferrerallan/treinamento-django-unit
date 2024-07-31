# myapp/presentation/controllers/list_heroes_controller.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from application.use_cases.list_heroes.list_heroes import ListHeroes
from application.use_cases.list_heroes.protocols.list_heroes_request import ListHeroesRequest


class ListHeroesController(APIView):   
    def post(self, request):
        try:
            # Building inbound
            inbound = ListHeroesRequest()
            inbound.canFly = request.data.get("canFly", "false").lower() == "true"
            inbound.genre = request.data.get("genre", "male")

            # Executing use case
            use_case = ListHeroes()
            result = use_case.execute(inbound)

            # Serializing the result
            outbound = [hero.__dict__ for hero in result]

            return Response({"data": outbound}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"message_error": "Error on listing heroes"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
