import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Air Quality Analysis Dashboard",
    layout="wide"
)

# Title
st.title("📊 Air Quality Analysis Dashboard")
st.markdown("Analisis PM2.5 berdasarkan faktor cuaca dan pola musiman")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/air_quality_clean.csv")

df = load_data()

# Sidebar
st.sidebar.header("Filter Data")
station = st.sidebar.selectbox(
    "Pilih Station",
    df["station"].unique()
)

df_filtered = df[df["station"] == station]

# --- Visualization 1 ---
st.subheader("📈 PM2.5 Trend Over Time")

fig, ax = plt.subplots()
df_filtered.groupby("month")["PM2.5"].mean().plot(ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("PM2.5")
st.pyplot(fig)

# --- Visualization 2 ---
st.subheader("🌦️ PM2.5 vs Weather Factors")

fig, ax = plt.subplots()
sns.scatterplot(
    data=df_filtered,
    x="WSPM",
    y="PM2.5",
    alpha=0.5,
    ax=ax
)
ax.set_xlabel("Wind Speed (WSPM)")
ax.set_ylabel("PM2.5")
st.pyplot(fig)

# --- Insight ---
st.subheader("🧠 Key Insights")
st.markdown("""
- PM2.5 cenderung lebih tinggi pada musim dingin.
- Kecepatan angin memiliki pengaruh negatif paling kuat terhadap PM2.5.
- Faktor cuaca berkontribusi terhadap variasi kualitas udara.
""")
