# 第4次实践作业：Python

本次实践将继续基于Python的容器技术开展

## 1.项目结构

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404152724527.png" alt="image-20220404152724527" style="zoom:50%;" />

## 2.python镜像构建

### 2.1配置文件

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404154410959.png" alt="image-20220404154410959" style="zoom:67%;" />

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404154433247.png" alt="image-20220404154433247" style="zoom:67%;" />

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404154447940.png" alt="image-20220404154447940" style="zoom:67%;" />

### 2.2构建对象

- Dockerfile文件

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404171008803.png" alt="image-20220404171008803" style="zoom:67%;" />

- 构建

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404171036443.png" alt="image-20220404171036443" style="zoom:67%;" />

## 3.运行程序

### 3.1构建容器

![image-20220404171603240](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404171603240.png)

### 3.2helloworl

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404175026441.png" alt="image-20220404175026441" style="zoom:67%;" />

## 4.opencv程序的部署运行

### 4.1 cv.py内容

![image-20220404204529825](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404204529825.png)

### 4.2效果

![image-20220404210114837](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404210114837.png)

图片转向

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404204621832.png" alt="image-20220404204621832" style="zoom:67%;" />

## 5.face_distance.py

参考：[face_recognition/README_Simplified_Chinese.md at master · ageitgey/face_recognition (github.com)](https://github.com/ageitgey/face_recognition/blob/master/README_Simplified_Chinese.md)

因为英文较差，使所以看的中文文档

这一节算是写的比较久，因为依赖问题折腾半天，还有校园网很慢，后来换的热点，速度飞升。

### 5.1先克隆face_distance仓库文件到本地

```
git clone https://github.com/ageitgey/face_recognition.git
```

### 5.2调用自带的docker-compose文件

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405013416175.png" alt="image-20220405013416175" style="zoom:67%;" />

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405013430912.png" alt="image-20220405013430912" style="zoom:67%;" />

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405020224034.png" alt="image-20220405020224034" style="zoom:67%;" />

```python
import face_recognition

#通常与其检查两张人脸是否匹配（真或假），不如看看它们有多相似。
#使用face_distance函数来执行此操作。

# 该模型的训练方式是，距离为 0.6 或更短的面应该是匹配的。但如果想
#更严格，可以寻找更小的面部距离。例如，使用 0.55 截止值将减少 false
# 正匹配，但存在更多漏报的风险。

#注意：这与"百分比匹配"并不完全相同。比例不是线性的。但您可以假设图像具有
# 距离越小，彼此越相似。"

# 加载一些图像进行比较
known_obama_image = face_recognition.load_image_file("obama.jpg")
known_biden_image = face_recognition.load_image_file("biden.jpg")

# 获取已知图像的人脸编码
obama_face_encoding = face_recognition。face_encodings（known_obama_image）[0]
biden_face_encoding = face_recognition。face_encodings（known_biden_image）[0]

known_encodings = [
    obama_face_encoding，
    biden_face_encoding
]

# 加载测试映像并获取其附件
image_to_test = face_recognition。load_image_file（"obama2.jpg")
image_to_test_encoding = face_recognition。face_encodings（image_to_test）[0]

# 查看测试图像与已知人脸的距离
face_distances = face_recognition。face_distance（image_to_test_encoding known_encodings)

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()
```

<img src="https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6(12).png" alt="未命名文件(12)" style="zoom: 33%;" />

## 6.编写一个python测试脚本测试nginx-tomcat负载均衡

### 6.1 python 脚本

![image-20220405022729814](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405022729814.png)

### 6.2启动nginx+tomcat服务

![image-20220405022847593](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405022847593.png)

### 3.nginx采取权重方式，访问服务器

![image-20220405022942688](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405022942688.png)



## 7.Python+Postgres

### 7.1 构建Python Flask容器

项目结构

![image-20220405030139523](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405030139523.png)

Dockerfile

![image-20220405030201113](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405030201113.png)

app.py

![image-20220405032728219](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405032728219.png)



构建镜像

![image-20220405030226362](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405030226362.png)

构建容器

![image-20220405032936270](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405032936270.png)

### 7.2 Python 连接  Postgres 

分卷

![image-20220405033627031](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405033627031.png)

![image-20220405041342814](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405041342814.png)



![image-20220405061119611](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405061119611.png)



## 实验总结

### 问题一

创建容器运行cv.py文件时一直报错

![image-20220404204741226](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404204741226.png)

配置文件 opencv-python 后加上 headless，完美解决问题

![image-20220404204956584](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220404204956584.png)

![image-20220404210049371](C:\Users\zengzhicheng\Desktop\第4次实践作业：Python.assets\image-20220404210049371.png)

### 问题二

![image-20220405012821402](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405012821402.png)

这个地方开始是自己手巧的配置，各种问题，后来下载github上仓库的就没问题了

### 问题三

容器一直闪退

![image-20220405015337410](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405015337410.png)

重新再制作一个容器。用-itd

![image-20220405020309445](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405020309445.png)

### 问题四

最开始在容器内运行 python 并没有反应

没有在容器内 pip install requests 

![image-20220405023258060](https://gitee.com/zengzhicheng01/typora-diagram/raw/master/img/image-20220405023258060.png)

### 小结

很多基础的东西不会，或者不熟练，导致做作业做起来十分困难，进度缓慢，时间利用率第=低，

这次作业就最后python flask连接 posthost 的部分感觉做的十分难受，最后一步甚至没做出来，要是用mysql做可能好一些，因为网上的资料比较多。

