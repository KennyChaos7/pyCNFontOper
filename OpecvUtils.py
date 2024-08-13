import numpy as np
import cv2
import datetime
BASE_PATH = 'static/'


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
    cv2.imwrite(BASE_PATH+output_filename, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return output_filename


def compare_img(img1path: str, img2path: str):
    img1path = BASE_PATH + unwrap_n_replace(img_path=img1path)
    img1 = cv2.imread(img1path)
    img2 = cv2.imread(img2path)
    size = (int(500), int(500))
    img1 = cv2.resize(img1, size, cv2.INTER_AREA)
    img2 = cv2.resize(img2, size, cv2.INTER_AREA)
    img1_gray_mat = cv2.cvtColor(img1, cv2.COLOR_BGRA2GRAY, cv2.CV_8UC3)
    img2_gray_mat = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY, cv2.CV_8UC3)
    img1_hist = cv2.calcHist(img1_gray_mat, [0], None, [255], [0, 255])
    img2_hist = cv2.calcHist(img2_gray_mat, [0], None, [255], [0, 255])
    cv2.imshow("img1_gray_mat", img1_gray_mat)
    cv2.imshow("img2_gray_mat", img2_gray_mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # ssim = cv2.compareHist(img1_hist, img2_hist, cv2.HISTCMP_CORREL)
    diff = cv2.absdiff(img1_gray_mat, img2_gray_mat)
    mse = np.mean(diff * 2)
    return mse