import csv
from matplotlib import pyplot as plt

trainfile = './CSVdata/alexnet/run_Alexnet_original(82.665)-tag-valid_acc.csv'
validfile = './CSVdata/alexnet/run_Alexnet_original1(90.74)-tag-valid_acc.csv'
#tfile = './CSVdata/alexnet/run_Alexnet_original(88.713)-tag-train_acc.csv'
#Rfile = './CSVdata/resnet50(7.2).csv'
label = ['alexnet','proposed']#每条曲线对应名称
#保存图片名称
savename = './CSVpic/valid.jpg'

#trainname = trainfile.split('/',2)[::-1][0]#获取.csv数据名称用于保存图片Oct16_19-31-04_-valid_acc.csv'
#保存图片命名格式Oct16_19-31-04_
#savename = savepath + trainname[::-1].split('-', 1)[-1][::-1]+'.jpg'
#csvname[::-1].split('.', 1)[-1][::-1]逆序的截取的方式,截取‘.’之前的部分,逆序分割选取第一个再逆序

"""获取trainfile的内容"""
trainfile = open(trainfile,'r')
train_reader = csv.reader(trainfile)
header_row = next(train_reader)#第一行的内容，表头
epoch, train_acc = [0], [0]
for row in train_reader:
    current_date = row[1]
    epoch.append(float(current_date)+1)
    high = row[2]
    train_acc.append(float(row[2][ :4])*100)
    #train_acc.append(float(row[2]))
trainfile.close()

"""validname"""
validfile = open(validfile,'r')
valid_reader = csv.reader(validfile)
header_row = next(valid_reader)#第一行的内容，表头
#print(header_row)
epoch, valid_acc = [0], [0]
for row in valid_reader:
    current_date = row[1]
    epoch.append(float(current_date)+1)
    high = row[2]
    valid_acc.append(float(row[2][ :4])*100)
    #valid_acc.append(float(row[2]))
validfile.close()
"""
#validname
tfile = open(tfile,'r')
t_reader = csv.reader(tfile)
header_row = next(t_reader)#第一行的内容，表头
epoch, t_acc = [0], [0]
for row in t_reader:
    t_date = row[1]
    epoch.append(float(t_date)+1)
    t_high = row[2]
    t_acc.append(float(t_high[ :4])*100)
tfile.close()

#validname
Rfile = open(Rfile,'r')
R_reader = csv.reader(Rfile)
header_row = next(R_reader)#第一行的内容，表头
epoch, R_acc = [0], [0]
for row in R_reader:
    R_date = row[1]
    epoch.append(float(R_date)+1)
    R_high = row[2]
    R_acc.append(float(R_high[ :4])*100)
Rfile.close()
"""
print("epoch",epoch)
print("train_acc", train_acc)
print("valid_acc", valid_acc)

# 根据数据绘制图形
fig = plt.figure(dpi=200, figsize=(10,6))#绘制输出图片大小
plt.axis([0,50,0 ,100])#坐标轴数据范围
plt.plot(epoch, train_acc, c='red')
plt.plot(epoch, valid_acc, c='blue')
#plt.plot(epoch, t_acc, c='green')
#plt.plot(epoch, R_acc, c='black')
plt.xlabel('epoch', fontsize=16)
plt.ylabel("acc(%)", fontsize=16)
#plt.ylabel("acc(%)", fontsize=16)
plt.legend(label,loc=4)#右下角
#plt.subplots_adjust(top=0.97,bottom=0.075,left=0.065,right=0.975,hspace=0.21,wspace=0.2)#设置边界距离
plt.tick_params(axis='both', which='major', labelsize=16)#坐标轴上数据大小
#plt.xticks([x for x in range(50) if x % 5 == 0])  # x标记step设置为2
#plt.yticks([y for y in range(100)if y % 10 == 0])  # y标记step设置为1
#plt.title("Oct16_19-31-04_-valid_acc", fontsize=12)# 设置标题的格式
plt.savefig(savename) # 在plt.show()之前调用plt.savefig(),否则会出现空白图片
plt.show()
print("保存成功")
