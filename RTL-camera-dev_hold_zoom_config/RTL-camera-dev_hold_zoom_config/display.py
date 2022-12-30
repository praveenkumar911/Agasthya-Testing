import cv2
import json

CONFIG_PATH = "config.json"
with open(CONFIG_PATH, "r") as outfile:
    config_dict = json.load(outfile)


IMG_PATH = config_dict["IMG_PATH"]
JSON_PATH = config_dict["SAVE_PATH"]
DEV = config_dict["DEV"]
SCALE_RATIO = config_dict["RESCALE_RATIO"]
WIDTH = int(config_dict["WIDTH"] * SCALE_RATIO)
HEIGHT = int(config_dict["HEIGHT"] * SCALE_RATIO)
DISPLAY_RESIZE = config_dict["DISPLAY_RESIZE"]
CAMERA_INDEX = int(config_dict["CAMERA_INDEX"])

if not DEV:
    cap = cv2.VideoCapture(CAMERA_INDEX)
with open(JSON_PATH, "r") as f:
    coords = json.load(f)

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if DEV:
        photo = cv2.imread(IMG_PATH)
    else:
        _, photo = cap.read()
    h, w, _ = photo.shape
    photo = cv2.flip(photo, 1)
    crops = []
    for data_ind in coords:
        data = coords[data_ind]
        x1 = int(data["x1"] * w)
        x2 = int(data["x2"] * w)
        y1 = int(data["y1"] * h)
        y2 = int(data["y2"] * h)
        crop = photo[y1:y2, x1:x2].copy()
        if DISPLAY_RESIZE:
            crop = cv2.resize(crop, (WIDTH, HEIGHT))
        crops += [crop]

    for i, crop in enumerate(crops):
        cv2.imshow("image" + str(i + 1), crop)
cv2.destroyAllWindows()
if not DEV:
    cap.release()
