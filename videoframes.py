import cv2

# Load the mp4 file
cap = cv2.VideoCapture("Fluidosc.mp4")

# Check if video is opened
if not cap.isOpened():
    print("Could not open the video file")
    exit()

# Read the frames from the video
i = 0
while True:
    ret, frame = cap.read()

    # If there are no more frames, break the loop
    if not ret:
        break

    # Save the frame as an image file
    cv2.imwrite("frame_" + str(i) + ".png", frame)

    i += 1

# Release the video capture
cap.release()