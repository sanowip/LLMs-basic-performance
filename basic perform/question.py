from LLM.wenxin import wenxin
from LLM.xinghuo import xinghuo
from LLM.zhipu import zhipu
from LLM.gpt4 import judge
from collections import defaultdict
import json
import os
s0="Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You will be given a reference answer and the assistant's answer. You evaluation should focus on the assistant's answer to the second question. Begin your evaluation by comparing the assistant's answer with the reference answer. Identify and correct any mistakes. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 0 to 10 by strictly following this format: '[[rating]]', for example: 'Rating: [[5]]'.The two questions need to be scored separately"
s1="Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question displayed below. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of the response. Begin your evaluation by providing a short explanation. Be as objective as possible. After providing your explanation, please rate the response on a scale of 0 to 10 by strictly following this format: '[[rating]]', for example: 'Rating: [[5]]'. The two questions need to be scored separately"
s2="Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You will be given a reference answer and the assistant's answer. You evaluation should focus on the assistant's answer to the second question. Begin your evaluation by comparing the assistant's answer with the reference answer. Identify and correct any mistakes. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 0 to 10 by strictly following this format: '[[rating]]', for example: 'Rating: [[5]]'.The two questions need to be scored separately"

wenxin_scores=defaultdict(list)
xinghuo_scores=defaultdict(list)
zhipu_scores=defaultdict(list)
classX=["writing","roleplay","reasoning","math","coding","extraction","stem","humanities"]

def get(s1,s2,model):
    if(model=='wenxin'):
        return wenxin(s1,s2)
    elif(model=='xinghuo'):
        return xinghuo(s1,s2)
    elif(model=='zhipu'):
        return zhipu(s1,s2)
    else:
        print("error")

def save(model,category,ans):

    s="\n"+category+":"+str(ans[0])+" "+str(ans[1])
    if(model=='wenxin'):
        with open('basic perform/wenxin.txt','a',encoding='utf-8') as f:
            f.write(s)
    elif(model=='xinghuo'):
        with open('basic perform/xinghuo.txt','a',encoding='utf-8') as f:
            f.write(s)
    elif(model=='zhipu'):
        with open('basic perform/zhipu.txt','a',encoding='utf-8') as f:
            f.write(s)
if __name__ == '__main__':

    with open('data_mt_bench_question.jsonl', 'r') as f:
        for line in f:
            data = json.loads(line)
            for model in ['wenxin','zhipu']:
                model_path=os.path.join('basic perform/answer',model)
                judge_path=os.path.join('basic perform/judgement',model)
                file=str(data['question_id'])+'.txt'
                path=os.path.join(model_path,file)
                if file in os.listdir(judge_path):
                    continue
                if file not in os.listdir(model_path):
                    ans1,ans2=get(data["turns"][0],data["turns"][1],model)
                    if(data['category']=='math' or data['category']=='reasoning' or data['category']=='coding' or data['category']=='extraction' or data['category']=='stem'):
                        if 'reference' in data:
                            tmp=s2+"\n[question1]:\n"+data['turns'][0]+"\n[answer1]:\n"+ans1
                            tmp+="\n[refence1]:\n]"+data['reference'][0]
                            tmp+="\n[question2]\n:"+data['turns'][1]+"\n[answer2]\n:"+ans2
                            tmp+="\n[refence2]:\n]"+data['reference'][1]
                        else:
                            tmp=s1+"\n[question1]:\n"+data['turns'][0]+"\n[answer1]:\n"+ans1
                            tmp+="\n[question2]\n:"+data['turns'][1]+"\n[answer2]\n:"+ans2
                    else:
                        tmp=s0+"\n[question1]:\n"+data['turns'][0]+"\n[answer1]:\n"+ans1
                        tmp+="\n[question2]\n:"+data['turns'][1]+"\n[answer2]\n:"+ans2
                
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(tmp)
                else:
                    with open(path, 'r', encoding='utf-8') as f:
                        tmp=f.read()
                save(model,data['category'],judge(tmp,model,str(data['question_id'])))




