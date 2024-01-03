from pest import module

from .haunted_houses_service import HauntedHousesService
from .repository import HauntedHousesRepository


@module(
    providers=[HauntedHousesService, HauntedHousesRepository],
)
class HauntedHousesModule:
    pass
