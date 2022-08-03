import folium
import requests
import streamlit as st
from streamlit_option_menu import option_menu
import folium
import pickle
import os
import pandas as pd
import time
from streamlit_folium import folium_static 


base_path = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_path, 'model')
cosine_filename = 'cosine.pkl'
cosine_filepath = os.path.join(model_path, cosine_filename)
with open(cosine_filepath, "rb") as filename:
    cosine = pickle.load(filename)

st.set_page_config(
    page_title = "Click Space | Find your space, in one click!",
    page_icon= "🏩",
    layout = 'centered',
    initial_sidebar_state = 'collapsed',
    menu_items={
        'Get Help': 'https://www.github.com/fahmihamzah84',
        'Report a bug': "https://github.com/fahmihamzah84",
        'About': "Welcome to our website for hotel recommendations", 
    }
)

@st.cache
def load_data1():
    data1 = pd.read_csv("https://raw.githubusercontent.com/H8-Assignments-Bay/p2---final-project-ftds-012-group-001/main/dataset/data_hotel.csv")
    return data1

@st.cache
def load_data2():
    data2 = pd.read_csv("https://raw.githubusercontent.com/H8-Assignments-Bay/p2---final-project-ftds-012-group-001/main/Notebook/latlong_kota.csv")
    return data2

@st.cache
def load_data3():
    data3 = pd.read_csv("https://raw.githubusercontent.com/H8-Assignments-Bay/p2---final-project-ftds-012-group-001/main/dataset/detailhotel_modif.csv")
    return data3

data1 = load_data1()
data2 = load_data2()
data3 = load_data3()

data = data1.copy()
data['Nama Hotel'] = data['Nama Hotel'].str.lower()
nama_kota = data2.copy()
data_hotel_price = data3.copy()
# Page config

def sidebar_bg():

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: linear-gradient(rgba(255,255,255,.8), rgba(255,255,255,.8)), url(https://i.ibb.co/6PLFkqY/wallpaperflare-com-wallpaper.jpg);
      }}
      </style>
      """,
      unsafe_allow_html=True,
)
sidebar_bg()
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url("https://i.ibb.co/yWXmtqW/wallpaperflare-com-wallpaper-2.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()
st.sidebar.image('https://i.ibb.co/7NvYR8K/clickspace-logo.png')
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=['Hotel Recommendation', 'Price Prediction'],
        menu_icon="cast",
        icons=['map', 'cash-coin'],
        default_index=0,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://clickspace.herokuapp.com/) is maintained by [Hillidatul Ilmi](https://github.com/hillidatulilmi) and [Fahmi Hamzah](https://github.com/fahmihamzah84). You can follow us on social media:
            [GitHub Hillidatul Ilmi](https://github.com/hillidatulilmi) | [GitHub Fahmi Hamzah](https://github.com/fahmihamzah84) | [LinkedIn Hillidatul Ilmi](https://www.linkedin.com/in/hillidatul-ilmi-287721228/) | [LinkedIn Fahmi Hamzah](https://www.linkedin.com/in/fahmihamzaah/).
        
        Source code: [Source](https://github.com/H8-Assignments-Bay/p2---final-project-ftds-012-group-001)
    """
    )

