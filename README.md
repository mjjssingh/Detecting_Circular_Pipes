
# Cirular Pipe Detection Web Application

This project is a web application that allows users to upload an image and detect pipes in it using image processing techniques. The application is built using Python, Flask, and OpenCV.


## Dependencies

To run this project, you will need the following dependencies:

- Python 3.x
- Flask
- OpenCV (cv2)

## Installation

1. Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/pipe-detection-web-app.git
cd pipe-detection-web-app
```

2. Install the required Python packages using pip:
```bash
pip install flask opencv-python
```

## Usage

1. Start the Flask web server:
```bash
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000/`. The web application will be displayed.

3. Upload Image: Click the "Choose File" button to select an image file (supported formats: png, jpg, jpeg). Then, click the "Upload" button to upload the image to the web application.

4. Detect Pipes: After the image is uploaded, you can specify the minimum area (in pixels) of pipes to be detected. The application will process the image using image processing techniques, detect the pipes, and display the result.

5. Result: The processed image with detected pipes will be displayed below the upload form.

## How it Works
The web application uses the Flask framework to handle user requests and render HTML templates. The main functionality of detecting pipes is implemented in the `PipeDetector` class in the `Detector.py` file.

1. **Upload Image**: Users can upload an image from their local machine using the web application's file upload feature.

2. **Image Processing**: Once the image is uploaded, the `PipeDetector` class processes the image using the following steps:

- Grayscale Conversion: The image is converted to grayscale using the weighted sum of RGB channels.
- Histogram Equalization: The histogram of the grayscale image is equalized to enhance the contrast.
- Median Filtering: A median filter is applied to the equalized image to remove noise and smooth the image.
- Morphological Opening: A morphological opening operation is performed to remove small objects and preserve the pipe-like structures.
- Blob Detection: Blob detection is applied to find connected regions in the processed image that correspond to pipes.
3. **Result**: The processed image with the detected pipes is displayed to the user on the web page.

## Limitations

The pipe detection algorithm may not be optimal for all types of images and pipe configurations. The performance may vary based on the quality and complexity of the input image. Fine-tuning the parameters such as the kernel size and minimum area for blob detection may be required for different images.

