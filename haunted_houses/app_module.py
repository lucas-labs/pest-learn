from pest import module

from .hello.module import HelloModule
from .houses.haunted_houses_module import HauntedHousesModule


@module(
    imports=[HelloModule, HauntedHousesModule],
)
class AppModule:
    pass
