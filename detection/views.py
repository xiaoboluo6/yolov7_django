from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import os
from django.conf import settings
import cv2
from . import fuction
import subprocess
import sys
sys.path.append("./yolov7model")
import re


class Index(View):
    def get(self, request):
        return render(request, 'detection/index.html')

    def post(self, request):
        # 读取图片文件
        img = request.FILES.get('image', None)



        if img is not None:
            # saveLocation本地保存的地址   input_url前端页面访问图片的路径
            saveLocation, input_url = fuction.save_uploaded_file(img)
            print("input_url:", input_url)
            conf = request.POST.get('conf', None)

            output_num = "未找到匹配的数字"  # 搞个全局参数 默认是没有找到  找到的话 后面会赋值
            try:
                command = [
                    'python',
                    'detection/yolov7model/detect.py',
                    '--weights',
                    'detection/yolov7model/weights/ElectronicScale0310Best.pt',
                    '--source',
                    saveLocation,
                    '--img-size',
                    '640',
                ]
                command+=['--conf',str(conf)]

                completed_process = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # 获取 detect.py 中打印的输出
                stdout_output = completed_process.stdout
                # 将字节数据转换为字符串（使用GB2312编码）
                stdout_output_str = stdout_output.decode('GB2312')
                # 现在 stdout_output_str 是字符串类型
                # 然后进行数字提取
                result = re.search(r'!!!([0-9.]+)!!!', stdout_output_str)
                if result:
                    extracted_number = result.group(1)  # 提取第一个捕获组
                    print(extracted_number)
                    output_num = extracted_number
                else:
                    print("未找到匹配的数字")
                print("--------------------------------------------------------------------")



                print("Script executed successfully.")
            except subprocess.CalledProcessError as e:
                print("Error executing script: {e}")


            # 上面执行的detect指令  会直接把结果图片放在 detection/media/detection/outputImg.img 里面
            # 前端可以直接用output_url来访问图片 进行显示
            output_name = 'outputImg'
            # 这是本地地址
            output_file = os.path.join(settings.MEDIA_ROOT, 'detection', output_name + '.jpg')
            # 这是html用的地址    这是前端页面读取图片的地址
            output_url = os.path.join(settings.MEDIA_URL, 'detection', output_name + '.jpg')

            # print(output_file)   # 检测结果的本地地址
            # print(output_url)    # 检测结果的html地址

            return render(request, 'detection/index.html',
                          {'input_image': input_url,
                           'output_image': output_url,
                           'output_num': output_num,
                           'conf_thresh': conf})


        else:
            return HttpResponse('请输入待检测图片！！！')