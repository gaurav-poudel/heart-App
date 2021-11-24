import streamlit as st 
from ml import ml
from PIL import Image
from aboutme import aboutme

def main():
    

    menu = ["Home","Predication Section", "About me "]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        img = Image.open("C:\\Users\\Gaurav\\Desktop\\streamlit peoject\\portfolio\\heart.png")
        
        st.header("Heart Attack Predication App")
        st.image(img)
        st.text_area("""Cardiovascular  diseases  (CVDs)  including  Ischemic  HeartDisease (IHD) are one of the major causes of death globally. As per the report of World Health Organization (WHO), in 2014, the death rate is 6.96% in Bangladesh due to Ischemic Heart Diseases, which ranks  it  first  as  the  cause  of  death .  WHO  also forecasts  that  CVDs  would  be  contributing  to  24%  as  cause  of death  by  2030  and  recommended  to  take  extensive  initiatives  at various levels to reduce the mortality and morbidity out of IHDs""")
        st.subheader("Dataset link")
        st.write("check out this [link](https://archive.ics.uci.edu/ml/datasets/heart+disease)")


    elif choice == "Predication Section":
        st.header("This is Predication section")
        ml()
    
    elif choice == "About me ":
        st.header("Gaurav poudel")
        img = Image.open("C:\\Users\\Gaurav\\Desktop\\streamlit peoject\\portfolio\\aa.gif")
        st.image(img)
        aboutme()
        
        

main()