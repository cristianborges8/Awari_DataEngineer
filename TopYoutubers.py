# Tarefa: Top Youtubers
# Fazer download do dataset Top Youtube Artists, do Kaggle. 
import pandas as pd
df = pd.read_csv('/Users/cristianborges/Documents/Projetos/Awari_DataEngineer/topyoutube.csv')

# Tratar as colunas sem informação adicionando o texto “Não informado”
df.fillna("Não informado")

# Formatar a coluna de total de inscritos multiplicando por 100 milhões
df = df.rename(columns={'100M': 'Total Subscribers'})
df['Total Subscribers'] = df['Total Subscribers'] * 100000000

# Formatar coluna “AVG” para 2 casas decimais depois da vírgula.
df['Avg'] = df['Avg'].round(2)

# Mostrar os top 10 usuários.
top_10_usuarios = df.head(10)
print(top_10_usuarios)

# Mostrar primeiros 100 usuários por nome decrescente.
df_sorted = df.sort_values(by='Artist', ascending=False)
primeiros_100_usuarios = df_sorted.head(100)
print(primeiros_100_usuarios)

# # Salvar um novo CSV com a informação tratada.
df.to_csv('topyoutube_.csv', index=False)
