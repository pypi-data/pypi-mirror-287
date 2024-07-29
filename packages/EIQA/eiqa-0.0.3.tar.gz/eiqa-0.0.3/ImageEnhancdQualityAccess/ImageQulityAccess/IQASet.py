import cv2
#import numba
import numpy as np
import onnxruntime as ort
from PIL import Image
from torchvision import transforms
from skimage import filters
from typing import Dict,List,Tuple

class IQASet(object):
    def __init__(self,GPUproviders:bool,MedianBlur:bool,ModelPath:str):
        self.DeviceProviders = 'CUDAExecutionProvider' if GPUproviders else 'CPUExecutionProvider'
        self.ModelPath = ModelPath
        self.MedianBlur = MedianBlur
    #@numba.jit()
    def blurDetection(self, Image_array:np.array)->float:
        Img2gray = Image_array = self._preImgOps(Image_array,True)
        f = Img2gray/255.0
        x, y = Img2gray.shape
        score = 0
        for i in range(x - 2):
            for j in range(y - 2):
                score += (f[i + 2, j] - f[i, j]) ** 2
        score=score/10
        return score
    
    #@numba.jit()
    def SMDDetection(self, Image_array:np.array)->float:
        Img2gray= Image_array = self._preImgOps(Image_array,True)
        f=Img2gray/255.0
        x, y = f.shape
        score = 0
        for i in range(x - 1):
            for j in range(y - 1):
                score += np.abs(f[i+1,j]-f[i,j])+np.abs(f[i,j]-f[i+1,j])
        score=score/100
        return score
    
    #@numba.jit()
    def SMD2Detection(self, Image_array:np.array)->float:
        Img2gray = Image_array = self._preImgOps(Image_array,True)
        f=Img2gray/255.0
        x, y = f.shape
        score = 0
        for i in range(x - 1):
            for j in range(y - 1):
                score += np.abs(f[i+1,j]-f[i,j])*np.abs(f[i,j]-f[i,j+1])
        return score

    #@numba.jit()
    def Vollath(self,Image_array:np.array)->float:
        Img2gray = Image_array = self._preImgOps(Image_array,True)
        source=0
        x,y=Img2gray.shape
        for i in range(x-1):
            for j in range(y):
                source+=Img2gray[i,j]*Img2gray[i+1,j]
        source=source-x*y*np.mean(Img2gray)
        return source


    def Variance(self, Image_array:np.array)->float:
        Img2gray = Image_array = self._preImgOps(Image_array,True)
        score = np.var(Img2gray)
        return score
    

    #引用算子，注意由于电子器械有系统噪声，大部分时间需要开启中值滤波

    #一阶梯度清晰度
    def Tenengrad(self, Image_array:np.array,MedianBlur:bool)->float:
        Image_array = self._preImgOps(Image_array,True)
        if MedianBlur:
            Img2gray = cv2.medianBlur(Img2gray, 3)
        tmp = filters.sobel(Img2gray)
        score=np.sum(tmp**2)
        score=np.sqrt(score)
        return score

    #二阶梯度清晰度
    def lapulaseDetection(self, Image_array:np.array,MedianBlur:bool)->float:
        Image_array = self._preImgOps(Image_array,True)
        if MedianBlur:
            Img2gray = cv2.medianBlur(Img2gray, 3)
        resLap = cv2.Laplacian(Img2gray, cv2.CV_64F)
        score = resLap.var()
        return score

    #饱和度，饱和度越高，图像越鲜艳
    def HSV_S(self,Image_array:np.array)->float:
        Image_array = self._preImgOps(Image_array,True)
        if Image_array.dtype != np.uint8 or len(Image_array.shape)!=3:
            raise ValueError("输入格式与类型不符")
        hsv = cv2.cvtColor(Image_array, cv2.COLOR_RGB2HSV)
        H, S, V = cv2.split(hsv)
        s = S.ravel()[np.flatnonzero(S)]
        average_s  = sum(s)/len(s)
        return  average_s  

    #像素点精确对比度
    def contrast(self,Image_array:np.array,MedianBlur:bool)->float:
        Image_array = self._preImgOps(Image_array,True)
        if MedianBlur:
            Image_array = cv2.medianBlur(Image_array, 3)
        Image_array = Image_array.astype(np.float32)
        Img_ext = cv2.copyMakeBorder(Image_array, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
        diff_up = Img_ext[1:-1, 1:-1] - Img_ext[2:, 1:-1]
        diff_down = Img_ext[1:-1, 1:-1] - Img_ext[:-2, 1:-1]
        diff_left = Img_ext[1:-1, 1:-1] - Img_ext[1:-1, :-2]
        diff_right = Img_ext[1:-1, 1:-1] - Img_ext[1:-1, 2:]
        sq_diffs = diff_up**2 + diff_down**2 + diff_left**2 + diff_right**2
        score = np.mean(sq_diffs)
        return score
     
    #网络模型评估图像质量
    def IQANet(self,Image_array:np.array)->float:
        Image_array = self._preImgOps(Image_array,False)
        transform = transforms.Compose([
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        ort_session = ort.InferenceSession(self.ModelPath, providers=[self.DeviceProviders])
        score = 0
        Image_array = Image.fromarray(Image_array)
        Image_array = transform(Image_array)
        Image_array.unsqueeze_(0)
        Image_array = Image_array.numpy().astype(np.float32)
        s_score,_ = ort_session.run(None, {'input': Image_array})
        score = float(s_score[0][0])
        return score

    def _preImgOps(self,Image_array:np.array,RGB2Gary:bool=False):
        if Image_array.dtype != np.uint8:
            raise ValueError("输入矩阵的元素类型必须为np.uint8")      
        if len(Image_array.shape)==3 and Image_array.shape[2]==3:
            if RGB2Gary:
                Image_array = cv2.cvtColor(Image_array, cv2.COLOR_BGR2GRAY)  # 将图片压缩为单通道的灰度图
            else:
                Image_array =  cv2.cvtColor(Image_array, cv2.COLOR_BGR2RGB)
        elif len(Image_array.shape)==2:
            pass
        else:
            raise ValueError("输入矩阵形状与类型不允许")    
        return Image_array
    
