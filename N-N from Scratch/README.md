# 🧠 Neural Network From Scratch — Digit Recognition

## Overview
Built a complete Neural Network using only NumPy — no 
TensorFlow, no Keras, no deep learning libraries.
Implemented every component manually including forward 
propagation, backpropagation, ReLU, Softmax and gradient descent.

Achieved 95.56% accuracy on sklearn's Digits dataset — 
recognizing handwritten digits 0-9.

## Results
| Metric | Value |
|--------|-------|
| Test Accuracy | 95.56% |
| Dataset | Sklearn Digits |
| Samples | 1797 |
| Image Size | 8x8 pixels |
| Classes | 10 (digits 0-9) |

## Architecture
Input (64) → Hidden Layer (64, ReLU) → Output (10, Softmax)

## Why From Scratch?
Anyone can call model.fit(). Building from scratch proves 
you understand what happens inside the black box.
This project demonstrates understanding of:
- How neurons actually compute
- Why activation functions are needed
- How backpropagation calculates gradients
- Why gradient descent works

## Mathematics Implemented

### Forward Propagation
Z1 = X · W1 + b1
A1 = ReLU(Z1)
Z2 = A1 · W2 + b2
A2 = Softmax(Z2)

### Activation Functions
ReLU(z) = max(0, z)
Softmax(zi) = e^zi / Σe^zj

### Loss Function — Cross Entropy
Loss = -1/m × Σ log(A2[i, yi])

### Backpropagation
dZ2 = A2 - Y_onehot
dW2 = 1/m × A1^T · dZ2
db2 = 1/m × Σ dZ2
dZ1 = (dZ2 · W2^T) × ReLU'(Z1)
dW1 = 1/m × X^T · dZ1
db1 = 1/m × Σ dZ1

### Gradient Descent
W = W - α × dW
b = b - α × db

## Built From Scratch
- Forward Propagation
- ReLU activation function
- Softmax activation function
- Cross Entropy Loss
- Backpropagation — full chain rule implementation
- Gradient Descent optimizer

## Comparison With Libraries
| Model | Accuracy |
|-------|----------|
| Neural Network From Scratch | 95.56% |
| sklearn MLPClassifier (default) | ~95% |

Our scratch implementation matches library performance!

## Key Concepts Learned
- Forward propagation — how data flows through network
- ReLU — why we need non-linear activation functions
- Softmax — converting outputs to probabilities for multiclass
- Cross Entropy Loss — measuring multiclass prediction error
- Backpropagation — chain rule to calculate gradients
- One-hot encoding — why we encode labels this way
- Matrix transpose — role in gradient calculations

## Why These Design Choices
- ReLU over Sigmoid — faster training, no vanishing gradient
- Softmax output — multiclass classification needs probabilities
- 64 hidden neurons — matches input size, good balance
- Cross Entropy — standard loss for classification

## Libraries Used
- NumPy — entire implementation
- Matplotlib — visualizations
- Sklearn — dataset loading only
