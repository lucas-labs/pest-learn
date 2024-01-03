from pydantic import BaseModel


class HauntedHouse(BaseModel):
    """A spooky house"""
    id: int
    name: str
    ghost_count: int


class HauntedHousesRepository:
    """Mock repository for haunted houses"""

    def __init__(self):
        self.houses: list[HauntedHouse] = [
            HauntedHouse(id=1, name="Spooky Manor", ghost_count=5),
            HauntedHouse(id=2, name="Eerie Estate", ghost_count=3),
        ]

    def get_all_houses(self) -> list[HauntedHouse]:
        return self.houses

    def get_house_by_id(self, house_id: int) -> HauntedHouse | None:
        return next((house for house in self.houses if house.id == house_id), None)

    def create_house(self, house: HauntedHouse) -> HauntedHouse:
        new_id = max(house.id for house in self.houses) + 1
        new_house = HauntedHouse(id=new_id, name=house.name, ghost_count=house.ghost_count)
        self.houses.append(new_house)
        return new_house

    def update_house(self, house_id: int, updated_house: HauntedHouse) -> HauntedHouse | None:
        house_index = next(
            (index for index, house in enumerate(self.houses) if house.id == house_id),
            None
        )
        if house_index is not None:
            self.houses[house_index] = updated_house
            return updated_house

    def delete_house(self, house_id: int) -> None:
        self.houses = [house for house in self.houses if house.id != house_id]
