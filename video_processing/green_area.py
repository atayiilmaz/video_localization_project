import cv2
import numpy as np

def detect_green_area(frame):
    """Detects the largest green area in a video frame and returns its bounding box."""
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])
    
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        return (x, y, w, h)
    
    return None
