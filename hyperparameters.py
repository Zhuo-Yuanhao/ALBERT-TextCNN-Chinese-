import os
import sys

#文档的目录要改

pwd = os.path.dirname(".../readme.txt")#只是用来标注模型文件夹位置，仅此而已，readme是个空文件即可。如，模型文件夹（albert_small_zh_google）在C：/.../model/albert_small_zh_google
#那么这个readme的地址就为C：/.../model/readme.txt
sys.path.append(pwd)
print('pwd:', pwd)


class Hyperparamters:
    # Train parameters
    # 训练相关参数，不做赘述
    print_step = 10
    batch_size = 16
    batch_size_eval = 16
    summary_step = 10
    num_saved_per_epoch = 3
    max_to_keep = 100
    logdir = '.../logdir/25cat_125W'
    file_save_model = '.../ALBERT_model1'#保存模型的地址，这是个文件夹，会根据所设定的步长存多个model

    # Optimization parameters
    num_train_epochs = 20
    warmup_proportion = 0.1
    use_tpu = None
    do_lower_case = True
    learning_rate = 5e-6

    # TextCNN parameters
    # TextCNN模型的相关参数    
    # filter_size, embedding_size, num_filters分别为：filter_height, filter_width, out_channels    
    filter_sizes = [2, 3, 4, 5, 6, 7]#层数可变化
    embedding_size = 384
    num_filters = 128
    keep_prob = 0.5

    # Sequence and Label
    # 数据相关参数
    sequence_length = 300##################最大也不能超过512！！！！！！！！！
    num_labels = 25
    dict_label = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        '11': '11',
        '12': '12',
        '13': '13',
        '14': '14',
        '15': '15',
        '16': '16',
        '17': '17',
        '18': '18',
        '19': '19',
        '20': '20',
        '21': '21',
        '22': '22',
        '23': '23',
        '24': '24'}#这玩意儿是label是啥，得跟其他文件中的cat匹配（另一个文件中好像用的是三分类测试，跑之前得调整一下）
    # ALBERT parameters
    # 模型地址和保存地址
    name = 'albert_small_zh_google'
    bert_path = os.path.join(pwd, name)
    data_dir = os.path.join(pwd, 'data')
    vocab_file = os.path.join(pwd, name, 'vocab_chinese.txt')
    init_checkpoint = os.path.join(pwd, name, 'albert_model.ckpt')
    saved_model_path = os.path.join(pwd, 'model')
