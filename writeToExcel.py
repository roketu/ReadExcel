import sys
import os
import pandas as pd
from openpyxl import Workbook
import openai
import generateText

# Open the excel
wb =  Workbook()
ws = wb.active

# read the excel
df = pd.read_excel('P2_飼010_主要飼料の輸入量_月報用_SQL.xlsx')
column = df['E']

print(generateText.generate_text("以下のSQLを日本語に解析ください："))

for row in column:
    prompt = ([row])
    outputMessage = generateText.generate_text(prompt)
    ws.append([outputMessage])

# save to the excel
wb.save('kaiseki1.xlsx')




