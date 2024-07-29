import os
import re
import cv2
import json
import numpy as np
from ImageEnhancdQualityAccess.ImageEnhance.ExposureFusion import ExposureFusion
from ImageEnhancdQualityAccess.ImageEnhance.PixelLightArrange import PixelLightArrange
from ImageEnhancdQualityAccess.ImageQulityAccess.IQASet import IQASet
from typing import Type,Dict,List,Tuple

class IQAEnhanceImage(object):            
    def __init__(self,ModelPath:str,pixelLightArrange:Type[PixelLightArrange] = PixelLightArrange, exposureFusion:Type[ExposureFusion] = ExposureFusion, IQAset:[IQASet] = IQASet,
                                                Rsrc:bool = False, AddWeight:bool = False, GPUproviders:bool = False, MedianBlur:bool = True, nums:int = 3, pictureNums:int = 10):
        self.pixelLightArrange = pixelLightArrange(AddWeight)
        self.exposureFusion = exposureFusion()
        self.IQAset = IQAset(GPUproviders,MedianBlur,ModelPath)
        self.nums = nums
        self.pictureNums = pictureNums
        self.AddWeight = AddWeight
        self.Rsrc = Rsrc

    # #json文件读取
    # def __readJson(self,Json_path:str)->Dict:
    #     context=None
    #     try:
    #         with open(Json_path, "r") as f:
    #             context= json.load(f)
    #     except IOError as e:
    #         print("An IOError occurred:",e)
    #     return context

    #图像命名
    def __PartstoreDict(self,pathList:List[str],ImageList:List[np.array])->Dict[str,np.array]:
        DictName = {}
        Lpaths = len(pathList)
        if self.Rsrc:
            for i in range(Lpaths):
                    DictName[pathList[i]] = ImageList[i]
        substr = "Number(.*?)imestamp"
        pathe = re.sub(substr,"Number_of_strobes_0000_Fusion_Model_1_",pathList[0],1)
        if Lpaths != len(ImageList):
            if   Lpaths == 1:
                return DictName
            elif Lpaths == 2:
                DictName[pathe] = ImageList[2]
                DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_2_")] = ImageList[3]
                if self.AddWeight:
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_5_")] = ImageList[4]
            elif Lpaths == 3:
                DictName[pathe] = ImageList[3]
                DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_2_")] = ImageList[4]
                DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_3_")] = ImageList[5]
                if self.AddWeight:
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_4_")] = ImageList[6]
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_5_")] = ImageList[7]
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_6_")] = ImageList[8]
            else:
                DictName[pathe] = ImageList[4]
                DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_2_")] = ImageList[5]
                DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_3_")] = ImageList[6]
                DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_4_")] = ImageList[7]
                if self.AddWeight:
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_5_")] = ImageList[8]
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_6_")] = ImageList[9]
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_7_")] = ImageList[10]
                    DictName[pathe.replace("Fusion_Model_1_","Fusion_Model_8_")] = ImageList[11]
        return DictName

    #分区频闪融合
    def _getPartNStore(self,contextDict:Dict)->Dict[str,np.array]:
        getPartNStorNameDict = {}
        ChannalFlag = 1    
        if not contextDict["PartNStoreList"]:
            raise ValueError("无法读取图像路径与模式")
        else:
            for key, values in contextDict["PartNStoreList"].items():
                pathList = values
                ImageList = [] 
                for path in pathList:
                    Img = cv2.imread(path,ChannalFlag)
                    ImageList.append(Img)
                ImageList = self.pixelLightArrange.MltipixelValueRerank(ImageList)
                nameDict = self.__PartstoreDict(pathList,ImageList)
                getPartNStorNameDict.update(nameDict)
        return  getPartNStorNameDict

    #HDR融合
    def _getHDR(self,contextDict:Dict)->Dict[str,np.array]:
        getHDRNameDict = {}
        nameOriginalDict = {}
        ImageList = []
        ChannalFlag = 1  
        if not contextDict["HDRList"]:
            raise ValueError("无法读取图像路径与模式")
        patht = contextDict["HDRList"][0][1]
        for Tkv in contextDict["HDRList"]:
            Img = cv2.imread(Tkv[1],ChannalFlag)
            ImageList.append(Img)
            if self.Rsrc:
                nameOriginalDict[Tkv[1]] = Img
        nameDict = self.exposureFusion.multi_resolution_fusion_multi_compose(ImageList,self.nums)
        pathstr = "time_0000_Number_of_strobes_0000_Fusion"
        pathre = "time_(.*?)_Fusion"
        patht = re.sub(pathre,pathstr,patht,1)
        for key , values in nameDict.items():
            Newkey = patht.replace("Fusion_Model_0","Fusion_Model_"+key)
            getHDRNameDict[Newkey] = values
        getHDRNameDict.update(nameOriginalDict)     
        return  getHDRNameDict

    #使用IQA评分
    def _getIQAScore(self,contextDict:Dict)->List[Tuple[str,float,np.array]]: 
        getScoreList = []
        nameDict = {}
        getScoreName = {}
        if contextDict["Model"]["PartNStore"] == True and contextDict["Model"]["HDR"] == False:
            nameDict.update(self._getPartNStore(contextDict))
        elif contextDict["Model"]["PartNStore"] == False and contextDict["Model"]["HDR"] == True:
            nameDict.update(self._getHDR(contextDict))
        else:
            nameDict.update(self._getPartNStore(contextDict))
            nameDict.update(self._getHDR(contextDict))
        for key, values in nameDict.items():
            score = self.IQAset.IQANet(values)
            getScoreName[key] = score
        getSortScoreList = sorted(getScoreName.items(),key=lambda item:item[1],reverse=True) #得分是否需要归一化
        if len(getSortScoreList) <= self.pictureNums:
            getSortScoreList = getSortScoreList[:self.pictureNums]
        # else:
        #     pass
        for Tkv in getSortScoreList:
            getScoreList.append((Tkv[0],Tkv[1],nameDict[Tkv[0]]))
        return getScoreList

    #未使用IQA评分
    def _getNIQAScore(self,contextDict:Dict)->List[Tuple[str,float,np.array]]:
        getScoreList = []
        nameDict = {}
        getScoreName = {}
        if contextDict["Model"]["PartNStore"] == True :
            nameDict.update(self._getPartNStore(contextDict))
        if contextDict["Model"]["PartNStore"] == True:
            nameDict.update(self._getHDR(contextDict))
        # if contextDict["Model"]["PartNStore"] == True and contextDict["Model"]["PartNStore"] == False:
        #     nameDict.update(self._getPartNStore(contextDict))
        # elif contextDict["Model"]["PartNStore"] == False and contextDict["Model"]["PartNStore"] == True:
        #     nameDict.update(self._getHDR(contextDict))
        # elif contextDict["Model"]["PartNStore"] == True and contextDict["Model"]["PartNStore"] == True:
        #     nameDict.update(self._getPartNStore(contextDict))
        #     nameDict.update(self._getHDR(contextDict))
        # else:
        #     pass
        score = 1.0
        for key, values in nameDict.items():
            getScoreList.append((key,score,values))
        return getScoreList

    #图像处理模块
    def __accessScore(self,context:Dict)->List[Tuple[str,float]]:
        getScoreList = []
        ScoreList = []
        if not context["Model"]:
            raise ValueError("输入文件格式不符")
        if context["Model"]["IQA"]:
            getScoreList.extend(self._getIQAScore(context))
        else:
            getScoreList.extend(self._getNIQAScore(context))
        for scoreCell in getScoreList:
            cv2.imwrite(scoreCell[0],scoreCell[2])
            # if len(ImageArray.shape) == 2:
            #     cv2.imwrite(key,values[1])
            # if len(ImageArray.shape) == 3 and ImageArray.shape[2]==3:
            #     ImageArray =  cv2.cvtColor(values[1], cv2.COLOR_RGB2BGR)
            #     cv2.imwrite(key,ImageArray)
            ScoreList.append((scoreCell[0],scoreCell[1]))
        return ScoreList

    #模块入口与出口
    def IQAEnImg(self, OriginalDict:Dict)->List[Tuple[str,float]]:
        getPicturePathScoreList = []
        # if (not os.path.isfile(pathJson)) or (not pathJson.endswith(".json")):
        #     raise ValueError("输入不是json文件")
        # else:
        #     getPicturePathScoreList.extend(self.__accessScore(self.__readJson(pathJson)))
        getPicturePathScoreList.extend(self.__accessScore(OriginalDict))
        return getPicturePathScoreList

