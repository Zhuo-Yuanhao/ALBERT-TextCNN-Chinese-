import jieba
import numpy as np

filePath = 'EDA_PATH.txt'
fileSegWordDonePath = 'Done_PATH.txt'

fileTrainRead = []
j=1
a=""
repeat=0
with open(filePath, encoding='utf-8') as fileTrainRaw:
    for line in fileTrainRaw:  # 按行读取文件
        #按照实际情况确定需要删掉的符号、字母、数字等
        lane=line
        line=line.split('\t')
        length=len(line)
        for i in ' ★」「『』':
            lane = lane.replace(i, '')
        fileTrainRead.append(lane)

n=0
x=[]
for l in range(len(fileTrainRead)):
    x.append(fileTrainRead[l])
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

