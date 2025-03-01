import pytest
import json
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data  # Cek apakah HTML dikembalikan


def test_predict(client):
    # Data input untuk prediksi
    test_data = {
        "jumlah_petani": 10,
        "luas_lahan_tanam": 5000,
        "luas_lahan_panen": 4000
    }
    # Kirim permintaan POST ke /predict
    response = client.post('/predict', data=json.dumps(test_data),
                           content_type='application/json')

    # Periksa status respons
    assert response.status_code == 200

    # Periksa apakah respons mengandung prediksi
    response_json = response.get_json()
    assert "prediction" in response_json
    assert isinstance(response_json["prediction"],
                      (int, float))  # Harus berupa angka
