######这才是实际运行的程序！！！！
from eda import *
import argparse
ap = argparse.ArgumentParser()
"""
    底下这个ap.add_argument其实并不是最终的参数值，只是为了加个double check保证多次运行程序时，输入的参数有做及时的修改（其实也不是，上下值不一样也不会报错，只是为了便于自己检查）
    另外一个目的是告诉第一次用这个代码的人这几个参数是干啥的，仅此而已。
    熟悉代码之后重复的部分保留一个即可
    
    The ap.add_argument below is actually not the final parameter value.
    It is just to add a double check to ensure that the input parameters are modified in time when the program is run multiple times. Easy to check by yourself
    Another purpose is to tell people who use this code for the first time what these parameters do, and nothing more.
    Keep one of the duplicated parts after familiarizing with the code
    
    Please forgive me that the comments in the rest part of the code uses Chinese
"""
ap.add_argument("--input",default='F:/project_data_model/p2.3_data/July-Aug23/x_pure_text.txt', required=False, type=str, help="原始数据的输入文件目录")
ap.add_argument("--output",default='F:/project_data_model/p2.3_data/July-Aug23/argumented_data1.txt', required=False, type=str, help="增强数据后的输出文件目录")
ap.add_argument("--num_aug", default=6 ,required=False, type=int, help="每条原始语句增强的语句数，注意要-1")
#上面这一行：有一句话，算上这句话要生成10句话，这个值选9，输出的第一条为这句话本身，然后增强出9句话
ap.add_argument("--alpha", default=0.08,required=False, type=float, help="每条语句中将会被改变的单词数占比")
args = ap.parse_args()

#重新定义输出文件的目录
output = None
if args.output:
    output = 'F:/project_data_model/p2.3_data/July-Aug23/argumented_data1.txt'
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#重新定义每条原始语句增强的语句数
num_aug = 6 #default
if args.num_aug:
    num_aug = 6


#重新定义每条语句中将会被改变的单词数占比
alpha = 0.08 #default
if args.alpha:
    alpha = args.alpha

def gen_eda(train_orig, output_file, alpha, num_aug=8):
    n=0
    writer = open(output_file, 'w',encoding='utf-8')
    #lines = open(train_orig, 'r',encoding='utf-16').readlines()
    print("正在使用EDA生成增强语句...")
    with open(train_orig, encoding='utf-8') as fileTrainRaw:
        for line in fileTrainRaw:  # 按行读取文件
    #for i, line in enumerate(lines):
            try:
                parts = line[:-1].split('\t')   
                label = parts[0]
                sentence = parts[1]
                aug_sentences = eda(sentence, alpha_sr=alpha, alpha_ri=alpha, alpha_rs=alpha, p_rd=alpha, num_aug=num_aug)#调用eda，注意原则上不能使用默认值
                for aug_sentence in aug_sentences:
                    writer.write(label + "\t" + aug_sentence + '\n')
                if n%5==0:
                    print(n)
            except:
                print("error sentence")
            n=n+1
    writer.close()
    print("Done!")
    print(output_file)

if __name__ == "__main__":
    gen_eda('F:/project_data_model/p2.3_data/July-Aug23/x_pure_text.txt', output, alpha=alpha, num_aug=num_aug)#调用eda
