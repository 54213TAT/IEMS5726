# 1155250136 Cheng Haotian
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os
import torch
import torchaudio
from torchaudio import transforms
from torch.utils.data import Dataset, DataLoader
from torch import nn, optim


# Problem 2
def problem_2(df, k=5, t=0.2): 
    list = []
    # write your logic here, test is a dataframe
    train_df, test = train_test_split(df, test_size=t, random_state=0)
    
    segment_size = len(train_df) // k
    remain_size = len(train_df) % k
    start_index = 0
    for i in range(k):
        current_len = segment_size + 1 if i < remain_size else segment_size
        end_index = start_index + current_len
        segment = train_df.iloc[start_index:end_index]
        list.append(segment)
        start_index = end_index
    return list, test

# Problem 3
def problem_3(filename, column_label):
    # write your logic here, df is a dataframe instead
    df = pd.read_csv(filename)
    dummies = pd.get_dummies(df[column_label], prefix='', prefix_sep='', dtype=int)
    df = pd.concat([df, dummies], axis=1)
    return df

# Problem 4
def problem_4(path):
    # Don't touch the settings below
    desired_length, n_fft, hop_len, n_mels, top_db = 100000, 1024, 256, 32, 80
    list_of_mel_spec_db = []
    # retrieve the list of files under path
    file_names = os.listdir(path)
    
    for file in file_names:
        # write your logic here: load audio file
        waveform, sample_rate = torchaudio.load(os.path.join(path, file))
    
        
        # get the current length of the waveform
        current_length = waveform.size(1)  # Size (channels, length)
    
        # write your logic here:
        # truncate the waveform, or pad the waveform with zeros
        if current_length > desired_length:
            waveform = waveform[:, :desired_length]
        elif current_length < desired_length:
            padding = desired_length - current_length
            waveform = torch.nn.functional.pad(waveform, (0, padding))
        
        
        # write your logic here: define mel spec with the settings
        mel_transform = transforms.MelSpectrogram(
            sample_rate=sample_rate,
            n_fft=n_fft,
            hop_length=hop_len,
            n_mels=n_mels
        )
        
        # write your logic here: apply the transform to the waveform
        mel_spec = mel_transform(waveform)
        
        # write your logic here: convert to decibels with the settings
        mel_spec_db = transforms.AmplitudeToDB(top_db=top_db)(mel_spec)
        
        list_of_mel_spec_db.append(mel_spec_db)
        
    # convert the list to a tensor
    # assume all spec have the same shape
    mel_spec_tensor = torch.stack(list_of_mel_spec_db)

    return mel_spec_tensor

# Problem 5
class MyDataset(Dataset):
	def __init__(self, tensors):
		self.tensors = tensors
	def __len__(self):
		return len(self.tensors)
	def __getitem__(self, idx):
		return self.tensors[idx]

# write your autoencoder structure here
class AE(nn.Module):
    def __init__(self):
        super(AE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(2 * 32 * 391, 8224),
            nn.ReLU(),
            nn.Linear(8224, 2056),
            nn.ReLU(),
            nn.Linear(2056, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256)
        )

        self.decoder = nn.Sequential(
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 2056),
            nn.ReLU(),
            nn.Linear(2056, 8224),
            nn.ReLU(),
            nn.Linear(8224, 2 * 32 * 391),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded, encoded

def problem_5(tensor_file):
    loaded_tensor = torch.load(tensor_file, weights_only=True)
    dataset = MyDataset(loaded_tensor)
    dataloader = DataLoader(dataset, batch_size=25, shuffle=False)
    
    model = AE()
    loss_function = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-8)
    epochs = 20
    losses = []
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    for epoch in range(epochs):
        loss1 = []
        for audio in dataloader:
            audio = audio.view(-1, 2 * 32 * 391).to(device)
            reconstructed = model(audio)[0]
            loss = loss_function(reconstructed, audio)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            loss1.append(loss.item())
            
        losses.append(sum(loss1) / len(loss1))
            
    return losses

