import cv2
import numpy as np
from itertools import combinations
from typing import Dict,List,Tuple

def gauss_curve(src, mean, sigma):
    dst = np.exp(-(src - mean)**2 / (2 * sigma**2))
    return dst

class ExposureFusion(object):
    def __init__(self, best_exposedness=0.5, sigma=0.2, eps=1e-12, exponents=(1.0, 1.0, 1.0), layers=7):
        self.best_exposedness = best_exposedness
        self.sigma = sigma
        self.eps = eps
        self.exponents = exponents
        self.layers = layers

    @staticmethod
    def cal_contrast(src):
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        laplace_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
        contrast = cv2.filter2D(gray, -1, laplace_kernel, borderType=cv2.BORDER_REPLICATE)
        return np.abs(contrast)

    @staticmethod
    def cal_saturation(src):
        mean = np.mean(src, axis=-1)
        channels = [(src[:, :, c] - mean)**2 for c in range(3)]
        saturation = np.sqrt(np.mean(channels, axis=0))
        return saturation

    @staticmethod
    def cal_exposedness(src, best_exposedness, sigma):
        exposedness = [gauss_curve(src[:, :, c], best_exposedness, sigma) for c in range(3)]
        exposedness = np.prod(exposedness, axis=0)
        return exposedness

    def cal_weight_map(self,sequence):
        weights = []
        for idx in range(sequence.shape[0]):
            contrast = self.cal_contrast(sequence[idx])
            saturation = self.cal_saturation(sequence[idx])
            exposedness = self.cal_exposedness(sequence[idx], self.best_exposedness, self.sigma)
            weight = np.power(contrast, self.exponents[0]) * np.power(saturation, self.exponents[1]) * np.power(exposedness, self.exponents[2])
            # Gauss Blur
            # weight = cv2.GaussianBlur(weight, (21, 21), 2.1)
            weights.append(weight)
        weights = np.stack(weights, 0) + self.eps
        # normalize
        weights = weights / np.expand_dims(np.sum(weights, axis=0), axis=0)
        return weights

    def build_gaussian_pyramid(self, high_res):
        gaussian_pyramid = [high_res]
        for idx in range(1, self.layers):
            L = cv2.GaussianBlur(gaussian_pyramid[-1], (5, 5), 0.83)[::2, ::2]
            gaussian_pyramid.append(L)
        return gaussian_pyramid

    def build_laplace_pyramid(self, gaussian_pyramid):
        laplace_pyramid = [gaussian_pyramid[-1]]
        for idx in range(1, self.layers):
            size = (gaussian_pyramid[self.layers - idx - 1].shape[1], gaussian_pyramid[self.layers - idx - 1].shape[0])
            upsampled = cv2.resize(gaussian_pyramid[self.layers - idx], size, interpolation=cv2.INTER_LINEAR)
            laplace_pyramid.append(gaussian_pyramid[self.layers - idx - 1] - upsampled)
        laplace_pyramid.reverse()
        return laplace_pyramid

    def multi_resolution_fusion(self,ImageList:List[np.array]):
        Img_num = len(ImageList)
        sequence = np.stack(ImageList, axis=0)
        sequence = sequence.astype(np.float32)/255.0
        weights = self.cal_weight_map(sequence)  # [N, H, W]
        weights = np.stack([weights, weights, weights], axis=-1)  # [N, H, W, 3]

        image_gaussian_pyramid = [self.build_gaussian_pyramid(sequence[i] * 255) for i in range(Img_num)]
        image_laplace_pyramid = [self.build_laplace_pyramid(image_gaussian_pyramid[i]) for i in range(Img_num)]
        weights_gaussian_pyramid = [self.build_gaussian_pyramid(weights[i]) for i in range(Img_num)]

        fused_laplace_pyramid = [np.sum([image_laplace_pyramid[n][l] *
                                         weights_gaussian_pyramid[n][l] for n in range(Img_num)], axis=0) for l in range(self.layers)]

        result = fused_laplace_pyramid[-1]
        for k in range(1, self.layers):
            size = (fused_laplace_pyramid[self.layers - k - 1].shape[1], fused_laplace_pyramid[self.layers - k - 1].shape[0])
            upsampled = cv2.resize(result, size, interpolation=cv2.INTER_LINEAR)
            result = upsampled + fused_laplace_pyramid[self.layers - k - 1]
        result = np.clip(result, 0, 255).astype(np.uint8)
        result = cv2.medianBlur(result, 3)
        return result
    def multi_resolution_fusion_multi_compose(self,ImageList:List,nums:int)->Dict:
        member_nums = len(ImageList)
        if member_nums==0 or ImageList is None:
            raise ValueError("输入为空,不合法")
        members = [i for i in range(len(ImageList))]
        members_groups = combinations(members,nums)
        nameDict = {}
        ImageListPart = []
        Img = None
        for members_group in members_groups:
            pathPart = list("9"+"0"*nums)
            for i in members_group:
                ImageListPart.append(ImageList[i])
                pathPart[i+1] = "1" 
            Img = self.multi_resolution_fusion(ImageListPart)    
            nameDict["".join(pathPart)] = Img
            ImageListPart.clear()
        return nameDict