

import keyboard
import cv2
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
cap = cv2.VideoCapture(0)
_, image = cap.read() 
original_image = cv2.flip(image, 1)  # Fliping the photo for mirror view
oriImage =original_image.copy()
cap.release
#image = cv2.imread('image.png')
#oriImage = image.copy()

def mouse_crop(event, x, y, flags, param):
    #grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
        # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
        
            # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
        refPoint = [(x_start, y_start), (x_end, y_end)]
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            dimensions=oriImage.shape # Taking dimensions of original image
            #print(dimensions)
            cx=dimensions[0]
            cy=dimensions[1]
            up_points = (cy,cx)
            resized_up = cv2.resize(roi, up_points, interpolation= cv2.INTER_LINEAR) #resizing the image based on main coordinates
            cv2.imwrite('crop.png',resized_up)
            image2 = cv2.imread('crop.png')
            window_name='new'
            cv2.imshow(window_name,image2)
            #keyboard.add_hotkey('m',lambda:cv2.imshow(window_name,image2))
            #showing resized cropped image with a window name called new
            
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)
#keyboard.add_hotkey('enter', lambda:cv2.setMouseCallback("image", mouse_crop) )

while True:
    i = image.copy()
    if not cropping:
        cv2.imshow("image", image)
    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("image", i)
    key = cv2.waitKey(1)
    
    # Close program with keyboard 'q'
    if key == ord('q'):
        cv2.imshow('image-zoom',image)
    elif key==ord('m'):
        cv2.destroyWindow('image')
        break
    elif key==('r'):
        cv2.destroyAllWindows()
        
        
