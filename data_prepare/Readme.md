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

# 感谢  Acknowledge & Reference
本部分代码基本照搬了https://github.com/zhanlaoban/EDA_NLP_for_Chinese 中的方法，仅进行了一定的修改使之能适用于MongoDB

# 其他描述  Other description
eda.py为函数文件，定义四个方法具体实现方式

arguement.py为实际执行EDA的文件，改文件内的参数，路径均需要修改

delete_space.py为可选文件，EDA会将文本分词，如不需要这项操作，运行完arguement.py后需要去空格

eda.py is a function file, which defines the specific implementation of four methods

arguement.py is the file that actually executes EDA, the parameters and paths in the file need to be modified

delete_space.py is an optional file. EDA will split the text by words. If this operation is not required, you need to remove the space after running argument.py
