# Medicine Counter Box

A Computer Vision application designed to classify and count medicine boxes using deep learning. This project leverages a pre-trained Keras model to identify specific medicine brands (Napa, Ranitidine, Seclo) from images.

## Features

*   **Image Classification**: Identify medicine brands from images.
*   **Confidence Scoring**: Provides a confidence score for each prediction.
*   **Supported Medicines**:
    *   Napa
    *   Ranitidine
    *   Seclo
*   **Lightweight**: Can run on CPU (GPU disabled by default).

## Technologies Used

*   **Language**: Python 3.8
*   **Deep Learning**: TensorFlow 2.4.0, Keras 2.4.3
*   **Image Processing**: Pillow (PIL), NumPy
*   **Model Format**: `.h5` (Keras HDF5)

## Prerequisites

To run this project, you need **Python 3.8**.

### Installing Python 3.8 on Ubuntu 20.04/22.04+

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8 python3.8-venv python3.8-dev
```

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd medicine-counter-box
    ```

2.  **Create a virtual environment**:
    ```bash
    python3.8 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Prepare your image**:
    Ensure you have an image you want to classify (e.g., in `dataset/napa/3.jpg`).

2.  **Run the script**:
    ```bash
    python app.py
    ```

3.  **Output**:
    The script will print the predicted class and the confidence score.
    ```text
    Class: Napa
    Confidence Score: 0.998
    ```

## Project Structure

*   `app.py`: Main script to load the model and run predictions.
*   `keras_model.h5`: The pre-trained Deep Learning model.
*   `labels.txt`: List of class names (indices mapping to medicine names).
*   `requirements.txt`: List of Python dependencies.
*   `dataset/`: Directory containing sample images for testing/training.

## Dataset & Training

The model was trained using [Teachable Machine](https://teachablemachine.withgoogle.com/).

### Dataset Structure
If you wish to retrain the model, structure your dataset as follows:
```
dataset/
├── napa/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
├── ranitidine/
│   ├── ...
└── seclo/
    └── ...
```
