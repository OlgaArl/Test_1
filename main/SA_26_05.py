import plotly.express as px

import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1bRtJkFXv3DfOjl19jlkJee65u_BPR1e6VLdGTIM8Gcc/export?format=csv'
df = pd.read_csv(url)
#print(df)

responses = df.iloc[1, 6:16]
#print(responses)

res = []

for respons in responses:
  #Получить 1 значение
  resu = respons[0]
  #Значение сделать числом"
  resu = int(resu)
  print(resu)
  #Число минус 1
  resu = resu - 1
  #Сохранить в список результатов
  res.append(resu)

print(res)

# Создание DataFrame с данными
data = {'Category': ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
        'Value': res
        }

df = pd.DataFrame(data)

"Дата 2"
data2 = {'Category': ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
        'Value': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        }
df2 = pd.DataFrame(data2)

# Построение радарного графика с Plotly Express
fig = px.line_polar(df, r='Value', theta='Category', line_close=True)

"Построить 2 линию - надо взять данные"
fig.add_trace(px.line_polar(df2, r='Value', theta='Category', line_close=True).data[0])



"_______________"
# Настройка внешнего вида графика
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]  # Задаем диапазон для радиальной оси
        )
    )
)

# Отображение графика
fig.show()
