from APP .FACTORY.factory import ConnectionDB
from APP .MODEL.model import CarroCriar, Carro
from fastapi import HTTPException


class CarroDao:
    def __init__(self):
        pass

    async def listar_carros(self):
        conn = await ConnectionDB().connection_db()
        cursor = conn.cursor()
        try:
            await cursor.execute("SELECT * FROM carros")
            resultados = await cursor.fetchall()
            carros = [Carro(id=linha[0], marca=linha[1], modelo=linha[2], preco=linha[3], descricao=linha[4]) for linha in resultados]
            return carros
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao listar os carros do banco de dados: {e}")
        finally:
            await cursor.close()
            if conn:
                await conn.ensure_closed()


    async def carro_id(self, item_id: int):
        conn = await ConnectionDB().connection_db()
        cursor =  conn.cursor()
        try:
            await cursor.execute("SELECT * FROM carros WHERE id = %s", (item_id,))
            result = await cursor.fetchone()
            if result:
                return Carro(id=result[0], marca=result[1], modelo=result[2], preco=result[3], descricao=result[4])
            else:
                raise HTTPException(status_code=404, detail="Carro não encontrado")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar o carro no banco de dados: {e}")
        finally:
            await cursor.close()
            await conn.ensure_closed()


    async def delete_car(self, id: int):
        conn = await ConnectionDB().connection_db()
        cursor =  conn.cursor()
        try:
            await cursor.execute("DELETE FROM carros WHERE id = %s", (id,))
            await conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Carro não encontrado")
        except Exception as e:
            await conn.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao deletar o carro do banco de dados: {e}")
        finally:
            await cursor.close()
            await conn.ensure_closed()


    async def criar_carro(self, carro: Carro):
        conn = await ConnectionDB().connection_db()
        cursor =  conn.cursor()
        try:
            query = "INSERT INTO carros (marca, modelo, preco, descricao) VALUES (%s, %s, %s, %s)"
            valores = (carro.marca, carro.modelo, carro.preco, carro.descricao)
            await cursor.execute(query, valores)
            await conn.commit()
            carro_id = cursor.lastrowid

            await cursor.execute("SELECT id, marca, modelo, preco, descricao FROM carros WHERE id = %s", (carro_id,))
            result = await cursor.fetchone()
            if result:
                return Carro(id=result[0], marca=result[1], modelo=result[2], preco=result[3], descricao=result[4])
            else:
                raise HTTPException(status_code=500, detail="Falha ao recuperar o carro criado")
        except Exception as e:
            await conn.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao criar o carro no banco de dados: {e}")
        finally:
            await cursor.close()
            await conn.ensure_closed()


    async def update_carro(self, car_id: int, carro: CarroCriar):
        conn = await ConnectionDB().connection_db()
        cursor =  conn.cursor()
        try:
            query = "UPDATE carros SET marca=%s, modelo=%s, preco=%s, descricao=%s WHERE id=%s"
            valores = (carro.marca, carro.modelo, carro.preco, carro.descricao, car_id)
            await cursor.execute(query, valores)
            await conn.commit()

            if cursor.rowcount > 0:
                await cursor.execute("SELECT id, marca, modelo, preco, descricao FROM carros WHERE id = %s", (car_id,))
                result = await cursor.fetchone()
                if result:
                    return Carro(id=result[0], marca=result[1], modelo=result[2], preco=result[3], descricao=result[4])
                else:
                    raise HTTPException(status_code=500, detail="Falha ao recuperar o carro atualizado")
            else:
                raise HTTPException(status_code=404, detail="carro não encontrado")
        except Exception as e:
            await conn.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar o carro no banco de dados: {e}")
        finally:
            await cursor.close()
            await conn.ensure_closed()
