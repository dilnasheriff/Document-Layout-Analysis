import cv2
import imutils
from transform import four_point_transform
class ExtractImage():
    def __init__(self,image,ratio,original):
        self.image=image
        self.ratio=ratio
        self.orig=original
    def canny_edge_detector(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)
        # show the original image and the edge detected image
        print("STEP 1: Edge Detection")
        cv2.imshow("Image", self.image)
        cv2.imshow("Edged", edged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return edged

    def contouring(self,edged):
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
        # loop over the contours
        for c in cnts:
	        # approximate the contour
         	peri = cv2.arcLength(c, True)
	        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	        # if our approximated contour has four points, then we
	        # can assume that we have found our screen
	        if len(approx) == 4:
		        screenCnt = approx
		        break
        # show the contour (outline) of the piece of paper
        print("STEP 2: Find contours")
        cv2.drawContours(self.image, [screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("Outline", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  

        # apply the four point transform to obtain a top-down
        # view of the original image
        warped = four_point_transform(self.orig, screenCnt.reshape(4, 2) * self.ratio)
        # convert the warped image to grayscale, then threshold it
        # to give it that 'black and white' paper effect
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        
        # show the original and scanned images
        print("STEP 3: Apply perspective transform")
        cv2.imshow("Scanned", imutils.resize(warped, height = 650))
        cv2.waitKey(0)      