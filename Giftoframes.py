import cv2

# Load the gif
cap = cv2.VideoCapture("Vortexanimation.gif")

# Get the number of frames in the gif
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop through the frames
for i in range(num_frames):
    # Get the current frame
    ret, frame = cap.read()

    # Save the current frame as an image file
    cv2.imwrite("frame_{}.png".format(i), frame)

# Release the video capture
cap.release()