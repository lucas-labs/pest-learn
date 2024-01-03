from pest import module
from pest.metadata.types.module_meta import ValueProvider

from .haunted_houses_controller import HauntedHousesController
from .haunted_houses_service import HauntedHousesService
from .repository import HauntedHousesRepository


@module(
    controllers=[HauntedHousesController],
    providers=[
        HauntedHousesService,
        ValueProvider(
            provide=HauntedHousesRepository,
            use_value=HauntedHousesRepository(),
        ),
    ],
)
class HauntedHousesModule:
    pass
