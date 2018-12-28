#pip install opencv-python
#pip install opencv-contrib-python==3.4.2.16
import cv2
import numpy as np
import glob

original = cv2.imread("www.tech.gov.sg/2018-12-27 18:55:02.357438.png")

sift = cv2.xfeatures2d.SIFT_create()
keypoints_ori, desc_ori = sift.detectAndCompute(original, None)

for image in  glob.iglob("www.tech.gov.sg/*"):
    print(image)
    compare = cv2.imread(image)

    keypoints_comp, desc_comp = sift.detectAndCompute(compare, None) 

    print("1st Image Keypoints: ", len(keypoints_ori))
    print("2nd Image Keypoints: ", len(keypoints_comp))

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_ori, desc_comp, k=2)
    #print(len(matches))    

    goodpoints = []

    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            goodpoints.append(m)

    print("Good Matches: ", len(goodpoints))

    keypoints = min(len(keypoints_ori), len(keypoints_comp))

    print("Match Quality: ", len(goodpoints)/keypoints * 100, "%")
    print()

    #result = cv2.drawMatches(original, keypoints_ori, compare, keypoints_comp, goodpoints, None)

    #cv2.imshow("result", cv2.resize(result, None, fx=0.15, fy=0.15))

# cv2.imshow("Original", original)
# cv2.imshow("Duplicate", compare)
# cv2.waitKey(0)
# cv2.destroyAllWindows()