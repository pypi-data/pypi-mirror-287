import numpy as np
from typing import Dict,List,Tuple

class PixelLightArrange(object):
    def __init__(self, AddWeight:bool=False):

        self.AddWeight = AddWeight
    
    def MltipixelValueRerank(self,ImageList:List)->List:
        if ImageList == None or len(ImageList) == 0 or len(ImageList) > 4:
            raise ValueError("获取数据失败")
        elif len(ImageList) == 1:
            return ImageList
        else:
            ImageList = self.__pixelValueRerank(ImageList,len(ImageList))
        return ImageList
           
 
    #size仅有2,3,4,3种可能
    def __pixelValueRerank(self,ImageList:List,size:int)->List:
        if size == 2:
            Img_channal1 = np.stack([ImageList[0][:,:,0],ImageList[1][:,:,0]],axis=2)
            Img_channal2 = np.stack([ImageList[0][:,:,1],ImageList[1][:,:,1]],axis=2)
            Img_channal3 = np.stack([ImageList[0][:,:,2],ImageList[1][:,:,2]],axis=2)
            Img_channal1 = np.sort(Img_channal1, axis=2)
            Img_channal2 = np.sort(Img_channal2, axis=2)
            Img_channal3 = np.sort(Img_channal3, axis=2)
            Img1 = np.stack([Img_channal1[:,:,0],Img_channal2[:,:,0],Img_channal3[:,:,0]],axis=2)
            Img2 = np.stack([Img_channal1[:,:,1],Img_channal2[:,:,1],Img_channal3[:,:,1]],axis=2)
            if not self.AddWeight:
                ImageList.extend([Img1,Img2])
            else:
                Img3 = (Img1+Img2)/2
                ImageList.extend([Img1,Img2,Img3])                 
        elif size ==3:
            Img_channal1 = np.stack([ImageList[0][:,:,0],ImageList[1][:,:,0],ImageList[2][:,:,0]],axis=2)
            Img_channal2 = np.stack([ImageList[0][:,:,1],ImageList[1][:,:,1],ImageList[2][:,:,1]],axis=2)
            Img_channal3 = np.stack([ImageList[0][:,:,2],ImageList[1][:,:,2],ImageList[2][:,:,2]],axis=2)
            Img_channal1 = np.sort(Img_channal1, axis=2)
            Img_channal2 = np.sort(Img_channal2, axis=2)
            Img_channal3 = np.sort(Img_channal3, axis=2)
            Img1 = np.stack([Img_channal1[:,:,0],Img_channal2[:,:,0],Img_channal3[:,:,0]],axis=2)
            Img2 = np.stack([Img_channal1[:,:,1],Img_channal2[:,:,1],Img_channal3[:,:,1]],axis=2)
            Img3 = np.stack([Img_channal1[:,:,2],Img_channal2[:,:,2],Img_channal3[:,:,2]],axis=2)
            if not self.AddAW:
                ImageList.extend([Img1,Img2,Img3]) 
            else:
                Img5 = (Img1+Img2)/2
                Img6 = (Img1+Img3)/2
                Img4 = (Img1+Img2+Img3)/3
                ImageList.extend([Img1,Img2,Img3,Img4,Img5,Img6]) 
        else:
            Img_channal1 = np.stack([ImageList[0][:,:,0],ImageList[1][:,:,0],ImageList[2][:,:,0],ImageList[3][:,:,0]],axis=2)
            Img_channal2 = np.stack([ImageList[0][:,:,1],ImageList[1][:,:,1],ImageList[2][:,:,1],ImageList[3][:,:,1]],axis=2)
            Img_channal3 = np.stack([ImageList[0][:,:,2],ImageList[1][:,:,2],ImageList[2][:,:,2],ImageList[3][:,:,2]],axis=2)
            Img_channal1 = np.sort(Img_channal1, axis=2)
            Img_channal2 = np.sort(Img_channal2, axis=2)
            Img_channal3 = np.sort(Img_channal3, axis=2)
            Img1 = np.stack([Img_channal1[:,:,0],Img_channal2[:,:,0],Img_channal3[:,:,0]],axis=2)
            Img2 = np.stack([Img_channal1[:,:,1],Img_channal2[:,:,1],Img_channal3[:,:,1]],axis=2)
            Img3 = np.stack([Img_channal1[:,:,2],Img_channal2[:,:,2],Img_channal3[:,:,2]],axis=2)
            Img4 = np.stack([Img_channal1[:,:,3],Img_channal2[:,:,3],Img_channal3[:,:,3]],axis=2)
            if not self.AddWeight:
                ImageList.extend([Img1,Img2,Img3,Img4])  
            else:  
                Img6 = (Img1+Img2)/2
                Img7 = (Img1+Img3)/2
                Img8 = (Img1+Img2+Img3)/3
                Img5 = (Img1+Img2+Img3+Img4)/4
                ImageList.extend([Img1,Img2,Img3,Img4,Img5,Img6,Img7,Img8])    
        return  ImageList        