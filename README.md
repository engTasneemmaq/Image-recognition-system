# Image Recognition System with Effects

This project is an **Image Recognition System** built using **OpenCV**, **NumPy**, and **Matplotlib**. It allows users to apply various effects and transformations to images, including Gaussian blur, edge detection, grayscale conversion, and more.

---

## Features
- Load and process images.
- Apply multiple effects:
  - Gaussian Blur
  - Edge Detection
  - Grayscale Conversion
  - Brightness Adjustment
  - Sepia Effect
  - Image Rotation
  - Drawing Shapes (Rectangle)
  - Adding Text to Images
- Display images before and after processing.

---

## Requirements
To run this project, you need the following:
- Python 3.7+
- Libraries:
  - OpenCV
  - NumPy
  - Matplotlib

Install the required libraries using:
```bash
pip install opencv-python numpy matplotlib

```

----------

## How to Run the Project

Follow these steps to run the project:

1.  Clone the repository:
    
    ```bash
    git clone https://github.com/engTasneemmaq/Image-Recognition-System.git
    
    ```
    
2.  Navigate to the project directory:
    
    ```bash
    cd Image-Recognition-System
    
    ```
    
3.  Place your image in the `images/` folder and name it `83f62d89-5df0-4fde-a211-59d69a205525.jpg`.
4.  Run the application:
    
    ```bash
    python app.py
    
    ```
    

----------

## Project Structure

```
Image-Recognition-System/
├── app.py                 # Main application file
├── images/                # Folder for input images
│   ├── example.jpg        # Example image (replace with your own)
├── requirements.txt       # List of required libraries

```

----------

## How It Works

1.  **Load Image**: The system loads the image from the `images/` folder.
2.  **Apply Effects**:
    -   **Gaussian Blur**: Smoothens the image.
    -   **Edge Detection**: Detects edges in the image.
    -   **Grayscale**: Converts the image to black and white.
    -   **Brightness Adjustment**: Increases image brightness.
    -   **Sepia Effect**: Adds a warm, brownish tone.
    -   **Rotation**: Rotates the image by 90°.
    -   **Drawing Rectangle**: Draws a rectangle on the image.
    -   **Adding Text**: Adds custom text to the image.
3.  **Display Results**: The system displays each processed image.

----------

## Future Enhancements

-   Add a graphical user interface (GUI) for easier interaction using **Tkinter**.
-   Allow users to select images dynamically.
-   Support for batch processing multiple images at once.
-   Add more advanced effects like histogram equalization, sharpening, or perspective transformations.

----------

## Contributions

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork the repository and create a pull request.

----------

## License

This project is licensed under the MIT License.

----------


