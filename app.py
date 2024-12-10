import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to preprocess the image
def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image. Check the file path.")
        exit()
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format for Matplotlib

# Function to apply Gaussian Blur
def apply_gaussian_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

# Function to apply Edge Detection
def apply_edge_detection(image):
    return cv2.Canny(image, 100, 200)

# Function to convert to Grayscale
def apply_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Function to adjust brightness
def adjust_brightness(image, alpha=1.2, beta=30):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Function to apply Sepia Effect
def apply_sepia(image):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_filter)
    return np.clip(sepia_image, 0, 255).astype(np.uint8)

# Function to rotate the image
def rotate_image(image, angle=45):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

# Function to draw a rectangle
def draw_rectangle(image):
    image_with_rectangle = image.copy()
    cv2.rectangle(image_with_rectangle, (50, 50), (200, 200), (255, 0, 0), 3)  # Blue rectangle
    return image_with_rectangle

# Function to add text to the image
def add_text(image, text="Hello, Tasnim!"):
    image_with_text = image.copy()
    cv2.putText(image_with_text, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Green text
    return image_with_text

# Display the image using Matplotlib
def display_image(image, title="Image", cmap=None):
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    # Load the image
    image_path = "./images/83f62d89-5df0-4fde-a211-59d69a205525.jpg"  # Change this to your image path
    original_image = load_image(image_path)

    # Display original image
    display_image(original_image, "Original Image")

    # Apply different effects
    blurred_image = apply_gaussian_blur(original_image)
    display_image(blurred_image, "Gaussian Blur")

    edge_image = apply_edge_detection(original_image)
    display_image(edge_image, "Edge Detection", cmap="gray")

    grayscale_image = apply_grayscale(original_image)
    display_image(grayscale_image, "Grayscale", cmap="gray")

    bright_image = adjust_brightness(original_image)
    display_image(bright_image, "Brightened Image")

    sepia_image = apply_sepia(original_image)
    display_image(sepia_image, "Sepia Effect")

    rotated_image = rotate_image(original_image, angle=90)
    display_image(rotated_image, "Rotated Image")

    rectangle_image = draw_rectangle(original_image)
    display_image(rectangle_image, "Rectangle on Image")

    text_image = add_text(original_image, text="AI Recognition System")
    display_image(text_image, "Text on Image")
