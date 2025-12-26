# Air Quality Data Analysis & Dashboard

## Deskripsi
Repository ini berisi analisis data kualitas udara menggunakan dataset Air Quality yang disediakan pada soal tugas. Analisis difokuskan pada eksplorasi konsentrasi PM2.5 serta hubungannya dengan faktor cuaca dan pola musiman.

dataset : https://github.com/marceloreis/HTI/tree/master

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
link dashboard : https://dashboardairqualityanalysis-ftjr7zzwjt7rqsngdwn8v4.streamlit.app/
## preview dashboard
<img width="1910" height="870" alt="Screenshot 2025-12-27 004017" src="https://github.com/user-attachments/assets/eeddbbd2-9692-4029-ae97-734739b807ed" />
<img width="1919" height="868" alt="Screenshot 2025-12-27 004303" src="https://github.com/user-attachments/assets/17678100-32ef-42ef-9a32-4cf4ae8b84df" />
<img width="1911" height="871" alt="Screenshot 2025-12-27 004028" src="https://github.com/user-attachments/assets/3565d0c7-1fa1-4c24-8843-afd7a0623506" />


## Insight Utama
1. Konsentrasi PM2.5 menunjukkan pola musiman, dengan nilai lebih tinggi pada musim dingin.
Kecepatan angin memiliki pengaruh negatif paling kuat terhadap PM2.5.
2. Faktor cuaca berkontribusi terhadap variasi kualitas udara.
