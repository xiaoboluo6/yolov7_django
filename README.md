### 安装和运行：
```
# 基础环境
conda create -name env python=3.6
conda activate env

# 直接跳转到下载的代码
cd path/to/yolov7_django

# 这里我默认使用的是CPU版本的torch和torchvision，换成GPU的话自己修改或者额外进行pip
pip install -r requirements.txt

# 运行 激活环境的情况下 在path/to/yolov7_django目录中
python manage.py runserver
# 然后直接访问http://127.0.0.1:8000/index/即可
```

### 权重文件的替换：
* 这里我选用的是自训练的权重，效果一般般，**仅供参考**
* 对于有阴影的数字难以识别，准确率较低
* `ElectronicScale0310Best.pt`    **[权重链接(Baidu Drive)](https://pan.baidu.com/s/12axyZO9wQxFZBLfzV027lQ )** (下载码: xbl6)
* 权重文件放置的位置 **↓↓↓**
```
├─detection
│  ├─...
│  ├─yolov7model
│  │  ├─...
│  │  ├─weights
│  │  	└─ElectronicScale0310Best.pt           # 权重文件放置位置
│  │  └─...
│  ├─views.py                                  # 调整权重文件名称路径等参数
│  ├─...
├─manage.py
├─images                                       # 效果图和测试图
├─yolov7_django
├─db.sqlite
├─requirements.txt
```
### 效果图
![页面效果图](https://github.com/xiaoboluo6/yolov7_django/blob/master/images/%E6%95%88%E6%9E%9C%E5%9B%BE1.png?raw=true)
