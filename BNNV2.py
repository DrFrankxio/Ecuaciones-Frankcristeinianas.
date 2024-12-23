import torch
import torch.nn as nn
import torch.optim as optim

class BinaryNet(nn.Module):
    def __init__(self):
        super(BinaryNet, self).__init__()
        self.fc1 = nn.Linear(784, 2**10)
        self.fc_hidden1 = nn.Linear(2**10, 2**10)
        self.fc_hidden2 = nn.Linear(2**10, 2**10)
        self.fc_hidden3 = nn.Linear(2**10, 2**10)
        self.fc2 = nn.Linear(2**10, 10)
        self._initialize_weights()  # Inicialización personalizada

    def _initialize_weights(self):
        # Función de inicialización de pesos (puedes modificar esto)
        for layer in self.children():
            if isinstance(layer, nn.Linear):
                nn.init.kaiming_uniform_(layer.weight, nonlinearity='relu')
                nn.init.zeros_(layer.bias)

    def binarize_weights(self, weights):
        # Binariza los pesos a -1 o 1
        return torch.sign(weights)

    def forward(self, x):
        x = self.fc1(x)
        x = torch.relu(x)  
        x = self.fc_hidden1(x)
        x = torch.relu(x)  
        x = self.fc_hidden2(x)
        x = torch.relu(x)  
        x = self.fc_hidden3(x)
        x = torch.relu(x)
        x = self.fc2(x)
        return x

    def train_model(self, train_loader, epochs=10, lr=0.01):
        # Función de entrenamiento
        optimizer = optim.SGD(self.parameters(), lr=lr)
        criterion = nn.CrossEntropyLoss()

        for epoch in range(epochs):
            running_loss = 0.0
            for inputs, labels in train_loader:
                optimizer.zero_grad()  # Resetear los gradientes
                outputs = self(inputs)  # Forward pass
                loss = criterion(outputs, labels)  # Pérdida
                loss.backward()  # Backpropagation
                optimizer.step()  # Actualización de los pesos
                running_loss += loss.item()

            print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader)}")

# Suponiendo que tengas un DataLoader, por ejemplo:
from torch.utils.data import DataLoader, TensorDataset

# Dumma tu lela:
inputs = torch.randn(2**10, 784)# 784 neuronas de input.
labels = torch.randint(0, 10, (2**10,))#10 neuronas de output.

# Crear DataLoader
train_loader = DataLoader(TensorDataset(inputs, labels), batch_size=32, shuffle=True)

# Crear y entrenar el modelo
model = BinaryNet()
model.train_model(train_loader, epochs=10, lr=0.01)
