import os
import cv2
path = r"x:/"
file_list = os.listdir(path)
file_list.sort()

for i in file_list:
    vid_cap = cv2.VideoCapture(r"x:/" + i)
    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame = int(round(vid_cap.get(cv2.CAP_PROP_FPS)))
    file_name = i.split(".")
    file_name = file_name[0]

    while vid_cap.isOpened():
        ret, image = vid_cap.read()
        image = cv2.resize(image, (w, h))
        if int(vid_cap.get(1)) % (frame * 60) == 0:
            print('Saved frame number : ' + str(int(vid_cap.get(1))))
            cv2.imwrite("test/"+file_name+".jpg", image)
            break
    vid_cap.release()
    print(file_name)