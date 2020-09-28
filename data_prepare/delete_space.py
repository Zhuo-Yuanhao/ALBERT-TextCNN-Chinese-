import jieba
import numpy as np

filePath = 'F:/project_data_model/p2.3_data/July-Aug23/argumented_data1.txt'
fileSegWordDonePath = 'F:/project_data_model/p2.3_data/July-Aug23/argumented6_x_train.txt'
fileydatapath = 'F:/project_data_model/p2.3_data/July-Aug23/argumented6_y_train.txt'

fileTrainRead = []
y_value = []
dic = {}
j=1
a=""
repeat=0
with open(filePath, encoding='utf-8') as fileTrainRaw:
    for line in fileTrainRaw:  # 按行读取文件
        #按照实际情况确定需要删掉的符号、字母、数字等
        lane=line
        line=line.split('\t')
        length=len(line)
        try:
            if not len(line[1])==0:
                b=1
            if len(line[0])==2 and (line[0][1]=='感' or line[0][1]=='业' or line[0][1]=='品' or line[0][1]=='性' or line[0][1]=='面')\
                    and (line[0][0]=='敏' or line[0][0]=='行' or line[0][0]=='竞' or line[0][0]=='正' or line[0][0]=='中' or line[0][0]=='负'):
                #print("length=",length)
                #for i in '@#￥%&*()[]{}><~`+-*/【】^=-—～\《》（） ［］“”"|_,★·」「『』\t':
                    #line[1] = line[1].replace(i, '')
                for i in ' ★」「『』':
                    line[1] = line[1].replace(i, '')
                line[0] = line[0].replace('行业', '0')
                line[0] = line[0].replace('竞品', '1')
                line[0] = line[0].replace('正面', '2')
                line[0] = line[0].replace('中性', '3')
                line[0] = line[0].replace('负面', '4')
                line[0] = line[0].replace('敏感', '5')
                if line[1] != ' ' and line[1] not in dic:
                    dic[line[1]] = 0
                    fileTrainRead.append(line[1])
                    y_value.append(line[0])
        except:
            c=1


y_value = [int(x) for x in y_value]
y_value = np.array(y_value)
n=0
y=[]
x=[]
for l in range(len(y_value)):
    y.append(y_value[l])
    x.append(fileTrainRead[l])
y_value = y
y_value = [int(x) for x in y_value]
y_value = np.array(y_value)
np.savetxt(fileydatapath,y_value)
fileTrainRead = x
fileTrainSeg = []
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([''.join(list(fileTrainRead[i][:-1]))])
    #print(' '.join(list(jieba.cut(fileTrainRead[i][:-1], cut_all=False))))
    if i % 1000 == 0:
        print(i)

i=0
f = open(fileSegWordDonePath, "w",encoding='utf-8')

for i in range(len(fileTrainSeg)):
    f.write(fileTrainSeg[i][0] + '\n')
f.close()

