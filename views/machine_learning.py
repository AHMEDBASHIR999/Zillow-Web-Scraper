# import streamlit as st
# import pandas as pd
# import joblib
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.signal import spectrogram
# import os
# # from skimage.io import imread
# # from skimage.transform import resize
# # import joblib



# def load_view(df):
    
#     st.title('Machine Learning')
#     sub_menu = ["Select the Model","Random Forest"]
#     sub_choice = st.selectbox("Please select Siganal Processing technique", sub_menu)


#     if sub_choice == "Random Forest":
#         cnn_submenu = ["Select Parameter","Current", "Vibration","Vibration_Bearing"]
#         cnn_subchoice = st.selectbox("Please select Attributes", cnn_submenu)


#         if cnn_subchoice=="Vibration":


#             # Load the saved Random Forest model
#             loaded_random_forest_model = joblib.load(r"F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\random_forest_model_vib\random_forest_model_vib.joblib")

#             # Function to preprocess a single image
#             def preprocess_single_image(image_path, target_size=(100, 100)):
#                 img = imread(image_path)
#                 img = resize(img, target_size)
#                 img = img / 255.0  # Normalize pixel values to [0, 1]
#                 return img.flatten()  # Flatten the image as a feature vector

#             # Path to the single image you want to predict
#             # Load the CSV file into a pandas DataFrame
    
#             df= df.iloc[:255,1].values.flatten()
            
#             # Function to generate a spectrogram for a single row
#             def generate_spectrogram(row_data, nperseg=250, noverlap=128):
#                 _, _, Sxx = spectrogram(row_data, nperseg=nperseg, noverlap=noverlap)
#                 return Sxx

#             # Create a folder named "brb2" to save the images
#             output_folder = 'TEMP44'
#             os.makedirs(output_folder, exist_ok=True)

#             # Loop through each row in the DataFrame and generate spectrogram
        
#             spectrogram_data = generate_spectrogram(df)
            
#                 # Plot the spectrogram without surrounding white space
#             plt.imshow(np.log1p(spectrogram_data), cmap='jet', aspect='auto', origin='lower')
                
#             plt.ylim(0, 60)
                
#                 # Remove surrounding white space
#             plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

#                 # Save the spectrogram as an image with a transparent background in the "brb2" folder
#             file_path = os.path.join(output_folder, f'BRB33_{0 + 1}.png')
#             plt.savefig(file_path, transparent=True)
#             plt.close()


#             single_image_path =file_path
#             # Preprocess the single image
#             preprocessed_image = preprocess_single_image(single_image_path)
#             # Reshape the preprocessed image to match the shape used during training
#             preprocessed_image = preprocessed_image.reshape(1, -1)
#             # Use the loaded model to predict the label of the single image
#             predicted_label = loaded_random_forest_model.predict(preprocessed_image)
#             # Display the predicted label using st.write or st.text
#             # st.title("Predicted Label: " + str(predicted_label[0]))
#             st.markdown(f"<h1 style='text-align: center;'>Predicted Label: {predicted_label[0]}</h1>", unsafe_allow_html=True)



#         elif cnn_subchoice=="Current":
#             # Load the saved Random Forest model
#             loaded_random_forest_model = joblib.load(r"F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\random_forest_model_vib\random_forest_model_cur.joblib")

#             # Function to preprocess a single image
#             def preprocess_single_image(image_path, target_size=(100, 100)):
#                 img = imread(image_path)
#                 img = resize(img, target_size)
#                 img = img / 255.0  # Normalize pixel values to [0, 1]
#                 return img.flatten()  # Flatten the image as a feature vector

#             # Path to the single image you want to predict
#             # Load the CSV file into a pandas DataFrame
#             df= df.iloc[:830,0].values.flatten()
#             # Function to generate a spectrogram for a single row

#             outputFolderPath = 'testSpectrogram_Images_forML'
#             os.makedirs(outputFolderPath, exist_ok=True)
#             Fs = 55611  # Assuming the data is uniformly sampled; change Fs to your actual sampling frequency if known.
                    
#                     # Choose appropriate parameters for the spectrogram calculation
#             window_size = 256  # Window size for STFT (adjust as needed)
#             overlap = window_size // 2  # Overlap between adjacent windows (adjust as needed)
#             nfft = 1024  # Number of FFT points (adjust as needed)

#                     # Compute the spectrogram using the spectrogram function
#             f, t, Sxx = spectrogram(df, fs=Fs, window='hann', nperseg=window_size, noverlap=overlap, nfft=nfft)

