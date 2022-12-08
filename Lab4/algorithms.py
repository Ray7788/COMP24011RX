#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cv2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist_thresholding(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k = len(des1))
    matchSet = []

    for i in range(0,len(matches)):
        matches_curr = []
        for match in matches[i]:
            if match.distance < threshold_value:
                matches_curr.append(match)
            else:
                break
        matchSet.append(matches_curr)
    return matchSet

def nn(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k = 1)
    matchSet = []
    
    for i in range(0,len(matches)):
        matches_curr = []
        for match in matches[i]:
            if threshold_value == -1:
                matches_curr.append(match[i][0])
        matchSet.append(matches_curr)
    return matchSet


def nndr(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    return []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
