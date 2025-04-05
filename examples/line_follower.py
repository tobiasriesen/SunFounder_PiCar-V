# This is a simple line follower program for the SunFounder PiCar-V

# Import the required libraries
from time import sleep
from picar import front_wheels, back_wheels
import picar
import cv2
import numpy as np

# Constants
SCREEN_WIDTH = 160 # The width of the camera image in pixels
SCREEN_HIGHT = 120 # The height of the camera image in pixels
MOTOR_SPEED = 50 # The speed of the motor (0-100)
ANGLE_FACTOR = 0.45 # The factor to convert the position of the line to a steering angle
LINE_RECOGNITION_THRESHOLD = 100 # The threshold for the line recognition algorithm (0-255)
DARK_LINE = True # Set this to False when using a bright line on a dark background

# Setup the picar library
picar.setup()

# Start the opencv video capture
img = cv2.VideoCapture(-1)
if not img.isOpened:
    print("Error: Could not open video source")
    exit()
print("Video source opened successfully")
img.set(3,SCREEN_WIDTH)
img.set(4,SCREEN_HIGHT)

# Initialize the components of the car
bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()

# Setup the motor and servo
bw.speed = MOTOR_SPEED
fw.turn(0)

def main():
    line_center_index = SCREEN_WIDTH/2

    # Read and discard the first 20 frames. This is because the camera may need some time to adjust
    # to the lighting conditions and focus properly.
    for _ in range(20):
        img.read()

    # Loop running forever
    while True:
        # Read the image from the camera. bgr_image is then a numpy array of shape (120, 160, 3)
        _, bgr_image = img.read()

        # Sum over the three color channels to get a grayscale image of shape (120, 160)
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

        # Sum over the bottom 10 rows to get a 1D array of shape (160,)
        brightness_distribution = np.mean(gray_image[-10:,:], axis=0)

        # Find the columns of the image where the line is located, i.e., where the brightness
        # exceeds the line recognition threshold.
        if DARK_LINE:
            line_indices = np.where(brightness_distribution < LINE_RECOGNITION_THRESHOLD)[0]
        else:
            line_indices = np.where(brightness_distribution > LINE_RECOGNITION_THRESHOLD)[0]

        # Calculate the column of the line as the average index of columns where the brightness
        # exceeds the line recognition threshold. When the threshold is not exceeded, the
        # line_indices is an empty array and the line_center_index is not updated.
        if line_indices.size != 0:
            line_center_index = np.mean(line_indices)

        # Calculate the turning angle proportional to the distance of the line from the center
        # of the image.
        turn_angle = (line_center_index - SCREEN_WIDTH/2) * ANGLE_FACTOR

        # Update the steering angle of the car
        fw.turn(turn_angle + 90) # For some reason, 90 means straight

# Stop the motor when the program is interrupted with ctrl+c
# When the program stops for any other reason, the motor will continue to run.
def destroy():
    bw.stop()

# Start the program
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
