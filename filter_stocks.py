Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
!pip install pandas
SyntaxError: invalid syntax
pip install pandas
SyntaxError: invalid syntax

======================================================= RESTART: Shell ======================================================
pip install pandas
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
pip3 install pandas
SyntaxError: invalid syntax
pip install --user pandas
SyntaxError: invalid syntax
KeyboardInterrupt
import pandas as pd
# Загрузите два списка в pandas DataFrame
df1 = pd.read_csv('Calendar spread trades.csv')


df2 = pd.read_csv('OPT_20230713.csv')

# Переименуйте колонку с тикерами в обоих DataFrame для упрощения дальнейших операций
df1 = df1.rename(columns={'Тикер': 'ticker'})
df2 = df2.rename(columns={'Тикер': 'ticker'})

# Сделайте отфильтрованный DataFrame, который содержит только строки из df2, где тикер присутствует в df1
filtered_df = df2[df2['ticker'].isin(df1['ticker'])]

# Сохраните отфильтрованный DataFrame в новый csv файл
filtered_df.to_csv('отфильтрованные_акции.csv', index=False)
SyntaxError: multiple statements found while compiling a single statement
# Загрузите два списка в pandas DataFrame
df1 = pd.read_csv('Calendar spread trades.csv')
df2 = pd.read_csv('OPT_20230713.csv')

# Переименуйте колонку с тикерами в обоих DataFrame для упрощения дальнейших операций
df1 = df1.rename(columns={'name': 'ticker'})
df2 = df2.rename(columns={'name': 'ticker'})

# Сделайте отфильтрованный DataFrame, который содержит только строки из df2, где тикер присутствует в df1
filtered_df = df2[df2['ticker'].isin(df1['ticker'])]

# Сохраните отфильтрованный DataFrame в новый csv файл
filtered_df.to_csv('filtered.csv', index=False)
SyntaxError: multiple statements found while compiling a single statement

# Загрузите два списка в pandas DataFrame
df1 = pd.read_csv('stocks.csv')
df2 = pd.read_csv('all_stocks.csv')

# Сделайте отфильтрованный DataFrame, который содержит только строки из df2, где тикер присутствует в df1
filtered_df = df2[df2['name'].isin(df1['name'])]

# Сохраните отфильтрованный DataFrame в новый csv файл
filtered_df.to_csv('filtered.csv', index=False)
SyntaxError: multiple statements found while compiling a single statement
df1 = pd.read_csv('stocks.csv')
df2 = pd.read_csv('all_stocks.csv')
filtered_df = df2[df2['name'].isin(df1['name'])]
filtered_df.to_csv('filtered.csv', index=False)
