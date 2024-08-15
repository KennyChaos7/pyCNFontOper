import numpy as np
import cv2
import datetime
import os
from skimage.metrics import structural_similarity
BASE_PATH = 'static/png'


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
    cv2.imwrite(os.path.join(BASE_PATH, "", output_filename), img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return output_filename


def compare_img(img1path: str, img2path: str):
    if os.path.exists(img1path) is False or os.path.exists(img2path) is False:
        return 0
    img1path = os.path.join(BASE_PATH, "", unwrap_n_replace(img_path=img1path))
    img1 = cv2.imread(img1path)
    img2 = cv2.imread(img2path)
    # cv2.imshow("img1_gray_mat", img1)
    # cv2.imshow("img2_gray_mat", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    size = (int(500), int(500))
    img1 = cv2.resize(img1, size, cv2.INTER_AREA)
    img2 = cv2.resize(img2, size, cv2.INTER_AREA)
    img1_gray_mat = cv2.cvtColor(img1, cv2.COLOR_BGRA2GRAY, cv2.CV_8UC3)
    img2_gray_mat = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY, cv2.CV_8UC3)
    # cv2.imshow("img1_gray_mat", img1_gray_mat)
    # cv2.imshow("img2_gray_mat", img2_gray_mat)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # img1_hist = cv2.calcHist(img1_gray_mat, [0], None, [255], [0, 255])
    # img2_hist = cv2.calcHist(img2_gray_mat, [0], None, [255], [0, 255])
    # ssim = cv2.compareHist(img1_hist, img2_hist, cv2.HISTCMP_CORREL)

    # diff = cv2.absdiff(img1_gray_mat, img2_gray_mat)
    # ssim = np.mean(diff * 2)

    # img_compare = cv2.compare(img1_gray_mat, img2_gray_mat, cv2.CMP_EQ)
    # cv2.imshow("img_compare", img_compare)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # img1_hist = cv2.calcHist(img1_gray_mat, [0], None, [256], [0, 255])
    # img2_hist = cv2.calcHist(img2_gray_mat, [0], None, [256], [0, 255])
    # ssim = 0
    # for i in range(len(img1_hist)):
    #     if img1_hist[i] != img2_hist[i]:
    #         ssim = ssim + (1 - (abs(img1_hist[i] - img2_hist[i]) / max(img1_hist, img2_hist)))
    #     else:
    #         ssim = ssim + 1
    # ssim = ssim / len(img1_hist)

    # sub_image1 = cv2.split(img1_gray_mat)
    # sub_image2 = cv2.split(img2_gray_mat)
    # ssim = 0
    # for i1, i2 in zip(sub_image1, sub_image2):
    #     ssim += cal2(i1, i2)
    # ssim = ssim / 3

    # ssim = np.sum((img1_gray_mat.astype("float") - img2_gray_mat.astype("float")) ** 2)
    # ssim /= float(img1_gray_mat.shape[0] * img1_gray_mat.shape[1])

    # ssim, _ = structural_similarity(img1_gray_mat, img2_gray_mat, full=True)

    # 初始化ORB检测器
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1_gray_mat, None)
    kp2, des2 = orb.detectAndCompute(img2_gray_mat, None)

    # 提取并计算特征点
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)

    # knn筛选结果
    matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

    # 查看最大匹配点数目
    good = [m for (m, n) in matches if m.distance < 0.55 * n.distance]
    print(len(good))
    print(len(matches))
    ssim = len(good) / len(matches)
    print("两张图片相似度为:%s" % ssim)
    return ssim


# def cal2(im1, im2):
#     img1_hist = cv2.calcHist(im1, [0], None, [256], [0, 255])
#     img2_hist = cv2.calcHist(im2, [0], None, [256], [0, 255])
#     ssim = 0
#     for i in range(len(img1_hist)):
#         if img1_hist[i] != img2_hist[i]:
#             ssim = ssim + (1 - (abs(img1_hist[i] - img2_hist[i]) / max(img1_hist, img2_hist)))
#         else:
#             ssim = ssim + 1
#     ssim = ssim / len(img1_hist)
#     return ssim