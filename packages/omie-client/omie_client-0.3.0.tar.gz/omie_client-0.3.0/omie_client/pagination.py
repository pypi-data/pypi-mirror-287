import typing

from omie_client.model import APIModel

T = typing.TypeVar("T")


class PaginatedResponse(APIModel, typing.Generic[T]):
    pagina: int
    total_de_paginas: int
    registros: int
    total_de_registros: int
    items: list[T]
