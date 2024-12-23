import torch
import torch.nn as nn
import torch.optim as optim

class BinaryNet(nn.Module):
	def __init__(self):
		super(BinaryNet, self).__init__()
		self.fc1 = nn.Linear(784, 256)
		self.fc_hidden1 = nn.Linear(256, 128)
		self.fc_hidden2 = nn.Linear(128, 128)
		self.fc2 = nn.Linear(128, 10)
	def binarize_weights(self, weights):
		return torch.sign(weights)  # Binariza los pesos a -1 o 1
	def forward(self, x):
	    x = self.fc1(x)
	    x = torch.relu(x)  
	    x = self.fc_hidden1(x)
	    x = torch.relu(x)  
	    x = self.fc_hidden2(x)
	    x = torch.relu(x)
	    x = self.fc2(x)
	    return x



# Crear un modelo
model = BinaryNet()

# Definir el optimizador y la función de pérdida
optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# Dummy data para prueba
inputs = torch.randn(64, 784)  # Batch de 64 muestras, cada una con 784 características
labels = torch.randint(0, 10, (64,))  # Etiquetas para un problema de clasificación de 10 clases

# Entrenamiento básico
for i in range(0,100):
	optimizer.zero_grad()
	output = model(inputs)  # Realizar forward pass
	loss = criterion(output, labels)  # Calcular la pérdida
	loss.backward()  # Backpropagation
	optimizer.step()  # Actualización de parámetros
	print(f"Loss: {loss.item()}")
