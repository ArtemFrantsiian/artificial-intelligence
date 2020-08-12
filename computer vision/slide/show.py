import cv2 as cv
from os import listdir
from pathlib import Path
import numpy as np

path_to_folder = (Path(__file__).parent / "static").resolve()
images = listdir(path_to_folder)

img1 = cv.imread(str(path_to_folder / images[0]))
shape = (img1.shape[1], img1.shape[0])

for i in range(1, len(images)):
    img2 = cv.resize(cv.imread(str(path_to_folder / images[i])), shape)

    for d in np.arange(0.0, 1.0, 0.01):
        dst = cv.addWeighted(img1, 1.0 - d, img2, d, 0)
        cv.imshow('dst', dst)
        cv.waitKey(30)

    img1 = img2
    cv.waitKey(600)

cv.destroyAllWindows()
