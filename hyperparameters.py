import os
import sys

#文档的目录要改

pwd = os.path.dirname("F:/project_data_model/p3.2_data/readme.txt")
sys.path.append(pwd)
print('pwd:', pwd)


class Hyperparamters:
    # Train parameters
    print_step = 10
    batch_size = 16
    batch_size_eval = 16
    summary_step = 10
    num_saved_per_epoch = 3
    max_to_keep = 100
    logdir = 'F:/project_data_model/p3.2_data/logdir/25cat_125W'
    file_save_model = 'F:/project_data_model/p3.2_data/model/ALBERT_model1'

    # Optimization parameters
    num_train_epochs = 20
    warmup_proportion = 0.1
    use_tpu = None
    do_lower_case = True
    learning_rate = 5e-6

    # TextCNN parameters
    num_filters = 128
    filter_sizes = [2, 3, 4, 5, 6, 7]#[2, 3, 4, 5, 6, 7]
    embedding_size = 384
    keep_prob = 0.5

    # Sequence and Label
    sequence_length = 300
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
        '24': '24'}
    # ALBERT parameters
    name = 'albert_small_zh_google'
    bert_path = os.path.join(pwd, name)
    data_dir = os.path.join(pwd, 'data')
    vocab_file = os.path.join(pwd, name, 'vocab_chinese.txt')
    init_checkpoint = os.path.join(pwd, name, 'albert_model.ckpt')
    saved_model_path = os.path.join(pwd, 'model')
