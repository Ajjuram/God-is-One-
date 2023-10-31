import streamlit as st
from PIL import Image
st.set_page_config(page_title="Aum Namah Shivay",page_icon=":tada:",layout="wide")

Hanuman_ji =Image.open("hanuman ji.jpg")
Arjun_ji= Image.open("Arjun.jpg")
bhagvan_shiv=Image.open("bhagvan_shiv.jpg")
shivji_new=Image.open("shivji_new.jpg")
main_image= Image.open("God is One photo.png")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
# Header Section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        # css = """
        # <style>
        # [data-testid="stAppViewContainer"]{
        #     background-image: url('https://yt3.ggpht.com/ytc/APkrFKb_hyYEPR7L6eVCVwHInw3LsvtGYzjp6Z1hWXHtmQ=s600-c-k-c0x00ffffff-no-rj-rp-mo');
        #     background-size: 1800px 1000px;
        #     color: black;
        # }
        # </style>
        # """
        # st.markdown(css, unsafe_allow_html=True)
        st.title("God is One and Supreme Truth")
        st.write("@GodisOneandSupremeTruth")
        st.subheader("'ॐ नमः शिवाय'")
        st.header("Hi, I am Ajay :wave:")
        st.subheader("The Owner of this Youtube Channel")
        st.markdown(
            f'<style>{open("custom.css").read()}</style>',
            unsafe_allow_html=True
        )
        st.write("[Youtube Channel >](https://www.youtube.com/c/GodisOneandSupremeTruth)")
    with right_column:
        st.image(main_image.resize((1600,800)))
        # resized_image= main_image.resize((200,100))
        # resized_image.save("new_image.jpg")
        # resized_image.show()


# What I do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##") # To give space between two lines
        st.write("""
        Hello, I am a follower of the path of God and i created a YouTube channel to promote Righteousness, Devotion and The knowledge related to God (Generator Operator and Destroyer).
        \n In this Youtube Channel you will find Devotional songs, Chanting Mantras, Motivational and Whatsapp status, Religious T.V. Serials like Shri Krishna, Mahabharata and Ramayana videos, so stay with us.

        \n If you like our videos then please Like, Share our videos and Subscribe to the Channel.
        """)

    with right_column:
        # st.write("""
        # chjhcjhd""")
        st.empty()
with st.container():
    st.write("---")
    st.header('My Projects')
    st.write('##') # "##": This is a string that represents a Markdown header. In Markdown, "##" signifies a level 2 (h2) header
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Hanuman_ji)
        st.image(Arjun_ji)
        st.image(bhagvan_shiv)
        st.image(shivji_new)
    with text_column:
        st.subheader("Jab Hanuman Ji Ne Apna Sina Chir Kar Dikhaya | Hanuman Movie Scene")
        st.write("""
        Jab Hanuman Ji Ne Apna Sina Chir Kar Dikhaya | 'Hanuman' Movie Scene
        """)
        st.write("[Watch Video...](https://youtu.be/2EOZjG8Xnv4)")
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.subheader("Arjun Status | Arjun Dialogue Status | Mahabharat Status Video | Whatsapp Status Video")
        st.write("""
                Arjun Status | Arjun Dialogue Status | Mahabharat Status Video | Whatsapp Status Video
                """)
        st.write("[Watch Video...](https://youtu.be/2bKPmU1ROiI)")
        st.write('##')
        st.write('##')
        st.write('##')
        st.subheader("Ajar Amar Shiv Shankar Song | Somnath Shiv Ji | Om Namah Shivay serial")
        st.write("""
                        Ajar Amar Shiv Shankar Song | Somnath Shiv Ji | Om Namah Shivay serial
                        """)
        st.write("[Watch Video...](https://youtu.be/IRULSFBzN5E)")
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.subheader("Hey Shiv Shankar Tripurari | Lord Shiva Song | Devotional Song | Peaceful Song")
        st.write("""
                                Hey Shiv Shankar Tripurari | Lord Shiva Song | Devotional Song | Peaceful Song
                                """)
        st.write("[Watch Video...](https://youtu.be/mtlFofkIMIY)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")
    contact_form = """  
    <form action="https://formsubmit.co/ajay.tamak321@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """ # Html code

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
