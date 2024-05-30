import streamlit as st
import torchvision.transforms as transforms
from PIL import Image
import torch.nn as nn
import torch
from torchvision.models import shufflenet_v2_x1_0
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import os
import numpy as np

status=0

def load_view(dt):
    global status
    st.title('Image Processing')
    technique_menu = ["Select The Model", "CNN", "SHUFFLENETVS"]
    technique_choice = st.selectbox("Please select Image Processing technique", technique_menu)

    if technique_choice == "CNN":
        cnn_submenu = ["Select Parameter","Current", "Vibration","Vibration_Bearing"]
        cnn_subchoice = st.selectbox("Please select CNN sub-technique", cnn_submenu)

        if cnn_subchoice == "Current":
                
                class CustomCNN(nn.Module):


    
                    def __init__(self, num_classes):
                        super(CustomCNN, self).__init__()
                        self.conv_layers = nn.Sequential(
                            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1),
                            nn.ReLU(),
                            nn.MaxPool2d(kernel_size=2, stride=2),
                            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
                            nn.ReLU(),
                            nn.MaxPool2d(kernel_size=2, stride=2),
                        )
                        self.fc_layers = nn.Sequential(
                            nn.Linear(32 * (image_size // 4) * (image_size // 4), 256),
                            nn.ReLU(),
                            nn.Linear(256, num_classes),
                        )

                    def forward(self, x):
                        x = self.conv_layers(x)
                        x = x.view(x.size(0), -1)
                        x = self.fc_layers(x)
                        return x
             
            # Constants
                num_classes = 5  # Number of classes in your dataset
                image_size = 224  # The same image size used during training
                model_weights_path = r'F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\views\save models\CurrentModel\trained_model_CustomCNN_1.pt'  # Path to your trained model weights

                # Data preprocessing
                data_transform = transforms.Compose([
                    transforms.Resize((image_size, image_size)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])

                # Load the saved model weights
                device = torch.device("cpu")  # Use CPU
                model = CustomCNN(num_classes=num_classes)
                model.load_state_dict(torch.load(model_weights_path, map_location=device))
                model.to(device)
                model.eval()

                data= dt.iloc[:830,0].values.flatten()
                # Create a directory to save the spectrogram images
                outputFolderPath = 'testSpectrogram_Images'
                os.makedirs(outputFolderPath, exist_ok=True)
                Fs = 55611  # Assuming the data is uniformly sampled; change Fs to your actual sampling frequency if known.
                window_size = 256  # Window size for STFT (adjust as needed)
                overlap = window_size // 2  # Overlap between adjacent windows (adjust as needed)
                nfft = 1024  # Number of FFT points (adjust as needed)

                    # Compute the spectrogram using the spectrogram function
                f, t, Sxx = spectrogram(data, fs=Fs, window='hann', nperseg=window_size, noverlap=overlap, nfft=nfft)

                    # Plot the spectrogram
                plt.figure()
                plt.pcolormesh(t, f, 10 * np.log10(Sxx))  # Convert to dB for better visualization
                plt.axis('off')  # Turn off the axes
                plt.gca().set_ylim(0, Fs/2)  # Show frequencies up to Nyquist limit
                    
                    # Save the image as PNG file
                outputFileName = f'Spectrogram_{0 + 1}.png'
                outputFilePath = os.path.join(outputFolderPath, outputFileName)
                plt.savefig(outputFilePath, bbox_inches='tight', pad_inches=0)  # Save without surrounding white space
                plt.close()

                # Compute the spectrogram for each row
                    
                    

                # Load and preprocess the input image
                input_image_path =outputFilePath
                input_image = Image.open(input_image_path).convert("RGB")
                input_tensor = data_transform(input_image).unsqueeze(0).to(device)

                # Make a prediction
                with torch.no_grad():
                    outputs = model(input_tensor)
                    predicted_class = torch.argmax(outputs, dim=1).item()

                # Get class labels from your dataset
                class_labels = ['BRB1', 'BRB2', 'BRB3', 'BRB4','HEALTHY']  # Replace with your actual class labels

                # Print the predicted label
                predicted_label = class_labels[predicted_class]


                # Display the predicted label in the Streamlit app
                st.title(f"Predicted Label With CNN: {predicted_label}")
                st.image(input_image, use_column_width=True)
                if (predicted_label !='HEALTHY'):
                    status=2
                else:
                    status=1

        elif cnn_subchoice == "Vibration":

            class CustomCNN(nn.Module):
         
                def __init__(self, num_classes):
                    super(CustomCNN, self).__init__()
                    self.conv_layers = nn.Sequential(
                        nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2, stride=2),
                        nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2, stride=2),
                    )
                    self.fc_layers = nn.Sequential(
                        nn.Linear(32 * (image_size // 4) * (image_size // 4), 256),
                        nn.ReLU(),
                        nn.Linear(256, num_classes),
                    )

                def forward(self, x):
                    x = self.conv_layers(x)
                    x = x.view(x.size(0), -1)
                    x = self.fc_layers(x)
                    return x
                
            # Constants
            num_classes = 5  # Number of classes in your dataset
            image_size = 224  # The same image size used during training
            model_weights_path =r"F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\views\save models\VibrationModel\trained_model_CustomCNN_1.pt"   # Path to your trained model weights

            # Data preprocessing
            data_transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])

            # Load the saved model weights
            device = torch.device("cpu")  # Use CPU
            model = CustomCNN(num_classes=num_classes)
            model.load_state_dict(torch.load(model_weights_path, map_location=device))
            model.to(device)
            model.eval()

        
            df= dt.iloc[:254,1].values.flatten()
        
            def generate_spectrogram(row_data, nperseg=255, noverlap=128):

                    
                _, _, Sxx = spectrogram(row_data, nperseg=nperseg, noverlap=noverlap)
                return Sxx

            output_folder = 'TEMP2'
            os.makedirs(output_folder, exist_ok=True)
            spectrogram_data = generate_spectrogram(df)
                
            # Plot the spectrogram without surrounding white space
            plt.imshow(np.log1p(spectrogram_data), cmap='jet', aspect='auto', origin='lower')  
            plt.ylim(0, 60)   
            # Remove surrounding white space
            plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

            # Save the spectrogram as an image with a transparent background in the "brb2" folder
            file_path = os.path.join(output_folder, f'Test_{0 + 1}.png')
            plt.savefig(file_path, transparent=True)
            plt.close()

            
                    
                
               

            input_image_path = file_path
            input_image = Image.open(input_image_path).convert("RGB")
            input_tensor = data_transform(input_image).unsqueeze(0).to(device)

            # Make a prediction
            with torch.no_grad():
                outputs = model(input_tensor)
                predicted_class = torch.argmax(outputs, dim=1).item()

            # Get class labels from your dataset
            class_labels = ['HEALTHY', 'BRB1', 'BRB2', 'BRB3', 'BRB4']  # Replace with your actual class labels

            # Print the predicted label
            predicted_label = class_labels[predicted_class]

            # Display the predicted label in the Streamlit app
            st.title(f"Predicted Label With CNN: {predicted_label}")
            st.image(input_image, use_column_width=True)
            if (predicted_label !='HEALTHY'):
                    status=2
            else:
                status=1
        
        elif cnn_subchoice=="Vibration_Bearing":

            class CustomCNN(nn.Module):
                def __init__(self, num_classes):

                    super(CustomCNN, self).__init__()
                    self.conv_layers = nn.Sequential(
                            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1),
                            nn.ReLU(),
                            nn.MaxPool2d(kernel_size=2, stride=2),
                            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
                            nn.ReLU(),
                            nn.MaxPool2d(kernel_size=2, stride=2),
                        )
                    self.fc_layers = nn.Sequential(
                            nn.Linear(32 * (image_size // 4) * (image_size // 4), 256),
                            nn.ReLU(),
                            nn.Linear(256, num_classes),
                        )

                def forward(self, x):
                    x = self.conv_layers(x)
                    x = x.view(x.size(0), -1)
                    x = self.fc_layers(x)
                    return x
            # Constants
            num_classes = 2 # Number of classes in your dataset
            image_size = 128  # The same image size used during training
            model_weights_path = r'F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\views\save models\BEARING MODELS\trained_model_CustomCNN_1.pt'  # Path to your trained model weights

            
            
            
            data_transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])




                    # Load the saved model weights
            device = torch.device("cpu")  # Use CPU
            model = CustomCNN(num_classes=num_classes)
            model.load_state_dict(torch.load(model_weights_path, map_location=device))
            model.to(device)
            model.eval()


            
            row_data = dt.iloc[:,2]
            # Parameters for the STFT
            windowSize = 1024
            hopSize = 256
            # Calculate the STFT spectrogram for the selected row
            f, t, s = spectrogram(row_data, window='hamming', nperseg=windowSize, noverlap=hopSize, nfft=windowSize)
            # Convert the complex STFT values to magnitude spectrogram and apply dB scaling
            magSpectrogram = np.abs(s)
            magSpectrogram = 20 * np.log10(magSpectrogram)
            # Plot the dB STFT spectrogram
            plt.figure()
            plt.imshow(magSpectrogram, origin='lower', aspect='auto', extent=[t.min(), t.max(), f.min(), f.max()], cmap='jet')
            plt.axis("off")
            # Create a directory to save the PNG files if it doesn't exist
            output_dir = 'Bearing_images'
            os.makedirs(output_dir, exist_ok=True)
            # Save the figure as a PNG image
            output_file = os.path.join(output_dir, 'Bearing_row_3.png')
            plt.savefig(output_file)
            # Close the current figure
            plt.close()



            # Load and preprocess the input image
                
            input_image_path =output_file
            input_image = Image.open(input_image_path).convert("RGB")
            input_tensor = data_transform(input_image).unsqueeze(0).to(device)


            # Make a prediction
            with torch.no_grad():
                outputs = model(input_tensor)
                predicted_class = torch.argmax(outputs, dim=1).item()

            # Get class labels from your dataset
            class_labels = ['INNER', 'OUTER']  # Replace with your actual class labels

            # Print the predicted label
            predicted_label = class_labels[predicted_class]

            # Display the predicted label in the Streamlit app
            st.title(f"Predicted Label With CNN: {predicted_label}")
            st.image(input_image, use_column_width=True)
            if (predicted_label !='HEALTHY'):
                    status=2
            else:
                    status=1
        

            
        
        

            
            

    if technique_choice == "SHUFFLENETVS":
        
        shufflenet_submenu = ["Select Parameter","Current", "Vibration","Vibration_Bearing"]
        shufflenet_subchoice = st.selectbox("Please select SHUFFLENETVS sub-technique", shufflenet_submenu)

        if shufflenet_subchoice == "Current":

            num_classes = 5  # Number of classes in your dataset
            image_size = 224  # The same image size used during training
            model_weights_path = r'F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\views\save models\CurrentModel\trained_model_ShuffleNetV2_1.pt'  # Path to your trained model weights

            # Data preprocessing
            data_transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])

            # Load the saved model weights on CPU
            device = torch.device("cpu")  # Use CPU
            model = shufflenet_v2_x1_0(pretrained=False)  # Initialize the same model architecture
            model.fc = nn.Linear(model.fc.in_features, num_classes)  # Change the fully connected layer
            model.load_state_dict(torch.load(model_weights_path, map_location=device))  # Load model on CPU
            model.to(device)
            model.eval()  # Set the model to evaluation mode

            # data=dt.iloc[0:1,::]
            
            df= dt.iloc[:830,0].values.flatten()


            # Create a directory to save the spectrogram images
            outputFolderPath = 'testSpectrogram_Images'
            os.makedirs(outputFolderPath, exist_ok=True)
            
            Fs = 55611  # Assuming the data is uniformly sampled; change Fs to your actual sampling frequency if known.
                
                # Choose appropriate parameters for the spectrogram calculation
            window_size = 256  # Window size for STFT (adjust as needed)
            overlap = window_size // 2  # Overlap between adjacent windows (adjust as needed)
            nfft = 1024  # Number of FFT points (adjust as needed)

                # Compute the spectrogram using the spectrogram function
            f, t, Sxx = spectrogram(df, fs=Fs, window='hann', nperseg=window_size, noverlap=overlap, nfft=nfft)

                # Plot the spectrogram
            plt.figure()
            plt.pcolormesh(t, f, 10 * np.log10(Sxx))  # Convert to dB for better visualization
            plt.axis('off')  # Turn off the axes
            plt.gca().set_ylim(0, Fs/2)  # Show frequencies up to Nyquist limit
                
                # Save the image as PNG file
            outputFileName = f'Spectrogram_{0 + 1}.png'
            outputFilePath = os.path.join(outputFolderPath, outputFileName)
            plt.savefig(outputFilePath, bbox_inches='tight', pad_inches=0)  # Save without surrounding white space
            plt.close()

         
            # Compute the spectrogram for each row
           
                

            

            # Load and preprocess the input image
            image_path = outputFilePath # Replace with the path to your input image
            input_image = Image.open(image_path).convert("RGB")  # Convert to RGB format
            input_tensor = data_transform(input_image).unsqueeze(0).to(device)

            # Make a prediction
            with torch.no_grad():
                outputs = model(input_tensor)
                predicted_class = torch.argmax(outputs, dim=1).item()

            # Get class labels from your dataset
            class_labels = ['BRB1', 'BRB2', 'BRB3', 'BRB4','HEALTHY']  # Replace with your actual class labels

            # Print the predicted label
            st.title(f"Predicted Label With ShuffleNet: {class_labels[predicted_class]}")

        
            # Display the testing image using Streamlit
            st.image(input_image, use_column_width=True)
            if (class_labels[predicted_class] !='HEALTHY'):
                    status=2
            else:

                status=1

           

        if shufflenet_subchoice == "Vibration":


            num_classes = 5  # Number of classes in your dataset
            image_size = 224  # The same image size used during training
            model_weights_path = r'F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\views\save models\VibrationModel\trained_model_ShuffleNetV2_1.pt'  # Path to your trained model weights

            # Data preprocessing
            data_transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])

            # Load the saved model weights on CPU
            device = torch.device("cpu")  # Use CPU
            model = shufflenet_v2_x1_0(pretrained=False)  # Initialize the same model architecture
            model.fc = nn.Linear(model.fc.in_features, num_classes)  # Change the fully connected layer
            model.load_state_dict(torch.load(model_weights_path, map_location=device))  # Load model on CPU
            model.to(device)
            model.eval()  # Set the model to evaluation mode


            # df=dt.iloc[1:2,:254]
            df= dt.iloc[:254,1].values.flatten()

            def generate_spectrogram(row_data, nperseg=255, noverlap=128):
                    
                _, _, Sxx = spectrogram(row_data, nperseg=nperseg, noverlap=noverlap)
                return Sxx

                # Create a folder named "brb2" to save the images
            output_folder = 'TEMP3'
            os.makedirs(output_folder, exist_ok=True)
          
            spectrogram_data = generate_spectrogram(df)
                
                    # Plot the spectrogram without surrounding white space
            plt.imshow(np.log1p(spectrogram_data), cmap='jet', aspect='auto', origin='lower')
                    
            plt.ylim(0, 60)
                    
                    # Remove surrounding white space
            plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

                    # Save the spectrogram as an image with a transparent background in the "brb2" folder
            file_path = os.path.join(output_folder, f'Test_{0 + 1}.png')
            plt.savefig(file_path, transparent=True)
            plt.close()

                # Loop through each row in the DataFrame and generate spectrogram
        
                    
                








            # Load and preprocess the input image
            image_path = file_path
            input_image = Image.open(image_path).convert("RGB")  # Convert to RGB format
            input_tensor = data_transform(input_image).unsqueeze(0).to(device)

            # Make a prediction
            with torch.no_grad():
                outputs = model(input_tensor)
                predicted_class = torch.argmax(outputs, dim=1).item()

            # Get class labels from your dataset
            class_labels = ['HEALTHY', 'BRB1', 'BRB2', 'BRB3', 'BRB4']  # Replace with your actual class labels

            # Print the predicted label
            st.title(f"Predicted Label With ShuffleNet: {class_labels[predicted_class]}")
        
    
            # Display the testing image using Streamlit
            st.image(input_image, use_column_width=True)
            if (class_labels[predicted_class] !='HEALTHY'):
                    status=False
            else:     
                status=True



        elif shufflenet_subchoice=="Vibration_Bearing":

            num_classes = 2  # Number of classes in your dataset
            image_size = 224  # The same image size used during training
            model_weights_path = r'F:\streamlit-navbar-flaskless-main\streamlit-navbar-flaskless-main\views\save models\BEARING MODELS\trained_model_ShuffleNetV2_1.pt'  # Path to your trained model weights

            # Data preprocessing
            data_transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])

            # Load the saved model weights on CPU
            device = torch.device("cpu")  # Use CPU
            model = shufflenet_v2_x1_0(pretrained=False)  # Initialize the same model architecture
            model.fc = nn.Linear(model.fc.in_features, num_classes)  # Change the fully connected layer
            model.load_state_dict(torch.load(model_weights_path, map_location=device))  # Load model on CPU
            model.to(device)
            model.eval()  # Set the model to evaluation mode

            # dt=dt.dropna()
            row_data = dt.iloc[:,2]


            # Parameters for the STFT
            windowSize = 1024
            hopSize = 256
            # Calculate the STFT spectrogram for the selected row
            f, t, s = spectrogram(row_data, window='hamming', nperseg=windowSize, noverlap=hopSize, nfft=windowSize)

            # Convert the complex STFT values to magnitude spectrogram and apply dB scaling
            magSpectrogram = np.abs(s)
            magSpectrogram = 20 * np.log10(magSpectrogram)

            # Plot the dB STFT spectrogram
            plt.figure()
            plt.imshow(magSpectrogram, origin='lower', aspect='auto', extent=[t.min(), t.max(), f.min(), f.max()], cmap='jet')
            plt.axis("off")

            # Create a directory to save the PNG files if it doesn't exist
            output_dir = 'Bearing_images'
            os.makedirs(output_dir, exist_ok=True)

            # Save the figure as a PNG image
            output_file = os.path.join(output_dir, 'Bearing_row_3.png')
            plt.savefig(output_file)

            # Close the current figure
            plt.close()
            

            # Load and preprocess the input image
            image_path = output_file
            input_image = Image.open(image_path).convert("RGB")  # Convert to RGB format
            input_tensor = data_transform(input_image).unsqueeze(0).to(device)

            # Make a prediction
            with torch.no_grad():
                outputs = model(input_tensor)
                predicted_class = torch.argmax(outputs, dim=1).item()

            # Get class labels from your dataset
            class_labels = ['INNER', 'OUTER']  # Replace with your actual class labels

            # Print the predicted label
            # st.title(f"Predicted Label With ShuffleNet: {class_labels[predicted_class]}")
            st.markdown(f"<h1 style='text-align: center;'>Predicted Label With ShuffleNet: {class_labels[predicted_class]}</h1>", unsafe_allow_html=True)
            # Display the testing image using Streamlit
            st.image(input_image, use_column_width=False)
            if (class_labels[predicted_class] !='HEALTHY'):
                    status=2
            else:
                status=1
            
            
           
            


def statusload():

    return status




hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)