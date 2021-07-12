# read, display and save a video
import cv2

cap = cv2.VideoCapture('vtest.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret ==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #for gray scale video

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()