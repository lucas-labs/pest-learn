import logging

from pest import Pest

from .app_module import AppModule

logging.basicConfig(level=logging.DEBUG)


app = Pest.create(
    AppModule,
    title='haunted-houses'
)
