import httpx


def test_flujo_completo_carrito():

    base_url = "http://localhost:8000"

    sesion = "CLIENTE001"

    response = httpx.post(
        f"{base_url}/carrito/{sesion}/productos",
        json={
            "nombre": "Monitor",
            "precio": 1000000,
            "cantidad": 1
        }
    )

    assert response.status_code == 201

    response = httpx.post(
        f"{base_url}/carrito/{sesion}/productos",
        json={
            "nombre": "Mouse",
            "precio": 50000,
            "cantidad": 1
        }
    )

    assert response.status_code == 201

    response = httpx.get(
        f"{base_url}/carrito/{sesion}"
    )

    assert response.status_code == 200

    carrito = response.json()

    assert carrito["total"] == 1050000