from flask import Flask, render_template, request, jsonify
import pickle
import os
import pandas as pd
import joblib

# Load the model
model = joblib.load('linear_regression_model.pkl')
app = Flask(__name__)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        jumlah_petani = data.get('jumlah_petani')
        luas_lahan_tanam = data.get('luas_lahan_tanam')
        luas_lahan_panen = data.get('luas_lahan_panen')
    X = pd.DataFrame({
        'jumlah_petani': [int(jumlah_petani)],
        'luas_lahan_tanam_(m2)': [int(luas_lahan_tanam)],
        'luas_lahan_panen_(m2)': [int(luas_lahan_panen)]
    })
    # standarisasi
    data_baru_scaled = scaler.transform(X)
    data_baru_scaled_df = pd.DataFrame(data_baru_scaled, columns=X.columns)
    hasil_panen_prediksi = model.predict(data_baru_scaled_df)
    # Memprediksi
    hasil_panen_prediksi_terbatas = round(hasil_panen_prediksi[0], 2)   
    return jsonify(prediction=hasil_panen_prediksi_terbatas)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
