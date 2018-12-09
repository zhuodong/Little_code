import os
from PIL import Image
path = r"C:\Users\zhuodong\Desktop\data"
save_path = r"C:\Users\zhuodong\Desktop\label"
#image_name = '0{logo}'
file_list = os.listdir(path)
for i,filename_ground in zip(range(len(file_list)),file_list):
    base_img = Image.open(path+'\\'+filename_ground)####################打开目标图片
    base_img = base_img.convert('RGB')
    #base_img.save(save_path+'\\'+image_name.format(logo=i)+".jpg") #保存图片
    base_img.save(save_path+'\\'+str(i+1001)+".jpg") #保存图片
print("Finsh resize image ...")
