"""
     这是实际训练时所要运行的代码
     由于processor和项目目的不同，与谷歌ALBERT的训练代码有一定不同，不过processor被分摊到了其他几个代码文件中，因此这部分只有几个基础的功能
     对于tensorboard部分，tf2中我暂时没有找到合适的替换函数，且tensorboard对我而言是个可有可无的部分，所以我直接注释掉了那一部分代码
     另：原作者在训练的过程中只关注了loss，完全没有关注acc，因此我自行补充了acc部分。acc部分的计算函数在network.py中。
"""
import os
import numpy as np
import tensorflow as tf
from classifier_utils import get_features,get_features_test
from networks import NetworkAlbert
from hyperparameters import Hyperparamters as hp
from utils import shuffle_one,select,time_now_string


# Load Model
pwd = os.path.dirname(os.path.abspath(__file__))
MODEL = NetworkAlbert(is_training=True)

# Get data features
input_ids,input_masks,segment_ids,label_ids = get_features()
input_ids_test,input_masks_test,segment_ids_test,label_ids_test = get_features_test()
num_train_samples = len(input_ids)
arr = np.arange(num_train_samples)
num_batchs = int((num_train_samples - 1)/hp.batch_size) + 1
print('number of batch:',num_batchs)
ids_test = np.arange(len(input_ids_test))

# Set up the graph
saver = tf.compat.v1.train.Saver(max_to_keep=hp.max_to_keep)
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())

# Load model saved before
MODEL_SAVE_PATH = os.path.join(pwd, hp.file_save_model)
ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
if ckpt and ckpt.model_checkpoint_path:
     saver.restore(sess, ckpt.model_checkpoint_path)
     print('Restored model!')


with sess.as_default():
    # Tensorboard writer
    writer = tf.compat.v1.summary.FileWriter(hp.logdir, sess.graph)
    for i in range(hp.num_train_epochs):
        indexs = shuffle_one(arr)
        for j in range(num_batchs-1):
            i1 = indexs[j * hp.batch_size:min((j + 1) * hp.batch_size, num_train_samples)]
            # Get features
            input_id_ = select(input_ids,i1)
            input_mask_ = select(input_masks,i1)
            segment_id_ = select(segment_ids,i1)
            label_id_ = select(label_ids,i1)
            # Feed dict
            fd = {MODEL.input_ids: input_id_,
                  MODEL.input_masks: input_mask_,
                  MODEL.segment_ids:segment_id_,
                  MODEL.label_ids:label_id_}
            # Optimizer
            sess.run(MODEL.optimizer, feed_dict = fd)
            # Tensorboard
            # Tf2这个部分会报错，暂时还没解决这个问题
            # 而且tensorboard对我没有太大用，所以我直接注释掉了
            '''
            if j%hp.summary_step==0:
                summary,glolal_step = sess.run([MODEL.merged,MODEL.global_step], feed_dict = fd)
                writer.add_summary(summary, glolal_step)
            '''
            # Save Model
            if j%(num_batchs//hp.num_saved_per_epoch)==0:
                if not os.path.exists(os.path.join(pwd, hp.file_save_model)):
                    os.makedirs(os.path.join(pwd, hp.file_save_model))
                saver.save(sess, os.path.join(pwd, hp.file_save_model, 'model_%s_%s.ckpt'%(str(i),str(j))))
            # Log
            if j % hp.print_step == 0:
                # Loss of Train data
                fd = {MODEL.input_ids: input_id_,
                      MODEL.input_masks: input_mask_ ,
                      MODEL.segment_ids:segment_id_,
                      MODEL.label_ids:label_id_}
                loss = sess.run(MODEL.loss, feed_dict = fd)
                acc = sess.run(MODEL.accuracy, feed_dict=fd)
                print('Time:%s, Epoch:%s, Batch number:%s/%s, Loss:%s, acc:%s'%(time_now_string(),str(i),str(j),str(num_batchs),str(loss),str(acc)))
                #  Loss of Test data
                indexs_test = shuffle_one(ids_test)[:hp.batch_size_eval]
                input_id_test = select(input_ids_test,indexs_test)
                input_mask_test = select(input_masks_test,indexs_test)
                segment_id_test = select(segment_ids_test,indexs_test)
                label_id_test = select(label_ids_test,indexs_test)
                fd_test = {MODEL.input_ids:input_id_test,
                           MODEL.input_masks:input_mask_test ,
                           MODEL.segment_ids:segment_id_test,
                           MODEL.label_ids:label_id_test}
                loss = sess.run(MODEL.loss, feed_dict = fd_test)
                acc = sess.run(MODEL.accuracy, feed_dict = fd_test)
                print('Time:%s, Epoch:%s, Batch number:%s/%s, Loss(test):%s, acc(test):%s'%(time_now_string(),str(i),str(j),str(num_batchs),str(loss),str(acc)))
    print('Optimization finished')
