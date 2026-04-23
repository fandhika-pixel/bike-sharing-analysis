import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page title
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.set_page_config(layout="wide")


# Load data
df = pd.read_csv("main_data.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# --- SIDEBAR ---
st.sidebar.header("Filter Data")
year_option = st.sidebar.selectbox("Pilih Tahun", [2011, 2012])
season_option = st.sidebar.multiselect("Pilih Musim", 
                                        options=df['season'].unique(),
                                        default=df['season'].unique())

filtered_df = df[(df['dteday'].dt.year == year_option) & (df['season'].isin(season_option))]

# --- MAIN PAGE ---
st.title("🚲 Bike Sharing Analysis Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Rental", value=filtered_df['cnt'].sum())
with col2:
    st.metric("Registered Users", value=filtered_df['registered'].sum())
with col3:
    st.metric("Casual Users", value=filtered_df['casual'].sum())

st.divider()

st.subheader(f"Performa Penyewaan pada Musim yang Dipilih ({year_option})")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="season", y="cnt", data=filtered_df, estimator=sum, palette="viridis", ax=ax)
st.pyplot(fig)

st.subheader("Pengaruh Suhu terhadap Jumlah Pengguna")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(x="temp", y="casual", data=filtered_df, label="Casual", alpha=0.6, ax=ax2)
sns.scatterplot(x="temp", y="registered", data=filtered_df, label="Registered", alpha=0.6, ax=ax2)
plt.legend()
st.pyplot(fig2)

st.caption("Copyright © Ferdy Andhika Tangkeallo 2026")