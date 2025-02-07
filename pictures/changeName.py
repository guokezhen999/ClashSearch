import os
from PIL import Image

# 想要更改图片所在的根目录
rootdir = "/Users/guokezhen/Desktop/Python_Work/clashofclans/Qt/pictures/clan/capitalPeak"
files = [os.path.join(rootdir, file) for file in os.listdir(rootdir)]
print(files)

for file in files:
    fileSplits = file.split('.')
    if fileSplits[1] != "png":
        pic = Image.open(file)
        pic.save(fileSplits[0] + '.png')
        os.remove(file)

