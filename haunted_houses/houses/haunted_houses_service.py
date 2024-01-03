from .repository import HauntedHouse, HauntedHousesRepository


class HauntedHousesService:
    """The haunted houses service"""

    repository: HauntedHousesRepository  # 💉 pest will know how to inject this!

    def get_houses(self) -> list[HauntedHouse]:
        """Get all haunted houses"""
        return self.repository.get_all_houses()

    def get_house_by_id(self, house_id: int) -> HauntedHouse | None:
        """Get a haunted house by ID"""
        return self.repository.get_house_by_id(house_id)

    def create_house(self, house: HauntedHouse) -> HauntedHouse:
        """Create a new haunted house"""
        return self.repository.create_house(house)

    def update_house(self, house_id: int, updated_house: HauntedHouse) -> HauntedHouse | None:
        """Update an existing haunted house"""
        return self.repository.update_house(house_id, updated_house)

    def delete_house(self, house_id: int) -> None:
        """Delete a haunted house by ID"""
        self.repository.delete_house(house_id)
