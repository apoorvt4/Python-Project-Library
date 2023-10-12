import cv2
image = cv2.imread('azamat-esmurziyev-7YD8af-OobI-unsplash.jpg') # is line se image seprate folder me chale jayge 
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # this line me image one line space me colour karege
invert = cv2.bitwise_not(grey_img)  
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur) # Yeah line sharp edges banayge or smooth bhi
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("sketch.png", sketch) # yeah line jo name likha h wo name se folder banayege jaha sketch save hoga