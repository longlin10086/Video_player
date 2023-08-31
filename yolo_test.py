import cv2
import yolov5
import numpy as np


# Model
model = yolov5.load('yolov5s.pt')


cap = cv2.VideoCapture("action2.mp4")
left_x = 999999999
right_x = 0
# current_frame = 0
# cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # print(width)
    # print(height)
    # cv2.imshow('frame', frame)
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(new_frame)
    # results.show()
    table = results.pandas().xyxy[0]
    person_table = table[table['name'] == 'person']
    left_x = min(person_table['xmax'][0], person_table['xmax'][1], left_x)
    right_x = max(person_table['xmin'][0], person_table['xmin'][1], right_x)
    middle = int((left_x + right_x) / 2)

    image = np.zeros(frame.shape, np.uint8)
    image[:height, :middle] = frame[:height, :middle]
    cv2.imshow('image', image)

    if cv2.waitKey(1) == ord('q'):

        # cv2.waitKey(0)
        print(left_x)
        print(right_x)
        print(middle)
        break

cap.release()
cv2.destroyAllWindows()

# # Inference
# results = model([im1, im2], size=640) # batch of images

# # Results
# results.print()
# results.show()  # or .show()
#
# results.xyxy[0]  # im1 predictions (tensor)
# results.pandas().xyxy[0]  # im1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
