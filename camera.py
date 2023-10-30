import cv2
import os
import argparse

def capture_image(directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Access the default camera
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        return

    # Save the frame to the specified directory
    filename = os.path.join(directory, "image.jpg")
    cv2.imwrite(filename, frame)

    # Release the camera
    cap.release()

    print(f"Image saved to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture an image from the camera and save it to a directory.")
    parser.add_argument("directory", help="The directory where the image will be saved")

    args = parser.parse_args()
    capture_image(args.directory)
