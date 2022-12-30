import os
import cv2
import json
import keyboard

CONFIG_PATH = "config.json"
with open(CONFIG_PATH, "r") as outfile:
    config_dict = json.load(outfile)


IMG_PATH = config_dict["IMG_PATH"]
JSON_PATH = config_dict["SAVE_PATH"]
DEV = config_dict["DEV"]
QUIT_KEY = config_dict["QUIT_KEY"]
ZOOM_IN_KEY = config_dict["ZOOM_IN_KEY"]
ZOOM_OUT_KEY = config_dict["ZOOM_OUT_KEY"]
DEL_KEY = config_dict["DEL_KEY"]
SCALE_RATIO = config_dict["RESCALE_RATIO"]
WIDTH = int(config_dict["WIDTH"] * SCALE_RATIO)
HEIGHT = int(config_dict["HEIGHT"] * SCALE_RATIO)
CAMERA_INDEX = int(config_dict["CAMERA_INDEX"])
RECTANGLE_LINE_THICKNESS = config_dict["RECTANGLE_LINE_THICKNESS"]
RECTANGLE_LINE_COLOR_RED = config_dict["RECTANGLE_LINE_COLOR_RED"]
RECTANGLE_LINE_COLOR_GREEN = config_dict["RECTANGLE_LINE_COLOR_GREEN"]
RECTANGLE_LINE_COLOR_BLUE = config_dict["RECTANGLE_LINE_COLOR_BLUE"]
RECTANGLE_LINE_COLOR = (RECTANGLE_LINE_COLOR_BLUE, RECTANGLE_LINE_COLOR_GREEN, RECTANGLE_LINE_COLOR_RED)


class rtlCapture:
    def __init__(self):
        if DEV:
            main_img = cv2.imread(IMG_PATH)
        else:
            cap = cv2.VideoCapture(CAMERA_INDEX)
            _, main_img = cap.read()
            cap.release()
        main_img = cv2.resize(main_img, (WIDTH, HEIGHT))
        self.original_img = main_img.copy()
        self.main_img = main_img.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.extract_coordinates)
        self.left_hold = False
        self.interactive_coords = [0, 0, 0, 0]
        self.image = self.main_img.copy()
        self.final_coords = []
        self.h, self.w, _ = main_img.shape
        self.zoom_x, self.zoom_y, self.zoom_w, self.zoom_h = 0, 0, self.w, self.h
        self.zooming_in = False

        keyboard.add_hotkey(DEL_KEY, self.remove_last_coord)
        keyboard.add_hotkey(ZOOM_IN_KEY, self.zoom_in)
        keyboard.add_hotkey(ZOOM_OUT_KEY, self.zoom_out)

    def extract_coordinates(self, event, x, y, flags, parameters):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.interactive_coords = [x, y, x, y]
            self.left_hold = True
        elif event == cv2.EVENT_MOUSEMOVE and self.left_hold:
            (self.interactive_coords[2], self.interactive_coords[3],) = (
                x,
                y,
            )
            self.image = self.main_img.copy()
            self.image = self.draw_rect(self.image, self.interactive_coords)
        elif event == cv2.EVENT_LBUTTONUP and self.zooming_in:
            self.image = self.original_img.copy()
            self.left_hold = False
            self.zoom_x = self.interactive_coords[0]
            self.zoom_y = self.interactive_coords[1]
            self.zoom_w = self.interactive_coords[2] - self.interactive_coords[0]
            self.zoom_h = self.interactive_coords[3] - self.interactive_coords[1]
            self.image = self.image[
                self.interactive_coords[1] : self.interactive_coords[3],
                self.interactive_coords[0] : self.interactive_coords[2],
            ].copy()
            self.interactive_coords = [0, 0, 0, 0]
            self.image = cv2.resize(self.image, (WIDTH, HEIGHT))
            self.main_img = self.image.copy()
            self.zooming_in = False

        elif event == cv2.EVENT_LBUTTONUP:
            self.left_hold = False
            format_interactive_coords = self.interactive_coords.copy()
            format_interactive_coords[0] = self.zoom_x + (self.interactive_coords[0] * self.zoom_w) // self.w
            format_interactive_coords[1] = self.zoom_y + (self.interactive_coords[1] * self.zoom_h) // self.h
            format_interactive_coords[2] = self.zoom_x + (self.interactive_coords[2] * self.zoom_w) // self.w
            format_interactive_coords[3] = self.zoom_y + (self.interactive_coords[3] * self.zoom_h) // self.h

            self.final_coords += [format_interactive_coords]
            self.main_img = self.draw_rect(self.main_img, self.interactive_coords)
            self.interactive_coords = [0, 0, 0, 0]
            self.image = self.main_img.copy()

    def draw_rect(self, img, coords):
        start_point = (
            coords[0],
            coords[1],
        )
        end_point = (
            coords[2],
            coords[3],
        )
        img = cv2.rectangle(img, start_point, end_point, RECTANGLE_LINE_COLOR, RECTANGLE_LINE_THICKNESS)
        return img

    def save_coords_json(self):
        save_dict = {}
        index = 0
        w, h = self.w, self.h
        for final_coord in self.final_coords:
            index += 1
            save_dict[index] = {}
            save_dict[index]["x1"] = final_coord[0] / w
            save_dict[index]["y1"] = final_coord[1] / h
            save_dict[index]["x2"] = final_coord[2] / w
            save_dict[index]["y2"] = final_coord[3] / h
        with open(JSON_PATH, "w") as outfile:
            json.dump(save_dict, outfile)

    def remove_last_coord(self):
        self.final_coords = self.final_coords[:-1]
        self.main_img = self.original_img.copy()
        for final_rect in self.final_coords:
            self.main_img = self.draw_rect(self.main_img, final_rect)
        self.main_img = self.main_img[
            self.zoom_y : self.zoom_y + self.zoom_h,
            self.zoom_x : self.zoom_x + self.zoom_w,
        ].copy()
        self.main_img = cv2.resize(self.main_img, (WIDTH, HEIGHT))
        self.image = self.main_img.copy()

    def zoom_in(self):
        self.zooming_in = True

    def zoom_out(self):
        self.main_img = self.original_img.copy()
        for final_rect in self.final_coords:
            self.main_img = self.draw_rect(self.main_img, final_rect)
        self.image = self.main_img.copy()
        self.zooming_in = False
        self.zoom_x, self.zoom_y, self.zoom_w, self.zoom_h = 0, 0, self.w, self.h


if __name__ == "__main__":
    rc = rtlCapture()
    while True:
        cv2.imshow("image", rc.image)
        if cv2.waitKey(1) == ord(QUIT_KEY):
            cv2.destroyAllWindows()
            rc.save_coords_json()
            exit()
