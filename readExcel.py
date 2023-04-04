import sys
import os
import pandas as pd
from openpyxl import Workbook
import openAIkey
import openai

openai.api_key = openAIkey.getOpenAIkey()

# Let's test out the authentication: List the models available to us
# models = openai.Model.list()
# for model in models['data']:
#     print(model.id)

# Use the models
model_engine = "text-davinci-002"

# openAIの初期化
# initialize  = openai.Completion.create(
#         engine=model_engine,
#         prompt=f"以下のSQLを日本語に解析ください：",
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

# Open the excel
wb =  Workbook()
ws = wb.active

# read the excel
df = pd.read_excel('P2_飼010_主要飼料の輸入量_月報用_SQL.xlsx')
column = df['selsql']

initWord = f"以下のSQLを日本語に解析ください："

for row in column:
    prompt = (initWord + row)
    print(prompt)

    completions  = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.75,
    )

    outputMessage = completions.choices[0].text

    # print(outputMessage.strip())
    ws.append([outputMessage])

# save to the excel
wb.save('kaiseki3.xlsx')




