import cv2
from glob import glob
file_list = glob("x:/*-S0*.*")
file_list.sort()
file_list = [x.split("/")[-1] for x in file_list]
print(len(file_list))
from tqdm import tqdm



for file in tqdm(file_list):
    vid_cap = cv2.VideoCapture(r"x:/" + file)
    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame = int(round(vid_cap.get(cv2.CAP_PROP_FPS)))
    file_name = file.split(".")
    file_name = file_name[0]

    while vid_cap.isOpened():
        ret, image = vid_cap.read()
        image = cv2.resize(image, (w, h))
        if int(vid_cap.get(1)) % (frame * 60) == 0:
            # print('Saved frame number : ' + str(int(vid_cap.get(1))))
            cv2.imwrite("test/"+file_name+"-IMG.png", image)
            break
    vid_cap.release()
    # print(file_name)
