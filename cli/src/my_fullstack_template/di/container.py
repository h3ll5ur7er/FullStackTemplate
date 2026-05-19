from dependency_injector import containers, providers
from .settings import Settings
from ..api_client import Client

class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration(pydantic_settings=[Settings()])

    wiring_config = containers.WiringConfiguration(modules=[".."])

    api_client = providers.Singleton(
        Client,
        base_url=config.api.base_url,
    )

_container = AppContainer()
def get_container() -> AppContainer:
    global _container
    if _container is None:
        _container = AppContainer()
    return _container