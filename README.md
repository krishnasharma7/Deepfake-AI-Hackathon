# Deep-Fake Detection System

This project implements a deep learning system for detecting deepfakes in images and videos. It leverages the strengths of two popular frameworks:

- **TensorFlow's MoveNet Model:** For efficient human pose estimation in video frames. This can help identify inconsistencies in movement patterns that might indicate manipulation.
- **PyTorch DenseNet169:** A powerful pre-trained convolutional neural network (CNN) for image feature extraction. This helps classify individual frames or images as real or fake.

By combining these techniques, the system aims to achieve robust and accurate deepfake detection.
