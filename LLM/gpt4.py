import os
import openai
import re

# OPENAI_API_KEY是自己设定的环境变量名
openai.api_key = os.getenv("OPENAI_API_KEY")
# 明文
openai.api_key = ""



def judge(prompt,model,id):
    response = openai.ChatCompletion.create(
    model= "gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "You are an impartial judge."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.5,
    n=1,
    stop=None,
    timeout=20,
)

    s=response.choices[0].message['content']
    path=os.path.join('judgement',model,id+'.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)


    matches = re.findall(r'\[\[(\d+)\]\]', s)
    return [int(match) for match in matches]  # Convert the matched strings to integers

