import os  
file_dir = "C:/opencv_3.0/opencv/newbuild/install/x64/vc14/lib";   
list_name = []
fp = open('filename.txt', 'w')  
for root, dirs, files in os.walk(file_dir):  
	print(root) #当前目录路径  
	print(dirs) #当前路径下所有子目录  
	print(files) #当前路径下所有非目录子文件  
lists=[line+"\n" for line in files]
fp.writelines(lists)
fp.close()