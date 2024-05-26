import plotly.express as px

# Создание данных
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

# Создание фигуры с использованием Plotly Express
fig = px.bar(data, x='Name', y='Age', color='City', title='Гистограмма возрастов по городам')
fig.show()
