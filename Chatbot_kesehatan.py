from flask import Flask, render_template, request

app = Flask(__name__)

def get_response(question):
    responses = {
        "apa itu diabetes?": {
            "penjelasan": "Diabetes adalah penyakit kronis yang terjadi ketika tubuh tidak dapat menghasilkan cukup insulin atau tidak dapat menggunakannya dengan efektif. Hal ini menyebabkan peningkatan kadar gula dalam darah yang dapat berisiko bagi kesehatan jika tidak dikontrol dengan baik.",
            "gejala": "Gejala umum diabetes meliputi sering merasa haus, sering buang air kecil, mudah lelah, penurunan berat badan tanpa sebab, dan penglihatan kabur.",
            "obat": "Obat yang umum digunakan untuk diabetes antara lain Metformin, Insulin, Sulfonylurea, dan DPP-4 inhibitors. Selalu konsultasikan dengan dokter sebelum menggunakan obat ini.",
            "pencegahan": "Jaga pola makan sehat, rutin berolahraga, hindari konsumsi gula berlebihan, dan lakukan pemeriksaan gula darah secara berkala."
        },
        "apa itu hipertensi?": {
            "penjelasan": "Hipertensi, atau tekanan darah tinggi, adalah kondisi di mana tekanan darah dalam arteri meningkat secara terus-menerus. Jika tidak ditangani, kondisi ini dapat meningkatkan risiko serangan jantung, stroke, dan masalah kesehatan lainnya.",
            "gejala": "Hipertensi sering disebut 'silent killer' karena jarang menunjukkan gejala. Namun, pada kasus berat, gejala seperti sakit kepala, pusing, dan mimisan dapat terjadi.",
            "obat": "Obat yang umum digunakan untuk hipertensi antara lain Amlodipine, Lisinopril, Losartan, dan Hydrochlorothiazide. Penggunaan obat harus sesuai resep dokter.",
            "pencegahan": "Kurangi konsumsi garam, hindari stres, rutin berolahraga, dan lakukan pemeriksaan tekanan darah secara berkala."
        },
        "apa itu anemia?": {
            "penjelasan": "Anemia adalah kondisi di mana tubuh kekurangan sel darah merah atau hemoglobin, yang berperan dalam membawa oksigen ke seluruh tubuh. Ini bisa menyebabkan gejala seperti lelah berkepanjangan, pucat, dan sesak napas.",
            "gejala": "Gejala anemia meliputi kelelahan, kulit pucat, sesak napas, pusing, dan tangan/kaki dingin.",
            "obat": "Obat yang umum digunakan untuk anemia antara lain suplemen zat besi (seperti Ferrous Sulfate), vitamin B12, dan asam folat. Konsultasikan dengan dokter untuk dosis yang tepat.",
            "pencegahan": "Konsumsi makanan kaya zat besi seperti daging merah, bayam, dan kacang-kacangan. Hindari minum teh atau kopi bersamaan dengan makanan kaya zat besi karena dapat menghambat penyerapan."
        },
        "apa itu demam berdarah?": {
            "penjelasan": "Demam berdarah adalah penyakit yang disebabkan oleh virus dengue yang ditularkan melalui gigitan nyamuk Aedes aegypti.",
            "gejala": "Gejala demam berdarah meliputi demam tinggi, sakit kepala parah, nyeri otot dan sendi, mual, muntah, dan ruam kulit.",
            "obat": "Tidak ada obat khusus untuk demam berdarah. Pengobatan biasanya bersifat suportif, seperti pemberian cairan intravena dan obat penurun demam (Paracetamol). Hindari obat seperti Aspirin karena dapat meningkatkan risiko perdarahan.",
            "pencegahan": "Hindari gigitan nyamuk dengan menggunakan kelambu, losion anti-nyamuk, dan membersihkan lingkungan dari genangan air."
        },
        "apa itu tifus?": {
            "penjelasan": "Tifus adalah penyakit infeksi yang disebabkan oleh bakteri Salmonella typhi. Penyakit ini menyebar melalui makanan atau air yang terkontaminasi.",
            "gejala": "Gejala tifus meliputi demam tinggi, sakit kepala, lemas, sakit perut, dan kehilangan nafsu makan.",
            "obat": "Obat yang umum digunakan untuk tifus adalah antibiotik seperti Ciprofloxacin atau Azithromycin. Pengobatan harus sesuai resep dokter.",
            "pencegahan": "Hindari konsumsi makanan atau minuman yang tidak higienis, cuci tangan sebelum makan, dan pastikan air yang diminum bersih."
        },
        "apa itu malaria?": {
            "penjelasan": "Malaria adalah penyakit yang disebabkan oleh parasit Plasmodium yang ditularkan melalui gigitan nyamuk Anopheles.",
            "gejala": "Gejala malaria meliputi demam, menggigil, sakit kepala, mual, dan muntah.",
            "obat": "Obat yang umum digunakan untuk malaria adalah Chloroquine, Artemether-Lumefantrine, dan Quinine. Pengobatan harus sesuai resep dokter.",
            "pencegahan": "Gunakan kelambu saat tidur, hindari gigitan nyamuk, dan lakukan pengobatan pencegahan jika bepergian ke daerah endemis malaria."
        },
        "apa itu tuberkulosis?": {
            "penjelasan": "Tuberkulosis (TB) adalah penyakit infeksi yang disebabkan oleh bakteri Mycobacterium tuberculosis, biasanya menyerang paru-paru.",
            "gejala": "Gejala TB meliputi batuk berkepanjangan (lebih dari 2 minggu), demam, keringat malam, penurunan berat badan, dan kelelahan.",
            "obat": "Obat yang umum digunakan untuk TB adalah Rifampicin, Isoniazid, Pyrazinamide, dan Ethambutol. Pengobatan TB memerlukan waktu minimal 6 bulan.",
            "pencegahan": "Lakukan vaksinasi BCG, hindari kontak dengan penderita TB aktif, dan jaga daya tahan tubuh."
        },
        "apa itu hepatitis?": {
            "penjelasan": "Hepatitis adalah peradangan pada hati yang dapat disebabkan oleh infeksi virus, konsumsi alkohol berlebihan, atau obat-obatan tertentu.",
            "gejala": "Gejala hepatitis meliputi kulit dan mata kuning (jaundice), kelelahan, sakit perut, mual, dan urine berwarna gelap.",
            "obat": "Pengobatan hepatitis tergantung pada jenisnya. Untuk hepatitis B dan C, obat antivirus seperti Tenofovir atau Sofosbuvir dapat digunakan. Konsultasikan dengan dokter untuk penanganan yang tepat.",
            "pencegahan": "Hindari konsumsi alkohol berlebihan, lakukan vaksinasi hepatitis B, dan hindari penggunaan jarum suntik yang tidak steril."
        },
        # Lanjutkan dengan penyakit lainnya...
    }
    return responses.get(question.lower(), {
        "penjelasan": "Maaf, saya belum memiliki informasi lengkap tentang hal itu. Silakan tanyakan hal lain atau konsultasikan dengan tenaga medis untuk informasi yang lebih akurat.",
        "gejala": "-",
        "obat": "-",
        "pencegahan": "-"
    })

@app.route('/', methods=['GET', 'POST'])
def index():
    response = {"penjelasan": "", "gejala": "", "obat": "", "pencegahan": ""}
    if request.method == 'POST':
        question = request.form.get('question', '')
        response = get_response(question)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)