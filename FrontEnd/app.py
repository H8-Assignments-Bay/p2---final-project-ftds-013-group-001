import json
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu #pip install streamlit-option-menu
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# API coinmarketcap coba coba
# url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#     'start':'1',
#     'limit':'5000',
#     'convert':'USD'
# }
# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
# }
# session = Session()
# session.headers.update(headers)

# try:
#     response = session.get(url, params=parameters)
#     data = json.loads(response.text)
#     print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#     print(e)


pageicon = Image.open('Meta.png')
home1=Image.open('home6.png')
home2=Image.open('home7.png')
home3=Image.open('home9.png')


st.set_page_config(
    page_title="MetaBlock!",
    page_icon=pageicon,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/rahmad07g',
        'Report a bug': "https://www.google.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

header = Image.open('Meta-Head.jpg')
header2 = Image.open('header2.png')
# header2 = header2.resize((1300,300))
st.image('Meta-Head.jpg', use_column_width=True)
st.subheader('Metablok adalah sebuah aplikasi sistem rekomendasi trading aset kripto untuk token Metaverse, berdasarkan profile resiko user (Low, Medium, High).')
st.write('-----')

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home','Profile Risk','Rekomendasi Aset Kripto'],
        icons=['house','app','currency-bitcoin'],
        menu_icon='cast',
        default_index=0,       
    )
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
            
    lottie_anim1 = load_lottiefile("anim1.json")
    st_lottie(
        lottie_anim1,height=300,width=300)
    
