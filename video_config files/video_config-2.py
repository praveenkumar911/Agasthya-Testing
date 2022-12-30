import cv2
import json

JSON_PATH = "video_config files\\video_config.json"
IMG_PATH = "video_config files\\cv.jpg"

# cap = cv2.VideoCapture(0)
with open(JSON_PATH, "r") as f:
    coords = json.load(f)

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    # _, photo = cap.read()  # Storing the frame in a variable photo
    photo = cv2.imread(IMG_PATH)
    h, w, _ = photo.shape
    photo = cv2.flip(photo, 1)  # Fliping the photo for mirror view
    crops = []
    for data_ind in coords:
        data = coords[data_ind]
        x1 = int(data["x1"] * w)
        x2 = int(data["x2"] * w)
        y1 = int(data["y1"] * h)
        y2 = int(data["y2"] * h)
        crop = photo[y1:y2, x1:x2].copy()
        crops += [crop]

    for i, crop in enumerate(crops):
        cv2.imshow("crop" + str(i + 1), crop)  # It will show cropu1 part in a window
cv2.destroyAllWindows()
# cap.release()
