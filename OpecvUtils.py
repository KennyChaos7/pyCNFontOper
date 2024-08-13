import numpy as np
import cv2
import datetime


def unwrap_n_replace(img_path: str):
    img = cv2.imread(img_path)
    gray_mat = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    _, mask = cv2.threshold(gray_mat, 50.0, 255.0, cv2.THRESH_BINARY)
    img[mask > 0] = [0, 0, 0]
    img[mask == 0] = [55, 67, 188]
    # cv2.imshow("output_", img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    width, height, channel = img.shape
    for i in range(width):
        for j in range(height):
            b, g, r, a = img[i][j]
            if r == 0 and g == 0 and b == 0:
                img[i][j] = [0, 0, 0, 0]
    # cv2.imshow("output", img)
    output_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    cv2.imwrite('templates/upload_file/png/'+output_filename, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return output_filename

