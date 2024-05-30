import streamlit as st

def load_view(status):
    st.title('Motor Status: ')
    if (status ==1):
        st.write(f"<h3 style='text-align: center;'>Motor is HEALTHY </h1>", unsafe_allow_html=True)
    elif(status==2):
        st.write(f"<h3 style='text-align: center;'>Motor is UN-HEALTHY </h1>", unsafe_allow_html=True)
    else:
        st.write(f"<h3 style='text-align: center;'>Please Apply Machine and Deep Learning Model Firstly </h1>", unsafe_allow_html=True)
        

    
    




hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)