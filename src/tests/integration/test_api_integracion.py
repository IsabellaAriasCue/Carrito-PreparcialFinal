from fastapi.testclient import TestClient

from src.carrito.api import app
from src.database.config import get_db
from src.database.models import CarritoDB


def test_agregar_producto_api(db_session):

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)

    response = client.post(
        "/carrito/ABC123/productos",
        json={
            "nombre": "Teclado",
            "precio": 100000,
            "cantidad": 1
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["mensaje"] == "Producto agregado"

    carrito = (
        db_session.query(CarritoDB)
        .filter_by(sesion_id="ABC123")
        .first()
    )

    assert carrito is not None

    assert len(carrito.items) == 1

    app.dependency_overrides.clear()