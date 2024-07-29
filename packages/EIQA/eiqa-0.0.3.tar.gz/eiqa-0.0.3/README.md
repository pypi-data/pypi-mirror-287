# **功能**
1. 图像分区频闪与HDR增强
2. 图像质量评估

# **开放接口参数使用代码示例**
1. 输入参数：1.模型路径、2.包含图像信息的字典
```python
import json
from ImageEnhancdQualityAccess import IQAEnhanceImage
Json_path = r"/home/y05281/EIQA/test/test.json"
with open(Json_path, "r") as f:
    context = json.load(f)
IQAEnImgModel = IQAEnhanceImage(r"/home/y05281/DP-IQA-main/trained_models/student_model.onnx")
Ltp = IQAEnImgModel.IQAEnImg(context)
```

# **PC端图像命名&&输入Json设计与输出**
=================================================================================
## 图像命名规则
1. 频闪图像命名规则&&示例:*expose_time_2500_Number_of_strobes_1000_Fusion_Model_0_imestamp_20240718192828*
   1. expose_time_2500 表示曝光时长是2500
   2. Number_of_strobes_1000 表示代表亮灯的位置(四位01编码,按位置一次代表上下左右四个频闪灯,0000代表融合后生成图)
   3. Fusion_Model_代表融合方式1-8代表频闪融合,编号9+0101代表HDR,其中0101编码代表曝光时间由低到高的图像选择,0代表不选,1代表选取,高阶融合初版不涉及编号10,0代表无融合
   4. 原图应该有时间戳,非原图时间戳随意等长字符代替
   5. 示例：
    - *path0="expose_time_2500_Number_of_strobes_1111_Fusion_Model_0_imestamp_20240718192828"*  
    - *path8="expose_time_2800_Number_of_strobes_0000_Fusion_Model_9110_imestamp_20240718192828"*
    - *注意：HDR是4频闪同时亮,代表频闪的字段为Number_of_strobes_1111*
## 输入Json结构
1. Json关键字与内容注释
    - 关键字 **"Model"**,值**字典｛关键字"PartNStore"、"HDR"与"IQA",类型bool分别代表是否使用分区频闪融合算法、HDR融合算法以及图像评估机制｝**
    - 关键字 **"PartNStoreList"**,值**字典｛关键字"曝光时长（真实）"",类型*List[str] -> 字符串列表*代表该曝光时长下采集频闪图路径｝**
    - 关键字 **"HDR"**,值**列表，列表内是有序元组Tuple[str,str] -> 第一个字符串代表曝光时长，第二个代表图像路径，有序指的是以元组曝光时长元素由小到大排序**
    ~~ - 关键字 **"GrayRGB"**,值**字典｛关键字"Gray"与"RGB",类型bool分别代表是否使用灰图与采图｝** ~~
2. 示例
``` python
PathList = [path0,path1,path2,path3]
path = path8
Json = {
    "Model":{
        "PartNStore":True, #是否使用了分区频闪模式
        "HDR":False, #是否使用了HDR模式
        "IQA":False,#是否使用评估机制
    },
~~    "GrayRGB":{                       ~~
~~        "Gray":False, #图像是灰度图    ~~
~~        "RGB":True,   #图像是彩        ~~
~~    },                                ~~
    "PartNStoreList":{
        "2500(expose_time)":PathList, #结构曝光时间：该曝光下的采图路径列表
        "2600(expose_time)":PathList,
        "2700(expose_time)":PathList,
        "2800(expose_time)":PathList
    },
    "HDRList":[
        ("2500(expose_time)",path), #结构曝光时间：该曝光下的采图路径
        ("2600(expose_time)",path),
        ("2700(expose_time)",path),
        ("2800(expose_time)",path),
        ("2900(expose_time)",path),
    ]
}
```
========================================================================================================
## PC端输出设计
- 返回有序元组列表 **List[Tuple(score,str)] -> 一个元组列表串列表,元组内容是图像得分和图像路径字符串,列表有序指列表按降得分排序**
    - **IQA -> True, List[str] -> 一个有序字符串列表,字符串是图像路径,有序指的是列表左到右字符串对应的图像得分一次降低,list[0]>=list[-1]**
    - **IQA -> False, List[str] -> 一个字符串列表,字符串是图像路径**

# **许可证**
> 代码库使用GNU General Public License v3 (GPLv3)
