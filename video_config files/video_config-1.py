import cv2
import json

JSON_PATH = "video_config files\\video_config.json"
IMG_PATH = "video_config files\\cv.jpg"


class DrawLineWidget(object):
    def __init__(self):
        # cap = cv2.VideoCapture(0)
        # _, photo = cap.read()  # Storing the frame in a variable photo
        photo = cv2.imread(IMG_PATH)
        self.original_image = cv2.flip(photo, 1)  # Fliping the photo for mirror view
        self.clone = self.original_image.copy()
        # cap.release()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.extract_coordinates)
        self.h, self.w, _ = self.original_image.shape
        # List to store start/end points
        self.image_coordinates = [0, 0, 0, 0]
        self.dict_main = {}
        self.dict_main["coords"] = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [x, y, x, y]
            self.left_hold = True
        elif event == cv2.EVENT_MOUSEMOVE and self.left_hold:
            self.image_coordinates[2], self.image_coordinates[3] = x, y
        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.left_hold = False
            self.image_coordinates.append((x, y))
            print(
                "Starting: {}, Ending: {}".format(
                    self.image_coordinates[0], self.image_coordinates[1]
                )
            )

            # storing all the coordinate values and pushing into an external json file
            self.list_coordinates = []
            self.dict = {}

            # Draw line
            for i in self.image_coordinates[0]:
                self.list_coordinates.append(i)
            for j in self.image_coordinates[1]:
                self.list_coordinates.append(j)

            self.dict["x1"] = self.list_coordinates[0] / self.w
            self.dict["x2"] = self.list_coordinates[2] / self.w
            self.dict["y1"] = self.list_coordinates[1] / self.h
            self.dict["y2"] = self.list_coordinates[3] / self.h

            self.dict_main["coords"] += [self.dict.copy()]
            cv2.rectangle(
                self.clone,
                self.image_coordinates[0],
                self.image_coordinates[1],
                (36, 255, 12),
                2,
            )

            # image = cv2.line(image, start_point, end_point, color, thickness)
            cv2.imshow("image", self.clone)
        with open(JSON_PATH, "w") as outfile:
            json.dump(self.dict_main, outfile)


if __name__ == "__main__":
    draw_line_widget = DrawLineWidget()
    while True:
        cv2.imshow("image", draw_line_widget.clone)
        key = cv2.waitKey(1)
        # Close program with keyboard 'q'
        if key == ord("q"):
            cv2.destroyAllWindows()
            exit(1)
