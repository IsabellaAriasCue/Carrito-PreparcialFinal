from playwright.sync_api import Page
from playwright.sync_api import expect


def test_agregar_producto(page: Page):

    page.goto(
        "http://localhost:4200/carrito"
    )

    page.get_by_test_id(
        "input-nombre-producto"
    ).fill("Monitor")

    page.get_by_test_id(
        "input-precio-producto"
    ).fill("1500000")

    page.get_by_test_id(
        "input-cantidad-producto"
    ).fill("1")

    page.get_by_test_id(
        "btn-agregar-producto"
    ).click()

    expect(
        page.get_by_test_id(
            "total-carrito"
        )
    ).to_contain_text(
        "1.500.000"
    )