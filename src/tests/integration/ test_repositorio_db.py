from src.database.models import CarritoDB
from src.database.repositorio import CarritoRepositorio


def test_agregar_item_persiste_en_bd(db_session):

    repo = CarritoRepositorio(db_session)

    repo.agregar_item(
        "SESION001",
        "Mouse",
        50000,
        2
    )

    carrito = (
        db_session.query(CarritoDB)
        .filter_by(sesion_id="SESION001")
        .first()
    )

    assert carrito is not None

    assert carrito.sesion_id == "SESION001"

    assert len(carrito.items) == 1

    item = carrito.items[0]

    assert item.nombre == "Mouse"
    assert item.precio == 50000
    assert item.cantidad == 2