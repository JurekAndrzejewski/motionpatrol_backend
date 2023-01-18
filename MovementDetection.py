import cv2

def MovementDetection(image, prev_image, parent):
    img = image.copy()
    prev_img = prev_image.copy()
    no_changes_img = img.copy()
    current_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    current_frame = cv2.GaussianBlur(src=current_frame, ksize=(5,5), sigmaX=0)
    
    previous_frame = cv2.cvtColor(prev_img, cv2.COLOR_BGR2GRAY)
    previous_frame = cv2.GaussianBlur(src=previous_frame, ksize=(5,5), sigmaX=0)


    diff_frame = cv2.absdiff(src1=current_frame, src2=previous_frame)

    thresh_frame = cv2.threshold(src=diff_frame, thresh=40, maxval=255, type=cv2.THRESH_BINARY)[1]
    
    contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE, )
    
    #cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    
    contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

            # draw the biggest contour (c) in green
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(img,(0,0),(640,475),(0,0,255),5)
    
    return img, no_changes_img

