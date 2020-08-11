import cv2 as cv
from pathlib import Path

red_removed = False
drawing = False
ix, iy = -1, -1
r, g, b = 0, 0, 0
size = 5


def nothing(x):
    pass


def set_image(image):
    def draw_circle(event, x, y, flags, param):
        global ix, iy, drawing, r, g, b, size

        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing:
                cv.circle(image, (x, y), size, (b, g, r), -1)
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            cv.circle(image, (x, y), size, (b, g, r), -1)

    return draw_circle


directory = (Path(__file__).parent / "static").resolve()
path_to_file = str(directory / "example.png")
img = cv.resize(cv.imread(path_to_file), (0, 0), fx=0.5, fy=0.5)
red = img[:, :, 2].copy()
height, weight, _ = img.shape

cv.namedWindow("draw")
cv.setMouseCallback("draw", set_image(img))

cv.createTrackbar("R", "draw", r, 255, nothing)
cv.createTrackbar("G", "draw", g, 255, nothing)
cv.createTrackbar("B", "draw", b, 255, nothing)
cv.createTrackbar("Size", "draw", size, 10, nothing)

while True:
    cv.imshow("draw", img)
    k = cv.waitKey(1)

    if k == ord("t"):
        center = height // 2
        cv.line(img, (0, center), (weight, center), (b, g, r), size)

    if k == ord("s"):
        cv.imwrite(str(directory / "example(1).png"), img)
        break

    if k == ord("q"):
        break

    if k == ord("r"):
        if red_removed:
            img[:, :, 2] = red
        else:
            red = img[:, :, 2].copy()
            img[:, :, 2] = 0
        red_removed = not red_removed

    r = cv.getTrackbarPos("R", "draw")
    g = cv.getTrackbarPos("G", "draw")
    b = cv.getTrackbarPos("B", "draw")
    size = cv.getTrackbarPos("Size", "draw")

cv.destroyAllWindows()
