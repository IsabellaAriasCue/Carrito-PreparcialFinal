from src.database.models import (
    CarritoDB,
    ItemCarritoDB
)


class CarritoRepositorio:

    def __init__(self, db):
        self.db = db

    def agregar_item(
        self,
        sesion_id,
        nombre,
        precio,
        cantidad
    ):

        carrito = (
            self.db.query(CarritoDB)
            .filter_by(sesion_id=sesion_id)
            .first()
        )

        if carrito is None:

            carrito = CarritoDB(
                sesion_id=sesion_id
            )

            self.db.add(carrito)

            self.db.flush()

        item = ItemCarritoDB(
            carrito_id=carrito.id,
            nombre=nombre,
            precio=precio,
            cantidad=cantidad
        )

        self.db.add(item)

        self.db.commit()

        self.db.refresh(item)

        return item

    def calcular_total(self, sesion_id):

        carrito = (
            self.db.query(CarritoDB)
            .filter_by(sesion_id=sesion_id)
            .first()
        )

        if carrito is None:
            return 0

        return sum(
            item.precio * item.cantidad
            for item in carrito.items
        )