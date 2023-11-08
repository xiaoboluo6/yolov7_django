import os
from django.conf import settings


# 定义一个获取文件路径的方法
def save_uploaded_file(input_file):
    file_extension = input_file.name.split('.')[-1].lower()

    if file_extension in ['jpg', 'png']:
        # 如果是图片的话 就返回后缀类型
        file_extension = '.' + file_extension
    else:
        return False

    # 构建文件保存路径
    saveName = 'inputImg'
    saveLocation = os.path.join(settings.MEDIA_ROOT, 'detection', saveName+file_extension)  # 完整的本地路径
    print(saveLocation)

    # 保存上传文件到指定路径
    with open(saveLocation, 'wb') as destination:
        for chunk in input_file.chunks():
            destination.write(chunk)
    # 重置文件指针到文件开头
    input_file.seek(0)

    print("图片保存至本地路径：" + saveLocation)    # 图片名称是inputImg.xxx

    # 获取保存后的文件的URL
    file_url = os.path.join(settings.MEDIA_URL, 'detection', saveName+file_extension)
    print("前端页面访问图片的路径：" + file_url)
    return saveLocation,file_url