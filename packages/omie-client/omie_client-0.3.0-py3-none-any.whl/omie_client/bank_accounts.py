import typing

from pydantic import Field, TypeAdapter, field_validator

from omie_client.endpoint import Endpoint
from omie_client.model import APIModel
from omie_client.pagination import PaginatedResponse


class BankAccountListParams(APIModel):
    pagina: int = Field(ge=0)
    codigo: int = None
    registros_por_pagina: int = Field(None, ge=1)


class BankAccount(APIModel):
    codigo_banco: str
    descricao: str
    inativo: bool
    tipo: str
    codigo_agencia: typing.Optional[str] = None
    numero_conta_corrente: typing.Optional[str] = None
    codigo: int = Field(..., alias="nCodCC")

    @field_validator("inativo", mode="before")
    @classmethod
    def parse_string_boolean(cls, value: str) -> bool:
        return value == "S"


class BankAccounts(Endpoint):
    ENDPOINT_URL: typing.ClassVar[str] = "/v1/geral/contacorrente/"

    def list(self, params: BankAccountListParams) -> PaginatedResponse[BankAccount]:
        response = self._omie_client.request(
            self.ENDPOINT_URL,
            data={
                "call": "ConsultarContaPagar",
                "param": [params.model_dump(exclude_none=True, by_alias=True)],
            },
        )
        items = response.pop("ListarContasCorrentes")

        return PaginatedResponse(
            **response, items=TypeAdapter(list[BankAccount]).validate_python(items)
        )
