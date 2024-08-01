import enum
import typing
from datetime import date, datetime

from pydantic import Field, TypeAdapter, field_validator

from omie_client.endpoint import Endpoint
from omie_client.model import APIModel
from omie_client.pagination import PaginatedResponse


class FinancialMovementDetail(APIModel):
    c_status: str
    d_dt_pagamento: date
    n_cod_titulo: int

    @field_validator("d_dt_pagamento", mode="before")
    @classmethod
    def parse_date(cls, value: str) -> date:
        return datetime.strptime(value, "%d/%m/%Y").date()


class FinancialMovement(APIModel):
    detalhes: FinancialMovementDetail


class FinancialMovementStatus(str, enum.Enum):
    CANCELADO = "CANCELADO"
    RECEBIDO = "RECEBIDO"
    LIQUIDADO = "LIQUIDADO"
    EMABERTO = "EMABERTO"
    PAGTO_PARCIAL = "PAGTO_PARCIAL"
    VENCEHOJE = "VENCEHOJE"
    AVENCER = "AVENCER"
    ATRASADO = "ATRASADO"
    NAO_CANCELADO = "NAO_CANCELADO"


class FinancialMovementListParams(APIModel):
    n_pagina: int = Field(ge=0)
    n_reg_por_pagina: int = Field(None, ge=1)
    n_cod_titulo: int = None
    c_status: FinancialMovementStatus = None


class FinancialMovements(Endpoint):
    ENDPOINT_URL: typing.ClassVar[str] = "/v1/financas/mf/"

    def list(self, params: FinancialMovementListParams) -> PaginatedResponse[FinancialMovement]:
        """List the financial movements.

        Parameters
        ----------
        params : ListParams
            The parameters to filter the listing.

        Returns
        -------
        PaginatedResponse[FinancialMovement]
        """
        response = self._omie_client.request(
            self.ENDPOINT_URL,
            data={
                "call": "ListarMovimentos",
                "param": [params.model_dump(exclude_none=True, by_alias=True)],
            },
        )

        return PaginatedResponse(
            pagina=response["nPagina"],
            total_de_paginas=response["nTotPaginas"],
            registros=response["nRegistros"],
            total_de_registros=response["nTotRegistros"],
            items=TypeAdapter(list[FinancialMovement]).validate_python(response["movimentos"]),
        )