#                     # Plot the spectrogram
#             plt.figure()
#             plt.pcolormesh(t, f, 10 * np.log10(Sxx))  # Convert to dB for better visualization
#             plt.axis('off')  # Turn off the axes
#             plt.gca().set_ylim(0, Fs/2)  # Show frequencies up to Nyquist limit
                    
#                     # Save the image as PNG file
#             outputFileName = f'Spectrogram_{0 + 1}.png'
#             outputFilePath = os.path.join(outputFolderPath, outputFileName)
#             plt.savefig(outputFilePath, bbox_inches='tight', pad_inches=0)  # Save without surrounding white space
#             plt.close()
#             single_image_path =outputFilePath
#             # Preprocess the single image
#             preprocessed_image = preprocess_single_image(single_image_path)
#             # Reshape the preprocessed image to match the shape used during training
#             preprocessed_image = preprocessed_image.reshape(1, -1)
#             # Use the loaded model to predict the label of the single image
#             predicted_label = loaded_random_forest_model.predict(preprocessed_image)
#             # Display the predicted label using st.write or st.text
#             # st.title("Predicted Label: " + str(predicted_label[0]))
#             st.markdown(f"<h1 style='text-align: center;'>Predicted Label: {predicted_label[0]}</h1>", unsafe_allow_html=True)


#         elif cnn_subchoice=="Vibration_Bearing":

#              # Load the saved Random Forest model
#             loaded_random_forest_model = joblib.load(r"F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\random_forest_model_vib\random_forest_model_bearing (1).joblib")

#             # Function to preprocess a single image
#             def preprocess_single_image(image_path, target_size=(100,100)):
#                 img = imread(image_path)
#                 img = resize(img, target_size)
#                 img = img / 255.0  # Normalize pixel values to [0, 1]
#                 return img.flatten()  # Flatten the image as a feature vector

#              # dt=dt.dropna()
#             row_data = df.iloc[:,2]


#             # Parameters for the STFT
#             windowSize = 1024
#             hopSize = 256
#             # Calculate the STFT spectrogram for the selected row
#             f, t, s = spectrogram(row_data, window='hamming', nperseg=windowSize, noverlap=hopSize, nfft=windowSize)

#             # Convert the complex STFT values to magnitude spectrogram and apply dB scaling
#             magSpectrogram = np.abs(s)
#             magSpectrogram = 20 * np.log10(magSpectrogram)

#             # Plot the dB STFT spectrogram
#             plt.figure()
#             plt.imshow(magSpectrogram, origin='lower', aspect='auto', extent=[t.min(), t.max(), f.min(), f.max()], cmap='jet')
#             plt.axis("off")

#             # Create a directory to save the PNG files if it doesn't exist
#             output_dir = 'Bearing_images'
#             os.makedirs(output_dir, exist_ok=True)

#             # Save the figure as a PNG image
#             output_file = os.path.join(output_dir, 'Bearing_row_3.png')
#             plt.savefig(output_file)

#             # Close the current figure
#             plt.close()
              
#             single_image_path =output_file
#             # Preprocess the single image
#             preprocessed_image = preprocess_single_image(single_image_path)
#             # Reshape the preprocessed image to match the shape used during training
#             preprocessed_image = preprocessed_image.reshape(1, -1)
#             # Use the loaded model to predict the label of the single image
#             predicted_label = loaded_random_forest_model.predict(preprocessed_image)
#             # Display the predicted label using st.write or st.text
#             # st.title("Predicted Label: " + str(predicted_label[0]), align='center')
#             st.markdown(f"<h1 style='text-align: center;'>Predicted Label: {predicted_label[0]}</h1>", unsafe_allow_html=True)




      
        



            


























    
#     # data=pd.read_csv('r1b05.csv')
    
#     # data=data.iloc[:,1]
#     # data=pd.DataFrame(data)
#     # rows_per_col = 831
#     # num_cols = len(data) // rows_per_col
#     # # Reshape the DataFrame into the desired format
#     # data= data.iloc[:num_cols * rows_per_col]  # Truncate any extra rows
#     # data = data.values.reshape(-1, rows_per_col).T
#     # data=pd.DataFrame(data)
#     # data= data.reset_index(drop=True)
#     # # Transpose the dataframe
#     # df_transposed = data.transpose()
#     # df_transposed=pd.DataFrame(df_transposed)





  
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)