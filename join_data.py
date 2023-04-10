import pandas as pd
import json

# Opening JSON file
f1 = open('data/all.jsonl')
f2 = open('data/train.jsonl')
Lines1 = f1.readlines()
Lines2 = f2.readlines()

questions, answers = [], []

for line in Lines1:
    row = json.loads(line)
    for answer in row["human_answers"]:
        questions.append("Human: "+row["question"])
        answers.append("Assistant: "+answer)
    for answer in row["chatgpt_answers"]:
        questions.append("Human: "+row["question"])
        answers.append("Assistant: "+answer)

for line in Lines2: 
    row = json.loads(line)
    history = row["human_prompt"]
    split = history.split("Assistant:")
    question = history.replace("Assistant:"+split[-1],"")
    answer = "Assistant:"+split[-1]
    questions.append(question)
    answers.append(answer)

df = pd.DataFrame()
df["question"] = questions
df["answer"] = answers

df.to_csv("data/train.csv", index=False)