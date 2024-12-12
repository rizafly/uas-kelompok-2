import streamlit as st

st.title ('luas persegi panjang')

panjang = st.number_input ("Masukan Nilai Panjang", 0)
lebar = st.number_input ("Masukan Nilai Lebar", 0)
hitung = st.button ("Hitung Luas")

if hitung :
    luas = panjang * lebar
    st.write ("Luas Persegi Panjang Adalah = " , luas)
