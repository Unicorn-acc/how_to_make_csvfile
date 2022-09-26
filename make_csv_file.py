import os, glob
import csv

# 类别->数字
class_to_num = {}

dir = 'data/train'  # 图像根目录

class_name_list = os.listdir('data/train')  # 获取文件夹下的列表
# print(class_name_list) # ['Disgusted', 'Fearful', 'Happy', 'Sad', 'Surprised']

for class_name in class_name_list:  # 遍历每一个类别里的文件名
    class_to_num[class_name] = len(class_to_num.keys())  # 将文件名映射为数字
# print(class_to_num) # {'Disgusted': 0, 'Fearful': 1, 'Happy': 2, 'Sad': 3, 'Surprised': 4}

# 获取数据图片路径，方便后面用函数打开
image_dir = []
for class_name in class_name_list:
    image_dir += glob.glob(os.path.join('data\\train', class_name, '*.jpg'))  # os.path.join将不同路径拼接起来；*.jpg是图像名字
# print(image_dir)  # ['data\\train\\Disgusted\\train_00031.jpg', 'data\\train\\Disgusted\\train_00063.jpg', 'data......

# 写csv文件
import random

random.shuffle(image_dir)  # random可以把文件顺序打乱
with open('myself_data.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    for image in image_dir:  # 遍历所有图片的路径，开始写数据
        class_name = image.split(os.sep)[-2]  # 路径从右开始数第二个路径就是类别名（文件夹名）
        '''
        这一步可以不做，直接把图片路径和类别名压在一起，读文件的时候对标签列做class-to-num
        label = class_to_num[class_name]  # 类别转换为数字
        writer.writerow([image, label])  # 图片路径与类别数字写在一行里
        '''
        writer.writerow([image, class_name])  # 图片路径与类别名写在一行里
# print('finish')


# ---------------------------------------------------------------------------------
# 语雀：动手学深度学习-30
# 打开csv文件，看看数据什么样子
import pandas as pd

labels_dataframe = pd.read_csv(os.path.join('myself_data.csv'), names=['path', 'class'])
'''
print(labels_dataframe.head(5))
                                   path      class
0      data\train\Happy\train_00011.jpg      Happy
1        data\train\Sad\train_00025.jpg        Sad
2      data\train\Happy\train_00009.jpg      Happy
3    data\train\Fearful\train_02837.jpg    Fearful
4  data\train\Disgusted\train_00071.jpg  Disgusted
['Disgusted', 'Fearful', 'Happy', 'Sad', 'Surprised']
{'Disgusted': 0, 'Fearful': 1, 'Happy': 2, 'Sad': 3, 'Surprised': 4}

Process finished with exit code 0

'''
# 如何读取csv后将类别对应成数字来训练呢？class-to-num？
labels = sorted(list(set(labels_dataframe['class'])))  # 所有类别去重排序
# print(labels) # ['Disgusted', 'Fearful', 'Happy', 'Sad', 'Surprised']
class_to_num2 = dict(zip(labels, range(len(labels))))  # 将类别对应成数字
# print(class_to_num2) # {'Disgusted': 0, 'Fearful': 1, 'Happy': 2, 'Sad': 3, 'Surprised': 4}

# 可以转换回来，方便最后预测的时候使用
num_to_class = {v: k for k, v in class_to_num.items()}
# print(num_to_class) # {0: 'Disgusted', 1: 'Fearful', 2: 'Happy', 3: 'Sad', 4: 'Surprised'}
