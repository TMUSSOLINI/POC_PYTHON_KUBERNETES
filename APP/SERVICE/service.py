from APP .DAO.dao import CarroDao
from APP .MODEL.model import Carro, CarroCriar
from typing import List


class ServiceCarro:
    def __init__(self):
        self.carro_dao = CarroDao()

    
    async def find_all_service(self) -> List[Carro]:
        return await self.carro_dao.listar_carros()
    

    async def find_id_service(self, id: int):
        return await self.carro_dao.carro_id(id)
    

    async def delete_service(self, id: int):
        return await self.carro_dao.delete_car(id)
    

    async def create_service(self, carro: CarroCriar):
        return await self.carro_dao.criar_carro(carro)
    

    async def update_service(self, id: int, carro: CarroCriar):
        return await self.carro_dao.update_carro(id, carro)