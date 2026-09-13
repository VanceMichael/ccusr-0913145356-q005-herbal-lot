from app.main import create_app

def test_health() -> None:
    response = create_app().test_client().get("/healthz")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
