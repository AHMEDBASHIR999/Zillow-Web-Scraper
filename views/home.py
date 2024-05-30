import streamlit as st

# Set page configuration as the first Streamlit command

from views import home, Signal_processing, plots, file, image_processing, Motor_Status

def load_view():
    # Set page layout
    st.markdown(
        """
        <style>
        .css-z5fcl4 {
            width: 100%;
            padding: 0rem 3rem 0rem;
            min-width: auto;
            max-width: initial;
        }
        .css-1kyxreq {
            display: flex;
            flex-flow: wrap;
            row-gap: 1rem;
            justify-content: center;
        }
        .container {
            max-width: 900px;
            padding: 20px;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
            font-size: 14px;
            margin-top: 185px;
        }
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        a {
            text-decoration: none; /* Removes underline from links */
            color: black; /* Sets link color to black */
        }
        a:hover {
            text-decoration: none; /* Removes underline on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Add header
    # st.write("""
    #     ### WELCOME TO PATRONECS AI DASHBOARD
    # """)
    st.header("WELCOME TO PATRONECS AI DASHBOARD", divider='orange')

    # Add columns with images and descriptions
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("test.jpg", use_column_width=True)
        st.header("Zillow Web Scraper", divider='blue')
        st.markdown('<a href="https://www.patronecs.com/">View Source →</a>', unsafe_allow_html=True)
   
        st.write("Efficiently extract and analyze web data for insights and automation with our robust web scraping solution.")

    with col2:
        st.image("test.jpg", use_column_width=True)
        st.header("Chatbots", divider='blue')
        st.markdown('<a href="#">Link 2 →</a>', unsafe_allow_html=True)
        st.write("Description for image 2.")

    with col3:
        st.image("test.jpg", use_column_width=True)
        st.header("Voice to Text", divider='blue')
        st.markdown('<a href="#">Link 3 →</a>', unsafe_allow_html=True)
        st.write("Efficiently extract and analyze web data for insights and automation with our robust web scraping solution.")

    with col4:
        st.image("test.jpg", use_column_width=True)
        st.header("Text to Audio", divider='blue')
        st.markdown('<a href="#">Link 4 →</a>', unsafe_allow_html=True)
        st.write("Description for image 4.")

    # Add footer
    st.markdown(
        """
        <div class="footer">
            © 2023 WELCOME TO PATRONECS AI DASHBOARD
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add call to action (if needed)

# Call the load_view function to display the content
load_view()
