import cv2
img = cv2.imread('computer-vision-with-python/DATA/00-puppy.jpg')
while True:
    cv2.imshow('puppy',img)
    
    if cv2.waitKey(1)==ord('q'):
        break
        
cv2.destroyAllWindows()