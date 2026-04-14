# 1155250136 Cheng Haotian
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing, load_wine
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.cluster import KMeans
from sklearn.model_selection import KFold
# Problem 2
# Define the feedforward neural network regressor
class FeedForwardNN(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def problem_2(X, y, test_size=0.3, learning_rate=0.01, max_epochs=50000):
    testing_mse = 0
    # use this seed number for reproducibility
    # however, results from win, mac, linux are different
    # even they share the same seed number
    seed_number=5731 
    torch.manual_seed(seed_number)
    np.random.seed(seed_number)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed_number)
    scaler = StandardScaler()
    
    # write your logic here: train a scaler based on training data, and apply the trained scaler on the testing data
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    input_size = X_train.shape[1]
    model = FeedForwardNN(input_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    X_train_tensor = torch.FloatTensor(X_train)
    y_train_tensor = torch.FloatTensor(y_train).view(-1, 1)
    X_test_tensor = torch.FloatTensor(X_test)
    y_test_tensor = torch.FloatTensor(y_test).view(-1, 1)
    
    for epoch in range(max_epochs):
        model.train()
        # write your logic here: fill in the training loop
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)
        loss.backward()
        optimizer.step()
        
        """ if (epoch+1) % 1000 == 0:
            print(f"Epoch [{epoch+1}/{max_epochs}], Loss: {loss.item():.4f}") """

    # write your logic here: evaluate the testing_mse based on testing set
    model.eval()
    with torch.no_grad():
        outputs = model(X_test_tensor)
        testing_mse = criterion(outputs, y_test_tensor).item()

    return testing_mse


# Problem 3
def problem_3(X, y, kfold=10):
    # write your logic here   
    model = GaussianNB()
    cv_accuracy = 0
    seed_number = 5731  # default seed is 5731
    kf = KFold(n_splits=kfold, shuffle=True, random_state=seed_number)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        cv_accuracy += metrics.accuracy_score(y_test, y_pred)
    
    cv_accuracy /= kfold
    model.fit(X, y)

    return cv_accuracy, model
    

# Problem 4
# write your logic here   
# define the Autoencoder according the specification
class Autoencoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, hidden_size),
        )
        self.decoder = nn.Sequential(
            nn.Linear(hidden_size, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, input_size),
            nn.Sigmoid(),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded, encoded

# Problem 5
def problem_5(model, loader):
    # write your logic here
    encoded_list = []
    model.eval()
    with torch.no_grad():
        for data in loader:
            img, _ = data
            _, encoded = model(img)
            encoded_list.append(encoded.detach().numpy())
    
    return_array = np.concatenate(encoded_list, axis=0)
    return return_array


# Problem 6
def problem_6(image_descriptor, k=5):
    # write your logic here   
    kmeans = KMeans(n_clusters=k, random_state=5731)
    kmeans.fit(image_descriptor)
    centres = kmeans.cluster_centers_
    
    return centres


if __name__ == "__main__":
    # Testing: Problem 2
    data = fetch_california_housing()
    X, y = data.data, data.target
    mse = problem_2(X, y, test_size=0.3, learning_rate=0.01, max_epochs=100)
    print("MSE in Testing: ", mse)


    # Testing: Problem 3
    data = load_wine()
    X, y = data.data, data.target
    cv_accuracy, model = problem_3(X, y, kfold=5)
    print("5-fold cross validation accuracy:", cv_accuracy)
    print("model description:", model)
   
   
    # Testing: Problem 4
    input_size = 28 * 28  
    latent_size = 128 
    model = Autoencoder(input_size, latent_size)
    print("Model information:", model)
    
    
    # Testing: Problem 5
    num_epochs = 10
    batch_size = 64
    learning_rate = 0.001
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.view(-1)),
    ])
    images = datasets.FashionMNIST(root='data', train=True, transform=transform, download=True)
    loader = DataLoader(dataset=images, batch_size=batch_size, shuffle=False)
    
    for epoch in range(num_epochs):
        for data in loader:
            img, _ = data
            output = model(img)[0]
            loss = criterion(output, img)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    image_descriptor = problem_5(model, loader)
    print("Image descriptor:", image_descriptor)
    print("Dimension:", image_descriptor.shape)
    
    
    # Testing: Problem 6
    centres = problem_6(image_descriptor, k=10)
    print("The 10 centres of the images:", centres)
    print("Dimension:", centres.shape) 
