from eda import *
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input",default='F:/project_data_model/p2.3_data/July-Aug23/x_pure_text.txt', required=False, type=str, help="原始数据的输入文件目录")
ap.add_argument("--output",default='F:/project_data_model/p2.3_data/July-Aug23/argumented_data1.txt', required=False, type=str, help="增强数据后的输出文件目录")
ap.add_argument("--num_aug", default=6 ,required=False, type=int, help="每条原始语句增强的语句数")
ap.add_argument("--alpha", default=0.08,required=False, type=float, help="每条语句中将会被改变的单词数占比")
args = ap.parse_args()

#输出文件
output = None
if args.output:
    output = 'F:/project_data_model/p2.3_data/July-Aug23/argumented_data1.txt'
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#每条原始语句增强的语句数
num_aug = 6 #default
if args.num_aug:
    num_aug = 6


#每条语句中将会被改变的单词数占比
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
                aug_sentences = eda(sentence, alpha_sr=alpha, alpha_ri=alpha, alpha_rs=alpha, p_rd=alpha, num_aug=num_aug)
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
    gen_eda('F:/project_data_model/p2.3_data/July-Aug23/x_pure_text.txt', output, alpha=alpha, num_aug=num_aug)
