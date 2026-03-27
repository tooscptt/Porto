from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Fungsi untuk membuat database dan tabel jika belum ada
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Membuat tabel pesan dengan struktur yang jelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            email TEXT NOT NULL,
            pesan TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Jalankan fungsi inisialisasi database
init_db()

# Membuat API Endpoint untuk menerima data dari Front-End
@app.route('/submit-pesan', methods=['POST'])
def submit_pesan():
    # Mengambil data berformat JSON dari JavaScript
    data = request.json
    nama = data.get('nama')
    email = data.get('email')
    pesan = data.get('pesan')

    # Validasi di sisi server (Back-End)
    if not nama or not email or not pesan:
        return jsonify({"status": "error", "message": "Data tidak lengkap!"}), 400

    # PROSES SIMPAN KE DATABASE (AMAN DARI SQL INJECTION)
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # PERHATIKAN: Kita menggunakan tanda tanya (?) sebagai Parameterized Query.
        # Ini mencegah hacker memasukkan script SQL jahat melalui form input.
        cursor.execute("INSERT INTO messages (nama, email, pesan) VALUES (?, ?, ?)", (nama, email, pesan))
        
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success", "message": "Pesan berhasil disimpan!"}), 200
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Menjalankan server di port 5000
    app.run(debug=True, port=5000)