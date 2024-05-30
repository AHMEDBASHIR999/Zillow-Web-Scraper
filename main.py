import streamlit as st

# Set page configuration as the first Streamlit command
st.set_page_config(layout="wide", page_title="WELCOME TO PATRONECS AI DASHBOARD")

# Now import other modules
from views import home, Signal_processing, plots, file, image_processing, Motor_Status

menu_items = ["Home", "File", "Web Scraper", "Signal Processing", "Image Processing", "Machine Learning", "Check Motor Status"]

st.sidebar.image("LOGO.png",width=200)
choice = st.sidebar.selectbox("", menu_items)

if choice == "Home":
    home.load_view()
elif choice == "File":
    file.load_view()
elif choice == "Plots":
    plots.load_view(file.load_data())

elif choice == "Web Scraper":
    Signal_processing.load_view()
elif choice == "Image Processing":
    image_processing.load_view(file.load_data())
# elif choice == "Machine Learning":
#     machine_learning.load_view(file.load_data())
elif choice == "Check Motor Status":
    Motor_Status.load_view(image_processing.statusload())

st.set_option('deprecation.showPyplotGlobalUse', False)
