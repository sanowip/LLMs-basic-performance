from collections import defaultdict
xinghuo_score = defaultdict(list)
with open("basic perform/xinghuo.txt", "r", encoding="utf-8") as f:
    for line in f:
        s,b=line.split(":")
        b=list(map(int,b.split()))
        xinghuo_score[s].extend(b)
for i in xinghuo_score:
    xinghuo_score[i]=sum(xinghuo_score[i])/len(xinghuo_score[i])
print(xinghuo_score)


wenxin_score = defaultdict(list)
with open("basic perform/wenxin.txt", "r", encoding="utf-8") as f:
    for line in f:
        s,b=line.split(":")
        b=list(map(int,b.split()))
        wenxin_score[s].extend(b)
for i in wenxin_score:
    wenxin_score[i]=sum(wenxin_score[i])/len(wenxin_score[i])
print(wenxin_score)

zhipu_score = defaultdict(list)
with open("basic perform/zhipu.txt", "r", encoding="utf-8") as f:
    for line in f:
        s,b=line.split(":")
        b=list(map(int,b.split()))
        zhipu_score[s].extend(b)
for i in zhipu_score:
    zhipu_score[i]=sum(zhipu_score[i])/len(zhipu_score[i])
print(zhipu_score)

