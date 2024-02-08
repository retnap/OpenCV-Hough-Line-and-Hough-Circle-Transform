import cv2 
import numpy as np 

img = cv2.imread("C:\\Users\\Selman\\Desktop\\Tasarim-1\\h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#canny func. Its task is to detect the corners in the image.
edges = cv2.Canny(gray, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50)
#will draw the corners, edges value, theta and ro value, threshold value
#If you put maxLineGap = 200 at the end, it will fill the undrawn spaces in between up to 200.

for line in lines:
    x1, y1, x2, y2 = line[0]  #x1,y1,x2,y2 starting and ending points of the line
    #First we want to access line[0] because the start and end points are there
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("img", img)


cv2.imshow("gray", gray)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()