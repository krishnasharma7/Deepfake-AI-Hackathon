import os
import torch 
from torch import nn
import cv2
import gdown
import pandas as pd
import numpy as np 
from pathlib import Path


class Deepfakedetector(nn.Module):
    def __init__(self, input_dim,hidden_units ):
        super().__init__()
        self.rnn = nn.LSTM(input_dim , hidden_units , batch_first = True)
        self.classifier = nn.Linear(hidden_units , 1)
        
    def forward(self , x):
        batch_size , frames , C , H , W = x.size()
        output , _ = self.rnn(x.view(batch_size , frames , -1))
        last_output = output[:,-1,:]
        output = self.classifier(last_output)
        return torch.round(torch.sigmoid(output))

        
def download_file_from_google_drive(file_id, destination):
    """
    Download a file from Google Drive.

    Args:
        file_id (str): The file ID from Google Drive.
        destination (str): The destination path where the file will be saved.
    """
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, destination, quiet=False)

def get_frames(video_path, duration=5):
    frames = []
    capture = cv2.VideoCapture(str(video_path))
    fps = capture.get(cv2.CAP_PROP_FPS)
    num_frames_to_read = int(fps * duration)
    capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    for _ in range(num_frames_to_read):
        ret, frame = capture.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224,224))
        frames.append(frame)

    capture.release()
    return torch.tensor(np.float32(np.array(frames , dtype = np.float32)/255))

def get_predictions(file_path):
    """
    This function takes input of file path and returns numpy array of predictions

    1-> Downloads model
    2-> Loads Model
    3-> Gets Predictions
    
    """
    model_path = Path("model.pth")
    if model_path.exists():
        print("Skipping download")
    else:
        print("Downloading model...")
        file_id = "1Dv3xB0S1FOJ7ssFtt5kXw3yRRSGqo53w"
        destination = "model.pth"
        download_file_from_google_drive(file_id, destination)
    print("Loading model")
    model = None
    try:
        model = torch.load(model_path , map_location=torch.device('cpu'))
        print("Model Loadded successfully")
    except Exception as e:
        print("Model loading failed ")
        return model
    frames = get_frames(file_path)
    model.eval()
    with torch.no_grad():
        preds = model(frames.unsqueeze(dim =0))
    return preds.numpy().squeeze()