if selected == 'Hotel Recommendation':
    opener = 'gambar'
    if opener == 'gambar':
        gif1 = '<div style="width:100%; display:flex; justify-content:center; align-items:center"><iframe allow="fullscreen" frameBorder="0" height="400" src="https://i.ibb.co/yhq6s4y/clickspacee.png" width="1440"></iframe></div>'
        st.markdown(gif1, unsafe_allow_html=True)

    st.markdown('<br><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([.8, 1, 1])
    with col1:
        st.write(' ')

    with col2:
        st.image('https://i.ibb.co/7NvYR8K/clickspace-logo.png', width=300)

    with col3:
        st.write(' ')
    About_us = '<h2 style="font-family:Monospace; color:#9401fd; text-align:left;">About Us</h2>'
    st.markdown(About_us, unsafe_allow_html=True)
    isi_about_us = '<h4 style="font-family:Monospace; color:#000000; text-align:justify;">ClickSpace makes it easy for those of you who will make hotel or lodging reservations by providing the best hotel recommendations. Here we provides recommendations where you can filter the desired hotel such as hotel recommendations based on similarities, finding the best hotel in Town, or hotel recommendations based on your preferences such as Hotels rating, stars, room types that can be your reference in choosing a hotel or lodge. </h4>'
    st.markdown(isi_about_us, unsafe_allow_html=True)
    title1 = '<h2 style="font-family:Monospace; color:#9401fd; text-align:center;">🌆 Hotel Recommendation Page 🌆</h2>'
    st.markdown(title1, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    hotel_recomen_page = """<h4 style="font-family:Monospace; color:#000000; text-align:left;">We present three options for Hotel recommendation types. <ul><li> <strong>Similar Hotels</strong> We'll provide hotel recommendations that are similar to the hotel you choose!</li> <li><strong>Based on City</strong> We'll give you recommendations for the best hotels in the city you choose, you can also sort by rating or stars </li><li><strong>Based on my preferences</strong> You will be given hotel recommendations based on your desired preferences</li></ul></h4>"""
    titlemap = '<h3 style="font-family:Monospace; color:#9401fd; text-align:center;">📍 You can locate our recommendations below 📍</h3>'
    st.markdown(hotel_recomen_page, unsafe_allow_html=True)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
    pilihan = st.radio("",("Similar Hotel","Based on City","Based on my preferences"))
    hotels_name = data['Nama Hotel'].apply(lambda x: x.title())
    if pilihan == "Similar Hotel":
        with st.form(key='form_parameters'):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                col_name = st.text_input('Your name')
                col_hotel = st.selectbox('Hotel similar to : ', hotels_name)
                st.markdown('<br>', unsafe_allow_html=True)
                submitted = st.form_submit_button('Recommend Me!')
            st.markdown('<br>', unsafe_allow_html=True)
            st.markdown('---', unsafe_allow_html=True)
            result_section = st.empty()
            if submitted : 
                result_section.empty()
                bar = st.progress(0)
                for i in range(100):
                    bar.progress(i + 1)
                    time.sleep(0.01)
                bar.empty()
            if submitted :
                with result_section.container():
                    col_hotel = col_hotel.lower()
                    if col_hotel == '':
                        st.error('Please enter a Hotel Name')
                    elif (data['Nama Hotel'].str.contains(col_hotel)).any():
                        st.markdown("""<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">Hi {} <span> 👋 </span></h1>""".format(col_name), unsafe_allow_html=True)
                        text_title_hasil = '<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">This is our recommendation</h1>'
                        st.markdown(text_title_hasil, unsafe_allow_html=True)
                        col_hotel = col_hotel.lower()
                    # st.write(col_hotel)
                        # Cari Index
                        similar_hotel = data.copy()
                        similar_hotel['Nama Hotel'] = similar_hotel['Nama Hotel'].str.lower()
                        hotel_similar_byuser = similar_hotel[similar_hotel['Nama Hotel']==col_hotel].index[0]
                        # Cari nilai cosine
                        hotel_mirip = list(enumerate(cosine[hotel_similar_byuser]))
                        sorted_hotel_similar = sorted(hotel_mirip, key=lambda x:x[1], reverse=True)
                        lima_hotel_similar = sorted_hotel_similar[:6]
                        list_index = []
                        for i in range(5):
                            list_index.append(lima_hotel_similar[i+1][0])
                        for i, idx in enumerate(list_index):
                            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
                            with col1:
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.image(data['Gambar'][idx], width=240)
                            with col2, col3:
                                # deskripsi = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description :</h4>'
                                # st.markdown(deskripsi, unsafe_allow_html=True)
                                st.markdown("""<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description </h4>""", unsafe_allow_html=True)
                                st.markdown("""<h5 style="font-family:Monospace; color:#000000; text-align:left;">{}</h5>""".format(data['Nama Hotel'][idx].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">{}</p>""".format(data['Nama Kota'][idx].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">Room Type: {}</p>""".format(data['Room Type'][idx].title()), unsafe_allow_html=True)
                            with col4:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:center;">Rating</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                st.markdown(f"""
                                        <h4 style="font-family:Monospace; color:#9401fd; text-align:center;">{data['Rating'][idx]}</h4>                                
                                        """,  unsafe_allow_html=True)
                            with col5:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Stars</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                if data['Stars'][idx] == 5:
                                    st.image('https://i.ibb.co/BVCn2Gh/stars.png', use_column_width='auto')    
                                elif data['Stars'][idx] == 4:
                                    st.image('https://cdn-icons-png.flaticon.com/512/3179/3179346.png', use_column_width='auto')
                                elif data['Stars'][idx] == 3:
                                    st.image('https://cdn-icons-png.flaticon.com/512/6713/6713718.png', use_column_width='auto')
                                elif data['Stars'][idx] == 2:
                                    st.image('https://cdn-icons-png.flaticon.com/128/3179/3179682.png', use_column_width='auto')
                                elif data['Stars'][idx] == 1:
                                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrFwo48zD0t73EuIeMpcc0plwPJLo9D6fvxg&usqp=CAU', use_column_width='auto')
                                else:
                                    st.write('Hotel tidak berbintang')
                            st.markdown('---')
                        st.markdown(titlemap, unsafe_allow_html=True)
                        map = folium.Map(location=[nama_kota.loc[nama_kota['Nama Kota']==data['Nama Kota'].iloc[lima_hotel_similar[0][0]]]['lat'], nama_kota.loc[nama_kota['Nama Kota']==data['Nama Kota'].iloc[lima_hotel_similar[0][0]]]['long']], zoom_start=10)
                        for i, idx in enumerate(list_index):
                            html=f"""
                            <h2 style="text-align: center;"><strong>{data['Nama Hotel'].loc[idx].title()}&nbsp;</strong></h2>
                            <p style="font-family:Monospace; font-size:20px"><strong>Alamat : <h3 style="font-family:Monospace">
                            {data['Alamat Hotel'].loc[idx]}
                            </h3></strong></p>
                            <p style="font-family:Monospace; font-size:20px"><strong>Fasilitas : <h3 style="font-family:Monospace">
                            {data['Deskripsi Room'].loc[idx]}
                            </h3></strong></p>
                            """
                        
                            iframe = folium.IFrame(html=html, width=400, height=300)
                            popup = folium.Popup(iframe, max_width=2560)
                            folium.Marker([data['lat'].loc[idx], data['long'].loc[idx]], popup=popup, icon=folium.Icon(icon='glyphicon-star')).add_to(map)

                        folium_static(map)

                    else :
                        st.error('Hotel tidak ditemukan')
        
    elif pilihan == "Based on City":
        with st.form(key='form_parameters'):
            # # Buat dictionary dari provinsi dan kota
            # pilihan_kota = {'provinsi' : data['Nama Provinsi'],
            #                 'kota' : data['Nama Kota'].drop_duplicates()}
            # # Buat dataframe dari dictionary
            # daftar_kota_provinsi = pd.DataFrame(pilihan_kota)
            # # Buat variabel data provinsi dari kolom provinsi dari data diatas
            # data_provinsi = daftar_kota_provinsi['provinsi'].drop_duplicates()
            # # with st.form(key='form_parameters'):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                col_name = st.text_input('Your name', '', key='name')
                # Buat selectbox untuk pilihan provinsi
                # pilih_provinsi = st.selectbox('Pilih Provinsi', data_provinsi.sort_values(ascending=True))
                # Buat dataframe untuk provinsi terpilih
                # if pilih_provinsi == pilih_provinsi:
                    # df1 = daftar_kota_provinsi.loc[daftar_kota_provinsi.provinsi==pilih_provinsi]
                    # Buat variabel penampung nama kota dari provinsi terpilih
                    # df2 = df1.kota.dropna().drop_duplicates()
                    # Buat select box untuk memilih kota
                pilih_kota = st.selectbox('Choose City', nama_kota['Nama Kota'].str.title().sort_values())
                sort = st.selectbox('Sort By', ['Rating', 'Stars'])
                st.markdown('<br>', unsafe_allow_html=True)
                submitted = st.form_submit_button('Recommend Me!')
            st.markdown('<br>', unsafe_allow_html=True)
            st.markdown('---', unsafe_allow_html=True)

            result_section = st.empty()
            if submitted : 
                result_section.empty()
                bar = st.progress(0)
                for i in range(100):
                    bar.progress(i + 1)
                    time.sleep(0.01)
                bar.empty()
            if submitted :
                with result_section.container():
                    basedoncity = data.copy()
                    basedoncity['Nama Kota']=basedoncity['Nama Kota'].str.lower()
                    basedoncity=basedoncity[basedoncity['Nama Kota']==pilih_kota.lower()]
                    if sort == 'Rating':
                        basedoncity = basedoncity.sort_values(by=['Rating', 'Stars'], ascending=False)
                    else:
                        basedoncity=basedoncity.sort_values(by=['Stars', 'Rating'],ascending=[False, False])
                    basedoncity.reset_index(drop=True, inplace=True)
                    panjang=len(basedoncity)
                    if(basedoncity.empty==True):
                        st.markdown("""<h2 style="font-family:Monospace; color:#9401fd; text-align:center;">Sorry, we can't recommend your hotel yet <span> 😣 </span>. Please adjust your search</h2>""".format(col_name), unsafe_allow_html=True)
                    elif panjang >= 5:
                        st.markdown("""<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">Hi {} <span> 👋 </span></h1>""".format(col_name), unsafe_allow_html=True)
                        text_title_hasil = '<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">This is our recommendation</h1>'
                        st.markdown(text_title_hasil, unsafe_allow_html=True)
                        for i, idx in basedoncity[:5].iterrows():
                            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
                            with col1:
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.image(basedoncity['Gambar'][i], width=240)
                            with col2, col3:
                                # deskripsi = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description :</h4>'
                                # st.markdown(deskripsi, unsafe_allow_html=True)
                                st.markdown("""<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description </h4>""", unsafe_allow_html=True)
                                st.markdown("""<h5 style="font-family:Monospace; color:#000000; text-align:left;">{}</h5>""".format(basedoncity['Nama Hotel'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">{}</p>""".format(basedoncity['Nama Kota'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">Room Type: {}</p>""".format(basedoncity['Room Type'][i].title()), unsafe_allow_html=True)
                            with col4:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:center;">Rating</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                st.markdown(f"""
                                        <h4 style="font-family:Monospace; color:#9401fd; text-align:center;">{basedoncity['Rating'][i]}</h4>                                
                                        """,  unsafe_allow_html=True)
                            with col5:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Stars</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                if basedoncity['Stars'][i] == 5:
                                    st.image('https://i.ibb.co/BVCn2Gh/stars.png', use_column_width='auto')    
                                elif basedoncity['Stars'][i] == 4:
                                    st.image('https://cdn-icons-png.flaticon.com/512/3179/3179346.png', use_column_width='auto')
                                elif basedoncity['Stars'][i] == 3:
                                    st.image('https://cdn-icons-png.flaticon.com/512/6713/6713718.png', use_column_width='auto')
                                elif basedoncity['Stars'][i] == 2:
                                    st.image('https://cdn-icons-png.flaticon.com/128/3179/3179682.png', use_column_width='auto')
                                elif basedoncity['Stars'][i] == 1:
                                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrFwo48zD0t73EuIeMpcc0plwPJLo9D6fvxg&usqp=CAU', use_column_width='auto')
                                else:
                                    st.write('Hotel tidak berbintang')
                            st.markdown('---')
                        st.markdown(titlemap, unsafe_allow_html=True)
                        map = folium.Map(location=[nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['lat'], nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['long']], zoom_start=10)
                        for i, idx in basedoncity[:5].iterrows():
                            html=f"""
                            <h2 style="text-align: center;"><strong>{basedoncity['Nama Hotel'].loc[i].title()}&nbsp;</strong></h2>
                            <p style="font-family:Monospace; font-size:20px"><strong>Alamat : <h3 style="font-family:Monospace">
                            {basedoncity['Alamat Hotel'].loc[i]}
                            </h3></strong></p>
                            <p style="font-family:Monospace; font-size:20px"><strong>Fasilitas : <h3 style="font-family:Monospace">
                            {basedoncity['Deskripsi Room'].loc[i]}
                            </h3></strong></p>
                            """
                        
                            iframe = folium.IFrame(html=html, width=400, height=300)
                            popup = folium.Popup(iframe, min_height=400,max_width=2560)
                            folium.Marker([basedoncity['lat'].loc[i], basedoncity['long'].loc[i]], popup=popup, icon=folium.Icon(icon='glyphicon-star') ).add_to(map)

                        folium_static(map)
                    elif panjang < 5:
                        st.markdown("""<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">Hi {} <span> 👋 </span></h1>""".format(col_name), unsafe_allow_html=True)
                        text_title_hasil = '<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">This is our recommendation</h1>'
                        st.markdown(text_title_hasil, unsafe_allow_html=True)
                        for i, idx in basedoncity.iterrows():
                            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
                            with col1:
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.image(basedoncity['Gambar'][i], width=240)
                            with col2, col3:
                                # deskripsi = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description :</h4>'
                                # st.markdown(deskripsi, unsafe_allow_html=True)
                                st.markdown("""<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description </h4>""", unsafe_allow_html=True)
                                st.markdown("""<h5 style="font-family:Monospace; color:#000000; text-align:left;">{}</h5>""".format(basedoncity['Nama Hotel'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">{}</p>""".format(basedoncity['Nama Kota'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">Room Type: {}</p>""".format(basedoncity['Room Type'][i].title()), unsafe_allow_html=True)
                            with col4:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:center;">Rating</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                st.markdown(f"""
                                        <h4 style="font-family:Monospace; color:#9401fd; text-align:center;">{basedoncity['Rating'][i]}</h4>                                
                                        """,  unsafe_allow_html=True)
                            with col5:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Stars</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                if basedoncity['Stars'][i] == 5:
                                    st.image('https://i.ibb.co/BVCn2Gh/stars.png', use_column_width='auto')    
                                elif basedoncity['Stars'][i] == 4:
                                    st.image('https://cdn-icons-png.flaticon.com/512/3179/3179346.png', use_column_width='auto')
                                elif basedoncity['Stars'][i] == 3:
                                    st.image('https://cdn-icons-png.flaticon.com/512/6713/6713718.png', use_column_width='auto')
                                elif basedoncity['Stars'][i] == 2:
                                    st.image('https://cdn-icons-png.flaticon.com/128/3179/3179682.png', use_column_width='auto')
                                elif basedoncity['Stars'][i] == 1:
                                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrFwo48zD0t73EuIeMpcc0plwPJLo9D6fvxg&usqp=CAU', use_column_width='auto')
                                else:
                                    st.write('Hotel tidak berbintang')
                            st.markdown('---')
                        st.markdown(titlemap, unsafe_allow_html=True)
                        map = folium.Map(location=[nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['lat'], nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['long']], zoom_start=10)
                        for i, idx in basedoncity.iterrows():
                            html=f"""
                            <h2 style="text-align: center;"><strong>{basedoncity['Nama Hotel'].loc[i].title()}&nbsp;</strong></h2>
                            <p style="font-family:Monospace; font-size:20px"><strong>Alamat : <h3 style="font-family:Monospace">
                            {basedoncity['Alamat Hotel'].loc[i]}
                            </h3></strong></p>
                            <p style="font-family:Monospace; font-size:20px"><strong>Fasilitas : <h3 style="font-family:Monospace">
                            {basedoncity['Deskripsi Room'].loc[i]}
                            </h3></strong></p>
                            """
                        
                            iframe = folium.IFrame(html=html, width=400, height=300)
                            popup = folium.Popup(iframe, max_width=2560)
                            folium.Marker([basedoncity['lat'].loc[i], basedoncity['long'].loc[i]], popup=popup, icon=folium.Icon(icon='glyphicon-star') ).add_to(map)

                        folium_static(map)
    else: # Based on preference
        with st.form(key='form_parameters'):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                col_name = st.text_input('Your Name')
                col_ratings = st.slider('Minimum Rating', 0.0, 5.0, 4.0)
                col_stars = st.slider('Stars', 1, 5, 3)
                col_type_room = st.selectbox('Room Type', ['Standard', 'Deluxe', 'Superior', 'Suite', 'Villa', 'Anything'])
                pilih_kota = st.selectbox('Choose city', nama_kota['Nama Kota'].str.title())
                st.markdown('<br>', unsafe_allow_html=True)
                submitted = st.form_submit_button('Recommend Me!')
            st.markdown('<br>', unsafe_allow_html=True)
            st.markdown('---', unsafe_allow_html=True)
            result_section = st.empty()


            if submitted : 
                result_section.empty()
                bar = st.progress(0)
                for i in range(100):
                    bar.progress(i + 1)
                    time.sleep(0.01)
                bar.empty()
            if submitted :
                with result_section.container():
                    basedonpreference = data.copy()
                    basedonpreference['Nama Kota']=basedonpreference['Nama Kota'].str.lower()
                    basedonpreference=basedonpreference[basedonpreference['Nama Kota']==pilih_kota.lower()]
                    if col_type_room != 'Anything':
                        basedonpreference=basedonpreference[basedonpreference['Room Type']==col_type_room]
                    else:
                        basedonpreference=basedonpreference
                    # if col_type_room == 'Anything':
                    #     citybase=citybase[(citybase['Nama Kota']==city.lower()) & (citybase['Rating']>=number) & (citybase['Stars']==stars)]
                    # else:
                    #     citybase=citybase[(citybase['Nama Kota']==city.lower()) & (citybase['Rating']>=number) & (citybase['Stars']== stars) & (citybase['Room Type']==room_type.lower())]
                    basedonpreference=basedonpreference[basedonpreference['Rating']>=col_ratings]
                    basedonpreference=basedonpreference[basedonpreference['Stars']==col_stars]
                    basedonpreference=basedonpreference.sort_values(by=['Rating', 'Stars'], ascending=False)
                    basedonpreference.reset_index(drop=True, inplace=True)
                    panjang=len(basedonpreference)
                    if(basedonpreference.empty==True):
                        st.markdown("""<h2 style="font-family:Monospace; color:#9401fd; text-align:center;">Sorry {}, we can't recommend your hotel yet <span> 😣 </span> <br>Please adjust your search</br></h2>""".format(col_name), unsafe_allow_html=True)
                    elif panjang >= 5:
                        st.markdown("""<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">Hi {} <span> 👋 </span></h1>""".format(col_name), unsafe_allow_html=True)
                        text_title_hasil = '<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">This is our recommendation</h1>'
                        st.markdown(text_title_hasil, unsafe_allow_html=True)
                        for i, idx in basedonpreference[:5].iterrows():
                            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
                            with col1:
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.image(basedonpreference['Gambar'][i], width=240)
                            with col2, col3:
                                # deskripsi = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description :</h4>'
                                # st.markdown(deskripsi, unsafe_allow_html=True)
                                st.markdown("""<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description </h4>""", unsafe_allow_html=True)
                                st.markdown("""<h5 style="font-family:Monospace; color:#000000; text-align:left;">{}</h5>""".format(basedonpreference['Nama Hotel'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">{}</p>""".format(basedonpreference['Nama Kota'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">Room Type: {}</p>""".format(basedonpreference['Room Type'][i].title()), unsafe_allow_html=True)
                            with col4:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:center;">Rating</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                st.markdown(f"""
                                        <h4 style="font-family:Monospace; color:#9401fd; text-align:center;">{basedonpreference['Rating'][i]}</h4>                                
                                        """,  unsafe_allow_html=True)
                            with col5:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Stars</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                if basedonpreference['Stars'][i] == 5:
                                    st.image('https://i.ibb.co/BVCn2Gh/stars.png', use_column_width='auto')    
                                elif basedonpreference['Stars'][i] == 4:
                                    st.image('https://cdn-icons-png.flaticon.com/512/3179/3179346.png', use_column_width='auto')
                                elif basedonpreference['Stars'][i] == 3:
                                    st.image('https://cdn-icons-png.flaticon.com/512/6713/6713718.png', use_column_width='auto')
                                elif basedonpreference['Stars'][i] == 2:
                                    st.image('https://cdn-icons-png.flaticon.com/128/3179/3179682.png', use_column_width='auto')
                                elif basedonpreference['Stars'][i] == 1:
                                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrFwo48zD0t73EuIeMpcc0plwPJLo9D6fvxg&usqp=CAU', use_column_width='auto')
                                else:
                                    st.write('Hotel tidak berbintang')
                            st.markdown('---')
                        st.markdown(titlemap, unsafe_allow_html=True)
                        f = folium.Figure(width=1600, height=43)
                        map = folium.Map(location=[nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['lat'], nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['long']], zoom_start=10)
                        for i, idx in basedonpreference[:5].iterrows():
                            html=f"""
                            <h2 style="text-align: center;"><strong>{basedonpreference['Nama Hotel'].loc[i].title()}&nbsp;</strong></h2>
                            <p style="font-family:Monospace; font-size:20px"><strong>Alamat : <h3 style="font-family:Monospace">
                            {basedonpreference['Alamat Hotel'].loc[i]}
                            </h3></strong></p>
                            <p style="font-family:Monospace; font-size:20px"><strong>Fasilitas : <h3 style="font-family:Monospace">
                            {basedonpreference['Deskripsi Room'].loc[i]}
                            </h3></strong></p>
                            """
                        
                            iframe = folium.IFrame(html=html, width=400, height=300)
                            popup = folium.Popup(iframe, max_width=2560)
                            folium.Marker([basedonpreference['lat'].loc[i], basedonpreference['long'].loc[i]], popup=popup, icon=folium.Icon(icon='glyphicon-star') ).add_to(map)

                        folium_static(map)
                    elif panjang < 5:
                        st.markdown("""<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">Hi {} <span> 👋 </span></h1>""".format(col_name), unsafe_allow_html=True)
                        text_title_hasil = '<h1 style="font-family:Monospace; color:#9401fd; text-align:center;">This is our recommendation</h1>'
                        st.markdown(text_title_hasil, unsafe_allow_html=True)
                        for i, idx in basedonpreference[:5].iterrows():
                            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
                            with col1:
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.image(basedonpreference['Gambar'][i], width=240)
                            with col2, col3:
                                # deskripsi = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description :</h4>'
                                # st.markdown(deskripsi, unsafe_allow_html=True)
                                st.markdown("""<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Description </h4>""", unsafe_allow_html=True)
                                st.markdown("""<h5 style="font-family:Monospace; color:#000000; text-align:left;">{}</h5>""".format(basedonpreference['Nama Hotel'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">{}</p>""".format(basedonpreference['Nama Kota'][i].title()), unsafe_allow_html=True)
                                st.markdown("""<p style="font-family:Monospace; color:#000000; text-align:justify;">Room Type: {}</p>""".format(basedonpreference['Room Type'][i].title()), unsafe_allow_html=True)
                            with col4:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:center;">Rating</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                st.markdown(f"""
                                        <h4 style="font-family:Monospace; color:#9401fd; text-align:center;">{basedonpreference['Rating'][i]}</h4>                                
                                        """,  unsafe_allow_html=True)
                            with col5:
                                rating = '<h4 style="font-family:Monospace; color:#9401fd; text-align:left;">Stars</h4>'
                                st.markdown(rating, unsafe_allow_html=True)
                                if basedonpreference['Stars'][i] == 5:
                                    st.image('https://i.ibb.co/BVCn2Gh/stars.png', use_column_width='auto')    
                                elif basedonpreference['Stars'][i] == 4:
                                    st.image('https://cdn-icons-png.flaticon.com/512/3179/3179346.png', use_column_width='auto')
                                elif basedonpreference['Stars'][i] == 3:
                                    st.image('https://cdn-icons-png.flaticon.com/512/6713/6713718.png', use_column_width='auto')
                                elif basedonpreference['Stars'][i] == 2:
                                    st.image('https://cdn-icons-png.flaticon.com/128/3179/3179682.png', use_column_width='auto')
                                elif basedonpreference['Stars'][i] == 1:
                                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrFwo48zD0t73EuIeMpcc0plwPJLo9D6fvxg&usqp=CAU', use_column_width='auto')
                                else:
                                    st.write('Hotel tidak berbintang')
                            st.markdown('---')
                        st.markdown(titlemap, unsafe_allow_html=True)
                        map = folium.Map(location=[nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['lat'], nama_kota.loc[nama_kota['Nama Kota']==pilih_kota]['long']], zoom_start=10)
                        for i, idx in basedonpreference.iterrows():
                            html=f"""
                            <h2 style="text-align: center;"><strong>{basedonpreference['Nama Hotel'].loc[i].title()}&nbsp;</strong></h2>
                            <p style="font-family:Monospace; font-size:20px"><strong>Alamat : <h3 style="font-family:Monospace">
                            {basedonpreference['Alamat Hotel'].loc[i]}
                            </h3></strong></p>
                            <p style="font-family:Monospace; font-size:20px"><strong>Fasilitas : <h3 style="font-family:Monospace">
                            {basedonpreference['Deskripsi Room'].loc[i]}
                            </h3></strong></p>
                            """
                        
                            iframe = folium.IFrame(html=html, width=400, height=300)                            
                            popup = folium.Popup(iframe, max_width=2560)
                            folium.Marker([basedonpreference['lat'].loc[i], basedonpreference['long'].loc[i]], popup=popup, icon=folium.Icon(icon='glyphicon-star') ).add_to(map)

                        folium_static(map)

else:
    opener = 'gambar'
    if opener == 'gambar':
        gif1 = '<div style="width:100%; display:flex; justify-content:center; align-items:center"><iframe allow="fullscreen" frameBorder="0" height="400" src="https://i.ibb.co/yhq6s4y/clickspacee.png" width="1440"></iframe></div>'
        st.markdown(gif1, unsafe_allow_html=True)

    st.markdown('<br><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([.8, 1, 1])
    with col1:
        st.write(' ')

    with col2:
        st.image('https://i.ibb.co/7NvYR8K/clickspace-logo.png', width=300)

    with col3:
        st.write(' ')
    this_page = '<h2 style="font-family:Monospace; color:#9401fd; text-align:center;">💸 Budget prediction page 💸</h2>'
    st.markdown(this_page, unsafe_allow_html=True)
    isi_this_page = '<h4 style="font-family:Monospace; color:#000000; text-align:justify;">ClickSpace makes it simple for those of you who want to know the price range that must be spent when selecting a hotel or lodge; depending on the hotel details you enter, we will deliver the appropriate budget amount.</h4>'
    st.markdown(isi_this_page, unsafe_allow_html=True)
    nama_hotel_prediksi = data_hotel_price['Nama Hotel'].apply(lambda x: x.title())
    data_hotel_price['Nama Hotel'] = data_hotel_price['Nama Hotel'].apply(lambda x: x.title())
    st.markdown('</br>', unsafe_allow_html=True)
    # Predict price hotel
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        Nama_Hotel = st.selectbox('Choose hotel : ', nama_hotel_prediksi)
        st.markdown("""<h5 style="font-family:Monospace; color:#000000; text-align:left;">Hotel location :</h5>""", unsafe_allow_html=True)
        Provinsi = data_hotel_price['Provinsi'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0]
        Nama_Kota = data_hotel_price['Nama Kota'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel].values[0]
        st.write(Provinsi)
        st.write(Nama_Kota)
    with st.form(key='form_parameters'):

        with col2:
            Luas_Kamar = st.number_input("Room size (m2)", step=1, min_value=15, max_value=1000)
            Kapasitas = st.number_input("Guest Capacity", step=1, min_value=1, max_value=100)

        with col3:
            Rating = st.number_input("Rating", step=.01, min_value=4.00, max_value=5.00)
        

        col1, col2, col3 = st.columns([3, 1, 3])
        with col2:
            submitted = st.form_submit_button('Budget Predict')
            
    if submitted:
        data_price = {'Nama Hotel' : Nama_Hotel,
        'Nama Kota' : Nama_Kota,
        'Provinsi' : Provinsi,
        'Luas Kamar' : Luas_Kamar,
        'Kapasitas' : Kapasitas,
        'Rating' : Rating}

# URL = "http://127.0.0.1:5000/price_hotel" # sebelum push backend
        URL = "https://backend-price-hotel.herokuapp.com/price_hotel"
        # communication
        r = requests.post(URL, json=data_price)
        res = r.json()
        # if r.status_code == 200:
        if submitted:
            prediction = res['prediction']
            hasil1 = '<h2 style="font-family:Monospace; color:#9401fd; text-align:center;">We predict that it will cost you around :</h2>'
            st.markdown(hasil1, unsafe_allow_html=True)
            hasil2 = '<h2 style="font-family:Monospace; color:#000000; text-align:center;">Rp {}</h2>'.format(round(prediction))
            st.markdown(hasil2, unsafe_allow_html=True)
            map = folium.Map(location=[data_hotel_price['Latitude'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0], data_hotel_price['Longitude'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0]], zoom_start=12)
            html=f"""
            <h2 style="text-align: center;"><strong>{data_hotel_price['Nama Hotel'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0]}&nbsp;</strong></h2>
            <p style="font-family:Monospace; font-size:20px"><strong>Provinsi : <h3 style="font-family:Monospace">
            {data_hotel_price['Provinsi'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0]}
            </h3></strong></p>
            <p style="font-family:Monospace; font-size:20px"><strong>Kota : <h3 style="font-family:Monospace">
            {data_hotel_price['Nama Kota'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0]}
            </h3></strong></p>
            """             
            iframe = folium.IFrame(html=html, width=400, height=300)
            popup = folium.Popup(iframe, max_width=2560)
            folium.Marker([data_hotel_price['Latitude'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0], data_hotel_price['Longitude'].loc[data_hotel_price['Nama Hotel']==Nama_Hotel.title()].values[0]], popup=popup, icon=folium.Icon(icon='glyphicon-star')).add_to(map)
            folium_static(map)
            

# def set_bg_hack_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp{{
#              background: url(data:image/jpeg;base64,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);
#              background-repeat: no-repeat;
#              background-size: 2650px 2280px;
#              background-position: center;
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )
# set_bg_hack_url()

# map = folium.Map(location=[-6.2088, 106.8456], zoom_start=10)
# html=f"""
#         <h2>Apa aelah</h2>
#         <p style="font-family:Monospace; font-size:20px">Alamat:</p> 
#         <ul style="font-family:Monospace">
#         Jl. Raya Cikarang No.1
#         </ul>
#         </p>
#         """
    
# iframe = folium.IFrame(html=html, width=300, height=210)
# popup = folium.Popup(iframe, max_width=350)
# folium.Marker([-6.2088, 106.8456], popup=popup ).add_to(map)
# st_data = st_folium(map, width=350, height=600)
