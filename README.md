# Air Quality Data Analysis & Dashboard

## Deskripsi
Repository ini berisi analisis data kualitas udara menggunakan dataset Air Quality yang disediakan pada soal tugas. Analisis difokuskan pada eksplorasi konsentrasi PM2.5 serta hubungannya dengan faktor cuaca dan pola musiman.

## Tools & Library
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Cara Menjalankan Notebook
1. Buka file `.ipynb` menggunakan Jupyter Notebook atau Google Colab.
2. Jalankan cell secara berurutan untuk melihat proses analisis data.

## Cara Menjalankan Dashboard Streamlit
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
exit
```

## Insight Utama
1. Konsentrasi PM2.5 menunjukkan pola musiman, dengan nilai lebih tinggi pada musim dingin.
Kecepatan angin memiliki pengaruh negatif paling kuat terhadap PM2.5.
2. Faktor cuaca berkontribusi terhadap variasi kualitas udara.
