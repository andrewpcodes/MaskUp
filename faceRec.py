# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2

cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("cascades/frontal_face.xml")
mouthCascade = cv2.CascadeClassifier("cascades/Mouth.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(10, 10)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)
	# Detect the Mouths in the picture
	mouths = mouthCascade.detectMultiScale(
		gray,
		scaleFactor=1.3,
		minNeighbors=8,
		minSize=(6, 6)
	)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	for (x, y, w, h) in mouths:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
