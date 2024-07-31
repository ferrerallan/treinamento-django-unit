class ListHeroesResponse:
    def __init__(self, id: int, name: str, canFly: bool, genre: str):
        self.id = id
        self.name = name
        self.canFly = canFly
        self.genre = genre
