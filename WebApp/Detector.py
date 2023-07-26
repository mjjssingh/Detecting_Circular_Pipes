import cv2
import numpy as np


class PipeDetector:
    def __init__(self, img_path):
        self.img_path = img_path
        self.image = cv2.imread(img_path)
        self.gray = None
        self.hist = None
        self.cdf = None
        self.cdf_normalized = None
        self.equalised = None
        self.median = None
        self.kernel = None
        self.opening = None
        self.keypoints = None
        self.detector = None

    def grayscale(self):
        self.gray = np.dot(self.image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

    def histogram(self):
        self.hist, bins = np.histogram(self.gray, 256, [0, 256])

    def cdf_transform(self):
        self.cdf = np.cumsum(self.hist)
        self.cdf_normalized = 255 * self.cdf / self.cdf[-1]
        self.equalised = self.cdf_normalized[self.gray]
        self.equalised = self.equalised.astype(np.uint8)

    def median_filter(self, kernel_size):
        pad = kernel_size // 2
        output = np.zeros_like(self.equalised)
        padded = np.pad(self.equalised, ((pad, pad), (pad, pad)), mode='edge')
        shape = (self.equalised.shape[0], self.equalised.shape[1], kernel_size, kernel_size)
        strides = padded.strides + padded.strides
        sub_arrays = np.lib.stride_tricks.as_strided(padded, shape=shape, strides=strides)
        output = np.median(sub_arrays, axis=(2, 3)).astype(np.uint8)
        self.median = output

    def morphological_opening(self, kernel_size):
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        self.opening = cv2.morphologyEx(self.median, cv2.MORPH_OPEN, self.kernel)

    def blob_detection(self, min_circularity, min_area):
        params = cv2.SimpleBlobDetector_Params()
        params.filterByCircularity = True
        params.minCircularity = min_circularity
        params.filterByArea = True
        params.minArea = min_area
        self.detector = cv2.SimpleBlobDetector_create(params)
        self.keypoints = self.detector.detect(self.opening)

    def draw_keypoints(self):
        img_with_circles = cv2.drawKeypoints(self.image, self.keypoints, np.array([]), (0, 0, 255),
                                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return img_with_circles

    def detect(self, kernel_size=5, min_circularity=0.8, min_area=50):
        print(type(min_area), " from class")
        self.grayscale()
        self.histogram()
        self.cdf_transform()
        self.median_filter(kernel_size)
        self.morphological_opening(kernel_size)
        self.blob_detection(min_circularity, min_area)
        result = self.draw_keypoints()
        return result

    def get_gray(self):
        return self.gray

    def get_equalised(self):
        return self.equalised

    def get_median(self):
        return self.median

    def get_opening(self):
        return self.opening
