from flask import Flask, render_template, request

app = Flask(__name__)

penyakit_data = {
    'Demam Berdarah': {
        'gejala': {'demam tinggi', 'mual', 'nyeri otot'},
        'obat': [
            {'nama': 'Paracetamol', 'harga': 'Rp5.000 - Rp10.000', 'dosis': '500mg, 3x sehari'},
            {'nama': 'Infus cairan', 'harga': 'Rp50.000 - Rp100.000', 'dosis': 'Sesuai petunjuk dokter'},
            {'nama': 'Istirahat total', 'harga': 'Gratis', 'dosis': 'Minimal 3 hari'}
        ]
    },
    'Influenza': {
        'gejala': {'demam', 'batuk', 'pilek'},
        'obat': [
            {'nama': 'Paracetamol', 'harga': 'Rp5.000 - Rp10.000', 'dosis': '500mg, 3x sehari'},
            {'nama': 'Vitamin C', 'harga': 'Rp3.000 - Rp7.000', 'dosis': '1 tablet per hari'},
            {'nama': 'Obat batuk', 'harga': 'Rp7.000 - Rp15.000', 'dosis': '10ml, 3x sehari'}
        ]
    },
    'Tipes': {
        'gejala': {'demam tinggi', 'sakit perut', 'lemas'},
        'obat': [
            {'nama': 'Antibiotik', 'harga': 'Rp20.000 - Rp50.000', 'dosis': 'Sesuai resep dokter'},
            {'nama': 'Paracetamol', 'harga': 'Rp5.000 - Rp10.000', 'dosis': '500mg, 3x sehari'},
            {'nama': 'Makan bergizi', 'harga': 'Variatif', 'dosis': '3x sehari'}
        ]
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    umur = None

    if request.method == 'POST':
        input_gejala = set(request.form.getlist('gejala'))
        umur = request.form.get('umur')
        rekomendasi = []

        for penyakit, data in penyakit_data.items():
            if input_gejala & data['gejala']:
                rekomendasi.append({
                    'penyakit': penyakit,
                    'obat': data['obat']
                })

        hasil = rekomendasi if rekomendasi else 'Tidak ditemukan penyakit yang cocok.'

    return render_template('index.html', hasil=hasil, umur=umur)

if __name__ == '__main__':
    app.run(debug=True)
