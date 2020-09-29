# ALBERT-TextCNN-Chinese-

# 针对任务  Targeted tasks:
基于ALBERT对于中文文本的单标签分类，
Single-label classification of Chinese text based on ALBERT

# 感谢  Acknowledgement & Reference
本项目是基于https://github.com/hellonlp/sentiment_analysis_albert 对tensorflow2.x的debug，以及部分细节的修改

This Project is based on https://github.com/hellonlp/sentiment_analysis_albert.

# 环境  Environmental dependence
本项目针对tensorflow2.x版本，下面为pip list中的部分：

This project is for the tensorflow 2.x version, the following is part of the pip list:

python                   3.7

tensorflow-gpu           2.2.0

tensorflow-hub           0.9.0

six                      1.15.0

sentencepiece            0.1.91

# 对不同的项目，必定需要修改的有 For different projects, the following parts must be modifications：
hyperparameters.py:	所有参数可能都要改 ALL parameters including file path needed to be changed for different tasks

classifier_utils.py:	156行左右，label 的种类  approximately line 156, the category's names

testCNN和testLSTM在modules里定义,需要修改网络可自行更改

# 训练集输入 Model input (training set)：
csv文件，第一列content，第二列label，其中第一行为表头，就是content和label，label为要与classifier_utils.py中定义一样

csv file, the first column is content, the second column is label, where the first row is the header, which is content and label, label have to be the same as defined in classifier_utils.py


generate_data.py提供了从MongDB中读取CSV文件的一种方法，仅供参考。MongoDB中的代码和数据来源恕不提供

generate_data.py provides a method to prepare CSV files from MongoDB, for reference only. Code and data sources in MongoDB will not be provided

# 数据平衡  Data Balancing
训练集各种类的数据数量需要平衡，对于不平衡的数据，data_prepare文件夹中提供了一种文本增强方法

The amount of data with different labels in the training set needs to be balanced. For unbalanced data set, a text enhancement method is provided in the data_prepare folder
