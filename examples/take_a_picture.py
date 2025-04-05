# This script captures a single frame from the camera and saves it as an image file.
# It can be used for testing and debugging when writing software based on the camera.

import cv2

# Open the video capture (use the correct device index, e.g., 0 for default camera)
video = cv2.VideoCapture(0)

# Check if the video capture is opened successfully
if not video.isOpened():
    print("Error: Could not open video source")
    exit()

# Read and discard the first 20 frames. This is because the camera may need some time to adjust
# to the lighting conditions and focus properly.
for _ in range(20):
    video.read()

# Capture the 21st frame
ret, frame = video.read()

if ret:
    cv2.imwrite("captured_frame.jpg", frame)
    print("Successfully captured a frame and saved it as 'captured_frame.jpg'")
else:
    print("Error: Could not read frame")

# Release the video capture
video.release()