if selected == 'Home':
    
    st.markdown ('''# **Meta Coin Price App**
    A Simple Cryptocurrency price app puling price data from coin marketcap API
    ''')

    st.header('**Selected Price**')
    
    # Load market data from Binance API
    df = pd.read_json('24hr.json')

    # Widget (Cryptocurrency selection box)
    st.subheader('Silahkan Input Coin yang ingin dicari!')
    text1=''
    text2=''
    text3=''

    with st.form('Cari'):
      col1, col2, col3 = st.columns(3)
      with col1:
          col1_selection = st.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
      with col2:
          col2_selection = st.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
      with col3:
          col3_selection = st.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )
      col1, col2, col3 = st.columns(3)
      st.form_submit_button('Cari')
            
    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    col1, col2, col3 = st.columns(3)

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]
    col2_df = df[df.symbol == col2_selection]
    col3_df = df[df.symbol == col3_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)
    col2_price = round_value(col2_df.weightedAvgPrice)
    col3_price = round_value(col3_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    col2_percent = f'{float(col2_df.priceChangePercent)}%'
    col3_percent = f'{float(col3_df.priceChangePercent)}%'
 
    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    col2.metric(col2_selection, col2_price, col2_percent)
    col3.metric(col3_selection, col3_price, col3_percent)

    st.header('**All Price**')
    st.dataframe(df)
    
    st.markdown("""
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)
          
    st.image(header2)
    # st.write('----')
    st.subheader('Kami Terintegrasi dengan Platform ........ ')
    st.write(' .....................')
 
    # st.button('Lihat Partner Kami')
    st.button('Further Improvement')
    st.write('-------')

    st.header('Trading Bot!')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(home1, use_column_width=True)
    with col2:
        st.image(home2, use_column_width=True)
    with col3:
        st.image(home3, use_column_width=True)

elif selected == 'Profile Risk':
    st.subheader('Profile Risk')
    st.write('''Sebelum memulai bertransaksi Cryptocurrency (Trading), alangkah baiknya mengetahui tujuan anda dalam bertransaksi,jangka waktu trading dan profil risiko anda, 
                merupakan alat bantu bagi Anda untuk mengetahui tingkat toleransi risiko Anda dalam bertransaksi.
                Dari hasil pengisian kuesioner berikut ini, Pengguna dapat kemudian menentukan token apa yang sesuai dan diharapkan dapat secara optimal 
                memenuhi kebutuhan untuk mencapai tujuan keuangan anda.Luangkan waktu Anda sekitar 3-5 menit untuk mengisi kuesioner profil risiko berikut dengan 
                memilih jawaban yang Anda anggap paling tepat''')
    with st.form('Profile'):
      col1, col2, col3 = st.columns(3)
      with col1:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
        st_lottie(
            lottie_hello,height=300,width=300)
      with col2:
          text1 = st.text_input('Nama User')
      with col3:
          num1 = st.number_input('Usia',min_value=17)
                    
      col1, col2 = st.columns(2)
      with col1: # ini untuk kolom 1
        # daftar pertanyaan
        question1 = {1:'Tidak mengetahui sama sekali',2:'Tidak terlalu familiar dengan cryptocurrency',3:
            'Sedikit mengetahui, namun tidak sepenuhnya paham dengan pergerakan harganya',5:'Cukup paham, dan mengetahui faktor pergerakan harga',
            7:'Sangat paham dan sering melakukan transaksi dan riset/menggali informasi untuk jual-beli'}
        question3 = {1:'Hanya 1 Kali dalam Seminggu',3:'2 – 5 Kali Seminggu ',5:'Setiap Hari'}    
        question5 = {1:'Saya tidak bersedia untuk menerima kerugian',2:'Saya bersedia menerima kerugian secara minimal (1–5%)',
        3:'Saya bersedia untuk mengalami kerugian secara moderat (>5-30%)',5:'Saya bersedia untuk mengalami kerugian yang cukup signiﬁkan >30%'}   
        question7 =  {3:'Jual segera, agar tidak mengalami kerugian yang lebih besar',1:'Tidak melakukan apapun karena anda merasa nilainya akan naik kembali',
        2:'Memasukan lebih banyak uang saat nilainya turun, karena ini merupakan kesempatan'}

        # function setiap pertanyaan
        def format_func(option):
            return question1[option]
        option = st.selectbox("Pertanyaan 1 : Seberapa paham anda mengenai cryptocurrency terutama token metaverse?", options=list(question1.keys()), format_func=format_func)

        def format_func3(option3):
            return question3[option3]
        option3 = st.selectbox('Pertanyaan 3 : Dalam bertransaksi (Trading) seberapa seringkah anda melakukan kegiatan jual-beli?', options=list(question3.keys()), format_func=format_func3)
        
        def format_func5(option5):
            return question5[option5]
        option5 = st.selectbox('Pertanyaan 5 : Setiap kegiatan transaksi jual-beli dapat mengalami kenaikan maupun penurunan. Secara umum, berapa banyak kerugian yang dapat Anda terima dalam rangka mencapai tingkat pengembalian yang Anda harapkan?', options=list(question5.keys()), format_func=format_func5)
                
        def format_func7(option7):
            return question7[option7]
        option7 = st.selectbox('Pertanyaan 7 : Jika transaksi yang dilakukan (trading) anda, mengalami kerugian, apa yang akan anda lakukan?', options=list(question7.keys()), format_func=format_func7)
        
      with col2: # kolom 2
        question2 =  {5:'Saya hanya trading (jangka pendek) ', 3:'Saya trading dan juga berinvestasi ', 1:'Saya hanya berinvestasi (jangka panjang)'}  
        question4 =  {1:'0 - 10%', 3:'Antara 10 dan 50%' , 5:'Di atas 50%'} 
        question6 =  {1:'0-5% (Setara Bunga Deposito)', 3:'>5-15%' , 5:'15-30%', 7:'>30%'}  
        question8 =  {1:'Risiko Rendah', 3:'Risiko Sedang' , 5:'Risiko Tinggi'}
      
        # function setiap pertanyaan
        def format_func2(option2):
            return question2[option2]
        option2 = st.selectbox('Pertanyaan 2 : Apakah anda seorang Trader atau Investor?', options=list(question2.keys()), format_func=format_func2)
      
        def format_func4(option4):
            return question4[option4]
        option4 = st.selectbox('Pertanyaan 4 : Dalam bertransaksi selalu ada potensi kerugian. Berapakah porsi dari total kekayaan Anda yang dapat Anda sisihkan untuk trading?', options=list(question4.keys()), format_func=format_func4)

        def format_func6(option6):
            return question6[option6]
        option6 = st.selectbox('Pertanyaan 6 : Secara Kumulatif, Berapakah tingkat pengembalian (return) yang anda harapkan dalam setiap tahunnya?', options=list(question6.keys()), format_func=format_func6)
        
        def format_func8(option8):
            return question8[option8]
        option8 = st.selectbox('Pertanyaan Terakhir : Seberapa besar tingkat risiko yang Anda ambil dalam keputusan pengelolaan keuangan anda di masa lalu?', options=list(question8.keys()), format_func=format_func8)


      if st.form_submit_button('Submit'):
        st.write('----')

        # INI hanya untuk fitur mengambil value pada setiap jawaban yang dipilih        
        # st.write(f"You selected option {option} called {format_func(option)}")
        # st.write(f"You selected option {option2} called {format_func2(option2)}")
        # st.write(f"You selected option {option3} called {format_func3(option3)}")
        # st.write(f"You selected option {option4} called {format_func4(option4)}")
        # st.write(f"You selected option {option5} called {format_func5(option5)}")
        # st.write(f"You selected option {option6} called {format_func6(option6)}")
        # st.write(f"You selected option {option7} called {format_func7(option7)}")
        # st.write(f"You selected option {option8} called {format_func8(option8)}")
        
    # Identifikasi Risk Profile Customer
    # Kelas Risiko (8-19 (Low) Rendah, 19-30 Moderate (Medium), 31-42 (High))
    skor = (option + option2 + option3 + option4 + option5 + option6 +option7 +option8)
    st.write(skor)
    if skor < 19:
        st.subheader('Profile Risk Pengguna')
        st.write(f"Hai {text1} Anda Merupakan Pengguna Dengan profil risiko Rendah, stabil Biasanya para investor pemula yang baru tertarik untuk investasi termasuk ke dalam tipe konservatif") 
        col4, col5 = st.columns(2)
        with col4:
            col4.metric("----", "Rendah", "Anda disarankan pada token yang cenderung stabil, dan volatilitas yang rendah") # akan dibuat otomatis, hanya tester tampilan
        with col5:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_okbkcby3.json")
            st_lottie(
                lottie_hello,height=400,width=400)
    elif 19<=skor<=30:
        st.subheader('Profile Risk Pengguna')
        st.write(f"Hai {text1} Anda Merupakan Pengguna Dengan profil risiko Medium/Moderate, stabil Biasanya para investor pemula yang baru tertarik untuk investasi termasuk ke dalam tipe konservatif") 
        col4, col5 = st.columns(2)
        with col4:
            col4.metric("----", "Sedang", "Anda disarankan untuk memilih token yang ") # akan dibuat otomatis, hanya tester tampilan
        with col5:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_okbkcby3.json")
            st_lottie(
                lottie_hello,height=400,width=400)
    else:
        st.subheader('Profile Risk Pengguna')
        st.write(f"Hai {text1} Anda Merupakan Pengguna Dengan profil risiko Tinggi/Agresif,adalah investor yang sudah berpengalaman. Tipe investor agresif tidak takut investasi pokoknya berkurang atau hilang demi imbal hasil yang tinggi.Investor agresif sudah terbiasa terhadap fluktuasi harga pasar modal yang ekstrim. Reksadana saham, saham dan crypto merupakan beberapa pilihan yang cocok untuk investor agresif") 
        col4, col5 = st.columns(2)
        with col4:
            col4.metric("----", "Tinggi", "Anda cocok terhadap token-token yang memiliki volatilitas tinggi untuk mendapatkan keuntungan yang maksimal") # akan dibuat otomatis, hanya tester tampilan
        with col5:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_okbkcby3.json")
            st_lottie(
                lottie_hello,height=400,width=400)

    Low = '''Tipe investor yang memilih profil risiko investasi paling rendah atau bahkan tidak ada risiko sama sekali. 
             Investor konservatif menyukai jenis investasi yang nilainya stabil. Biasanya para investor pemula yang baru tertarik untuk investasi termasuk ke dalam tipe konservatif'''
             
    Medium = '''Profil risiko moderat adalah investor yang berani mengambil risiko sedang. Tipe investor moderat sudah berani mengambil risiko besar, namun tetap berhati-hati dalam memilih instrumen investasi. 
            Biasanya seorang investor moderat tidak langsung mencairkan dana investasi saat terjadi penurunan nilai. '''
             
    High = '''Investor agresif adalah investor yang berani menghadapi risiko investasi tinggi. Biasanya investor yang seperti ini adalah investor yang sudah berpengalaman. Tipe investor agresif tidak takut investasi pokoknya berkurang atau hilang demi imbal hasil yang tinggi. 
            Investor agresif sudah terbiasa terhadap fluktuasi harga pasar modal yang ekstrim. Reksadana saham, saham dan crypto merupakan beberapa pilihan yang cocok untuk investor agresif. '''
             
else:
    page3 = Image.open('token.png')
    st.image(page3, use_column_width=True)
    # st.header('>>Kami berikan rekomendasi token kripto sesuai profile risk anda')
    st.subheader('Rekomendasi Aset Kripto')
    # st.write('----')
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    col6, col7, col8 = st.columns(3)
    col6.metric("Low Risk", "Axie", "8%") # akan dibuat otomatis, hanya tester tampilan
    col7.metric("Low Risk", "Sand Box", "4%") #
    col8.metric("Low Risk", "Ape Coin", "15.5%") #
st.write('----')

