import streamlit as st
import matplotlib.pyplot as plt

def load_view(dt):
        
    st.title('Plots')
    sub_menu2 = ["Select the Plot","Bar chart", "Line chart", "Area chart", "Spectrogram"]
    sub_choice = st.selectbox("Please select a chart ", sub_menu2)

    if sub_choice == "Bar chart":
        barchart = ["Select Parameter","Current", "Vibration","Bearing_Vib"]
        bar_subchoice = st.selectbox("Please select Attributes", barchart)

        if bar_subchoice=="Current":
            st.bar_chart(dt.iloc[:830,0])

        elif bar_subchoice=="Vibration":
            st.bar_chart(dt.iloc[:255,1])

        elif bar_subchoice=="Bearing_Vib":
            st.bar_chart(dt.iloc[::,2])
      
    


    elif sub_choice=="Line chart":
        linechart = ["Select Parameter","Current", "Vibration","Bearing_Vib"]
        line_subchoice = st.selectbox("Please select Attributes", linechart)
        if line_subchoice=="Current":
            st.line_chart(dt.iloc[:830,0])
        elif line_subchoice=="Vibration":
            st.line_chart(dt.iloc[:255,1])
        elif line_subchoice=="Bearing_Vib":
            st.line_chart(dt.iloc[::,2])

    elif sub_choice=="Area chart":
        Areachart = ["Select Parameter","Current", "Vibration","Bearing_Vib"]
        Areachart_subchoice = st.selectbox("Please select Attributes", Areachart)
        if Areachart_subchoice=="Current":
            st.area_chart(dt.iloc[:830,0])
        elif Areachart_subchoice=="Vibration":
            st.area_chart(dt.iloc[:255,1])
        elif Areachart_subchoice=="Bearing_Vib":
            st.area_chart(dt.iloc[::,2])


    elif sub_choice=="Spectrogram":
        specto = ["Select Parameter","Current", "Vibration","Bearing_Vib"]
        spectogram_subchoice = st.selectbox("Please select Attributes", specto)

        if spectogram_subchoice=="Current":
            plot_spectrogram(dt.iloc[:830,0],55611)

        elif spectogram_subchoice=="Vibration":
            plot_spectrogram(dt.iloc[:255,1],8326)
        elif spectogram_subchoice=="Bearing_Vib":
            plot_spectrogram(dt.iloc[::,2],1)






            
    
    
    




    # if sub_choice == "Bar chart":
        
    # elif sub_choice == "Line chart":
    #     st.line_chart(dt.iloc[0,::])
    # elif sub_choice == "Area chart":
    #     st.area_chart(dt.iloc[0,::])
    # elif sub_choice == "Spectrogram":
    #     plot_spectrogram(dt.iloc[0,::])


def plot_spectrogram(dt,fs):
    plt.specgram(dt, Fs=fs,cmap='jet')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.title('Spectrogram')
    st.pyplot()




hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)