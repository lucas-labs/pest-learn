from pest import controller, delete, get, post, put

from .haunted_houses_service import HauntedHousesService
from .repository import HauntedHouse


@controller("/haunted-houses")
class HauntedHousesController:
    """Haunted-houses routes"""
    service: HauntedHousesService  # 💉 injected

    @get("/")
    def get_houses(self) -> list[HauntedHouse]:
        """Get all haunted houses"""
        return self.service.get_houses()

    @get("/{house_id}")
    def get_house_by_id(self, house_id: int) -> HauntedHouse:
        """Get a haunted house by ID"""
        return self.service.get_house_by_id(house_id)

    @post("/")
    def create_house(self, house: HauntedHouse) -> HauntedHouse:
        """Create a new haunted house"""
        return self.service.create_house(house)

    @put("/{house_id}")
    def update_house(self, house_id: int, updated_house: HauntedHouse) -> HauntedHouse:
        """Update an existing haunted house"""
        return self.service.update_house(house_id, updated_house)

    @delete("/{house_id}")
    def delete_house(self, house_id: int) -> None:
        """Delete a haunted house by ID"""
        self.service.delete_house(house_id)
