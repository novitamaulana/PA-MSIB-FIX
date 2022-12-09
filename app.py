import sklearn
from process import preparation, generate_response
from flask import Flask, render_template, request, url_for
from model import load, recommendations, recommendations_lembaga

app = Flask(__name__)

# download nltk
preparation()

# load model dan scaler
load()

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/rs')
def rs():
    return render_template('rs.html')

@app.route('/predict', methods=["post"])
def predict():
        # menangkap data yang diinput user melalui form
        nama = (request.form['nama'])
        jenis_kelamin = (request.form['jenis_kelamin'])
        umur = (request.form['umur'])  
        provinsi = (request.form['provinsi'])
        jenis_kekerasan = (request.form['jenis_kekerasan'])
        jenis_lembaga = (request.form['jenis_lembaga'])

        # melakukan prediksi menggunakan model yang telah dibuat
        index, nama_lembaga, jenis_lembaga, profile_lembaga, provinsi, alamat, kontak, jenis_kelamin, umur, jenis_kekerasan = recommendations(jenis_lembaga, provinsi, jenis_kelamin, umur, jenis_kekerasan)
        rekom_nama, rekom_profile, rekom_alamat, rekom_kontak = recommendations_lembaga(index, number_of_recommendations=1)
        return render_template('rs.html', hasil_alamat=alamat, hasil_nama=nama_lembaga, hasil_profile=profile_lembaga, hasil_kontak=kontak, hasil_nama2=rekom_nama, hasil_profile2=rekom_profile,  hasil_alamat2=rekom_alamat, hasil_kontak2=rekom_kontak)

@app.route('/chatbot')
def chatbot():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)