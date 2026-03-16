# 📱 E-Commerce Price Predictor (HP/Laptop)
### *Collaborative Project: Data Engineering x Data Science*

Proyek ini adalah aplikasi web cerdas yang memberikan saran harga jual barang bekas berdasarkan spesifikasi teknis (RAM, Storage, Brand, dll) menggunakan **Machine Learning**.

---

## 👥 Meet the Team
* **Alena Ghinna Kirana (Data/AI Engineer):** Bertanggung jawab pada *deployment*, pembuatan API (FastAPI), *containerization* (Docker), dan Frontend (React).
* **Nazwa Oktaviani Mohammad (Data Scientist):** Bertanggung jawab pada *Exploratory Data Analysis* (EDA), *model training*, dan optimasi algoritma regresi.

---

## 🚀 Features
* ✅ **Accurate Prediction:** Menggunakan algoritma Random Forest/Linear Regression untuk estimasi harga.
* ✅ **Modern API:** Dibangun dengan **FastAPI** yang cepat dan terdokumentasi secara otomatis (Swagger UI).
* ✅ **Containerized:** Aplikasi dapat dijalankan di mana saja menggunakan **Docker**.
* ✅ **User-Friendly UI:** Dashboard input yang simpel berbasis **React**.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python, JavaScript |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy |
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | React.js, Axios |
| **DevOps** | Docker, Docker Compose |

---

## 🏗️ System Architecture
Berikut adalah gambaran bagaimana data mengalir dalam sistem ini:

1.  **Frontend (React):** User menginput spesifikasi barang.
2.  **API (FastAPI):** Menerima data input dan memprosesnya.
3.  **Model AI (.pkl):** Melakukan kalkulasi prediksi berdasarkan pola data historis.
4.  **Result:** Harga prediksi dikirim kembali ke user.

---

## 🔧 How to Run
Gak perlu ribet install library satu-satu, cukup jalankan perintah ini (pastikan sudah install Docker):

```bash
docker-compose up --build
Akses aplikasi di: http://localhost:3000

##📈 Model Performance (Sisi Data Science)
Dataset: [Sebutkan nama dataset/link Kaggle di sini]

**Algorithm: Random Forest Regressor**

**Metrics: * R-Squared: 0.XX**

**MAE: XXXX**


---
