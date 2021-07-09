import cv2
vidcap = cv2.VideoCapture('/home/ncbc/Desktop/WorkSpace_NCBC/Hand Glove Detection/yolov5-develop/Gloves/Gloves dataset/unglove.mp4')
count = 0
success = True
image= True
while success:
  cv2.imwrite("/f2mee%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

