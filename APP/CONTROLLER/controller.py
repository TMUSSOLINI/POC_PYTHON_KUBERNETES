from APP .SERVICE.service import ServiceCarro
from APP .SERVER.server import Server
from APP .MODEL.model import Carro, CarroCriar
from typing import List



app = Server().app


@app.get("/carros/", response_model=List[Carro])
async def get_all():
    service = ServiceCarro()
    carros = await service.find_all_service()
    return carros


@app.get("/carros/{id}", response_model=Carro)
async def get_id(id: int):
    service = ServiceCarro()
    carro = await service.find_id_service(id)
    return carro


@app.delete("/carros/{id}", status_code=204)
async def delete_car(id: int):
    service = ServiceCarro()
    await service.delete_service(id)
    
    

@app.post("/carros/", response_model=Carro, status_code=201)
async def create_car(carro: CarroCriar):
    service = ServiceCarro()
    carro_criado = await service.create_service(carro)
    return carro_criado


@app.put("/carros/{id}", response_model=Carro)
async def update_car(id: int, carro: CarroCriar):
    service = ServiceCarro()
    carro_atualizado = await service.update_service(id, carro)
    return carro_atualizado