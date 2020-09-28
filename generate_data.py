""" 这是唯一一个不是ALBERT的部分 这部分的目的是从MongoDB中读取数据，并存成.CSV文件以供后续使用
目标文件分两列，第一列content（中文文本），第二列label（0-24数值）
MongoDB中的数据处理程序和来源的代码恕不提供
Since in this project, the original data is stored in MongoDB, this part is used to save the data in MongoDB as CSV
The target file is divided into two columns, the first column is content (Chinese text), the second column is label (0-24 value)
The data processing program and source code in MongoDB are not provided
"""
import codecs
import pymongo
import csv
# db名和表名要改！！！
mongo_url = "X.X.X.X:27017"
DATABASE = "nlp"
TRAININGTABLE="test_train"
VALTABLE="test_val"

client = pymongo.MongoClient(mongo_url)
db_des = client[DATABASE]
db_des_training = db_des[TRAININGTABLE]
db_des_val = db_des[VALTABLE]

#首先处理train
search=db_des_training.find(no_cursor_timeout = True)
i=0
data=[]
data.append(("content","label"))
for record in search:
    a=record['tag']
    b=record['content']
    if len(b) > 1200:
        b = b[:1200]
    c=(b,a)
    data.append(c)
    i=i+1
    if i%1000==0:
        print("------finished loading train set #",i)
f = codecs.open('F:/project_data_model/p3.2_data/data/sa_train.csv','w','utf-8')#这个地址要改！！！！
writer = csv.writer(f)
for i in data:
    writer.writerow(i)
f.close()


#然后处理val
search=db_des_val.find(no_cursor_timeout = True)
i=0
data=[]
data.append(("content","label"))
for record in search:
    a=record['tag']
    b=record['content']
    if len(b) > 1200:
        b = b[:1200]
    c=(b,a)
    data.append(c)
    i=i+1
    if i%1000==0:
        print("------finished loading val set #",i)
f = codecs.open('F:/project_data_model/p3.2_data/data/sa_test.csv','w','utf-8')#这个地址要改！！！！
writer = csv.writer(f)
for i in data:
    writer.writerow(i)
f.close()
