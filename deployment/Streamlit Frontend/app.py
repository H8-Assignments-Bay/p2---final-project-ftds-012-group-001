import streamlit as st
from PIL import Image
import requests

text_title = '<h1 style="font-family:sans-serif; color:#7a00a3; text-align:center;">ClickSpace Harga Hotel</h1>'
st.markdown(text_title, unsafe_allow_html=True)
img = Image.open('clickspace_logo.png')
st.image(img, width=35, use_column_width=True)
st.title('  ')
st.markdown('ClickSpace memberikan kemudahan terhadap anda yang ingin mengetahui kisaran harga yang harus dikeluarkan saat memilih hotel atau penginapan dengan memberikan informasi harga, dimana ClikSpace memuat informasi-informasi penting berupa kisaran harga berdasarkan jenis hotel yang diinginkan parawisatawan.') 
st.subheader(' ')
text_title1 = '<h1 style="font-family:sans-serif; color:#7a00a3; text-align:center;">Check Harga Hotel</h1>'
st.markdown(text_title1, unsafe_allow_html=True)

# Predict price hotel
with st.form(key='form_parameters'):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
         Nama_Hotel = st.text_input("Nama Hotel")
    
    with col2:
        Provinsi = st.selectbox("Lokasi Hotel (Provinsi)", ['Daerah Khusus Ibukota Jakarta', 'Banten', 'Jawa Barat','Jawa Timur', 'Daerah Istimewa Yogyakarta','Special Region of Yogyakarta', 'Sumatera Utara', 'North Sumatra','Jawa Tengah', 'Bali', 'Nusa Tenggara Barat', 'West Nusa Tenggara','Central Java', 'Kabupaten Badung'])
    
    with col3:
         Nama_Kota = st.selectbox("Lokasi Hotel (Kota)", ['Kota Jakarta Selatan', 'Kota Jakarta Pusat', 'Kota Jakarta Barat','Kota Jakarta Timur', 'Kota Jakarta Utara', 'North Jakarta City','Kota Tangerang', 'Kota Bekasi', 'Kota Bandung','Kabupaten Bandung Barat', 'Kabupaten Subang', 'Bandung City','Kabupaten Sumedang', 'Kabupaten Bandung', 'Subang Regency','Kota Cimahi', 'Kota Surabaya', 'Surabaya City','Kabupaten Sidoarjo', 'Kabupaten Sleman', 'Kota Yogyakarta','Kabupaten Bantul', 'Kabupaten Gunung Kidul', 'Bantul Regency','Kota Medan', 'Kabupaten Deli Serdang', 'Medan City','Kota Semarang', 'Kabupaten Semarang', 'Kota Malang','Kabupaten Malang', 'Kota Batu', 'Malang City','Kabupaten Magelang', 'Kabupaten Badung', 'Gianyar Regency','Kabupaten Buleleng', 'Kabupaten Lombok Barat','Kabupaten Lombok Tengah', 'Kota Mataram', 'Badung Regency','Central Lombok Regency', 'Kota Denpasar', 'Kabupaten Gianyar','Kabupaten Lombok Utara', 'North Lombok Regency', 'Kuta','Semarang City', 'West Lombok Regency', 'Kuta Lombok','Semarang Regency', 'East Lombok Regency', 'Kabupaten Jembrana','Kabupaten Klungkung', 'Kabupaten Lombok Timur', 'Batu City','Lombok', 'Karangasem Regency', ' Seminyak', ' Bali', ' Malang','Buleleng Regency', 'Regency', 'Klungkung Regency','Bangli Regency', 'Mataram City', 'Kabupaten Karangasem','Kabupaten Tabanan', 'Kota Cirebon', 'Kabupaten Cirebon'])
    
    col4, col5, col6 = st.columns([1, 1, 1])
    with col4:
         Luas_Kamar = st.number_input("Luas Ruangan Hotel")
    
    with col5:
        Kapasitas = st.number_input("Kapasitas")
    
    with col6:
         Rating = st.number_input("Rating Penilaian")

    col1, col2, col3 = st.columns([3, 1, 3])
    with col2:
        submitted = st.form_submit_button('Harga Hotel')

# inference
data = {'Nama Hotel' : Nama_Hotel,
        'Nama Kota' : Nama_Kota,
        'Provinsi' : Provinsi,
        'Luas Kamar' : Luas_Kamar,
        'Kapasitas' : Kapasitas,
        'Rating' : Rating}

# URL = "http://127.0.0.1:5000/price_hotel" # sebelum push backend
URL = "https://backend-price-hotel.herokuapp.com/price_hotel" # URL Heroku

# communication
r = requests.post(URL, json=data)
res = r.json()
# if r.status_code == 200:
if submitted:
       prediction = res['prediction']
       st.subheader(prediction)

