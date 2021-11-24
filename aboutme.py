import streamlit as st

def aboutme():
    socials =["linkedIn","Github","mail"]
    linkedIn = "https://www.linkedin.com/in/gaurav-poudel-76645a12b/"
    github = "https://github.com/gaurav-poudel"
    mail = "gauravpoudel83@gmail.com"
    
    with st.expander("LINKS TO MY SOCIAL"):
        a = st.selectbox("Socials",socials)
        if a == "linkedIn":
            st.write(linkedIn)
        elif a == "Github":
            st.write(github)
        elif a == "mail":
            st.write(mail)



aboutme()

