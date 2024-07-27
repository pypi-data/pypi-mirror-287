# TFLite Image Classification Broker

This library provides a simple interface for image classification using TensorFlow Lite models. It's designed to work with pre-trained models and can process both single images and directories of images.

## Installation

```bash
pip install imBroker
```

## Features

- Single image classification
- Batch classification for directories
- Support for custom TFLite models
- Handles any type of image shapes

## Usage

### Initializing the Broker

```python
from imBroker import tflBroker

# Define your TFlite model's path
model_path = "path/to/your/model.tflite"

# Define your output labels
output_labels = {
    0: 'Label 1',
    1: 'Label 2',
    ... 
}

# Initialize the broker
broker = tflBroker(model_path, output_labels)
```

### Classifying a Single Image

```python
result = broker.predict_single_image("path/to/image.jpg")
print(result)
```

### Classifying a Directory of Images

```python
results = broker.predict_image_directory("path/to/image/directory")
print(results)
```