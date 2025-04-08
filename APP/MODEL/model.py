from pydantic import BaseModel


class CarroCriar(BaseModel):
    marca: str
    modelo: str
    preco: float | None = None
    descricao: str


class Carro(CarroCriar):
    id: int