# Problem 6
class OAE(nn.Module):
    def __init__(self):
        super(OAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(2, 32, kernel_size=3, stride=1, padding=1),  
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2), 
            
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),  
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2), 
            
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1), 
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)   
        )
        
        self.flatten_size = 128 * 4 * 48
        self.fc_enc = nn.Linear(self.flatten_size, 256)
        
        self.fc_dec = nn.Linear(256, self.flatten_size)
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2, output_padding=(0, 1)),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            
            nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2, output_padding=(0, 1)),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            
            nn.ConvTranspose2d(32, 2, kernel_size=2, stride=2, output_padding=(0, 1)),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        encoded_flat = encoded.view(-1, self.flatten_size)
        latent = self.fc_enc(encoded_flat)
        
        decoded_flat = self.fc_dec(latent)
        decoded_view = decoded_flat.view(-1, 128, 4, 48)
        decoded = self.decoder(decoded_view)
            
        return decoded, latent

def problem_6(tensor_file):
    # write your logic here   
    loaded_tensor = torch.load(tensor_file, weights_only=True)
    dataset = MyDataset(loaded_tensor)
    dataloader = DataLoader(dataset, batch_size=25, shuffle=True)
    
    model = OAE()
    loss_function = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-8)
    epochs = 20
    losses = []
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    for epoch in range(epochs):
        loss1 = []
        batch_count = 0
        for audio in dataloader:
            
            audio = audio.view(-1, 2 * 32 * 391).to(device)
            reconstructed = model(audio)[0]
            loss = loss_function(reconstructed, audio)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            loss1.append(loss.item())
            batch_count += 1
        
        avg_loss = sum(loss1) / len(loss1)
        losses.append(avg_loss)
        #print(f"Problem 6 - Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.6f}")
            
    return losses


if __name__ == "__main__":
    # Testing: Problem 2
    df = pd.read_csv("problem2.csv")
    list, test = problem_2(df, k=5, t=0.2)
    for item in list:
        print("Segment: ", item.shape)
    print("Testing: ", test.shape)


    # Testing: Problem 3
    df = problem_3("problem3.csv","color")
    print(df)
   
   
    # Testing: Problem 4
    tensor = problem_4("TRAIN")
    print("Type of tensor:", type(tensor))
    print("Shape of tensor:", tensor.shape)
    torch.save(tensor, "problem_4.pt")

    
    # Testing: Problem 5
    losses = []
    losses = problem_5("problem_4.pt")
    i = 1
    for loss in losses:
        print(f"Epoch {i}/20, Loss: {loss:.6f}")
        i += 1
    
    
    # Testing: Problem 6
    losses = []
    losses = problem_6("problem_4.pt")
    i = 1
    for loss in losses:
        print(f"Epoch {i}/20, Loss: {loss:.6f}")
        i += 1


""" Written Part

CNN AutoEncoder
Encoder: Use 3-layer Conv2d+BatchNorm+ReLU+MaxPool2d to gradually compress the features of the input (250, 2, 32, 391).
Latent Space: After flattening, it is mapped to a 256 dimensional vector through a fully connected layer.
Decoder: Use 3-layer ConvTranspose2d for upsampling, and combine it with output padding to ensure that the output size is accurately restored to (250, 2, 32, 391).
Removing the Sigmoid activation function from the last layer of the Decoder allows the model to more accurately fit the true dB values

output: 
Epoch 1/20, Loss: 2182.771716
Epoch 2/20, Loss: 2139.431750
Epoch 3/20, Loss: 2117.004724
Epoch 4/20, Loss: 2096.492700
Epoch 5/20, Loss: 2076.086646
Epoch 6/20, Loss: 2054.827820
Epoch 7/20, Loss: 2025.395715
Epoch 8/20, Loss: 2003.397449
Epoch 9/20, Loss: 1968.346362
Epoch 10/20, Loss: 1940.104871
Epoch 11/20, Loss: 1913.002002
Epoch 12/20, Loss: 1885.661597
Epoch 13/20, Loss: 1862.066125
Epoch 14/20, Loss: 1829.054407
Epoch 15/20, Loss: 1799.668823
Epoch 16/20, Loss: 1773.946277
Epoch 17/20, Loss: 1751.414355
Epoch 18/20, Loss: 1713.818494
Epoch 19/20, Loss: 1682.382593
Epoch 20/20, Loss: 1654.562366 """