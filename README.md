
# TCC Backend

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=1388F7&random=false&width=435&lines=Training+Code+Center)](https://git.io/typing-svg)

**TCC (Training Code Center)** adalah wadah belajar pemrograman kompetitif yang dirancang khusus untuk mahasiswa Universitas Syiah Kuala (USK). Platform ini memungkinkan pengguna untuk mengasah keterampilan dalam menyelesaikan berbagai tantangan pemrograman💻. Setiap jawaban yang benar akan memberikan pengguna poin, dan ada sejumlah tingkatan prestasi, seperti "Sepuh"🥇, "Master"🥈, dan "Pemula"🥉, yang mencerminkan tingkat keahlian berdasarkan jumlah poin yang diperoleh🏆.


## Installation 🛠️

- Klon projek ini dengan menjalankan perintah berikut

```bash
  git clone git@github.com:fadhrr/TCC-Backend.git
  cd TCC-Backend
  pip install -r requirements.txt
  cd app
```

- import basic mysql schema `tcc-database.sql`

- Bila menggunakan *phpmyadmin*, buat database `tcc_database``, lalu import schemanya

**Inisiasi Konfigurasi:**

- Buat file baru `.env` di dalam direktori `app/`, salin isi dari file `.env.example`, dan atur nilai-nilai sesuai kebutuhan proyek Anda.
```
  copy .env.example .env (windows)
  cp .env.example .env (linux)
```

- setelah konfigurasi selesai, 🚀jalankan server dengan dengan mengeksekusi perintah 
```
  uvicorn main:app --reload
```

## Documentation 📚

Untuk melihat dokumentasi lokal, jalankan project terlebih dahulu. Lalu buka url `http://localhost:8000/docs`

## Note📝
- Memerlukan mysql


    
