# Data_prepare

# Overall
由于在实际工程项目中，数据往往极度不平衡，因此在训练之前需要先进行数据平衡。本文件夹内提供了一种中文文本平衡的方式。

Since in actual engineering projects, data is often extremely unbalanced, data balance needs to be performed before training. This folder provides a way to balance Chinese text.

# 具体方法  Specific method
方法1：同义词替换，将分词后的文本中的随机若干个词替换为同义词表中的同义词

方法2：插入n个词

方法3：随机交换词

方法4：随机删除词


Method 1: Synonym replacement, replace several random words in the text after word segmentation with synonyms in the synonym table

Method 2: Insert n words

Method 3: Swap words randomly

Method 4: Delete words randomly

# 其他描述  Other description
EDA.py为
