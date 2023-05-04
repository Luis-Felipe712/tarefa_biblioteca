import pandas as pd

# Cria um DataFrame com dados fictícios
data = {'nome': ['Alice', 'Bob', 'Carol', 'David'], 'idade': [25, 30, 35, 40], 'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}
df = pd.DataFrame(data)

# Imprime o DataFrame
print(df)

# Seleciona os dados dos indivíduos com idade maior que 30
df2 = df[df['idade'] > 30]

# Imprime o novo DataFrame
print(df2)

# Calcula a média das idades dos indivíduos
media_idade = df['idade'].mean()

# Imprime a média das idades
print(media_idade)