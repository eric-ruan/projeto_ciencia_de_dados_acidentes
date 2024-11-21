# Projeto Ciencia de Dados Acidentes
Nesse projeto básico de ciência de dados eu fiz toda uma análise de dados de acidentes que ocorreram na cidade de Porto Alegre, o projeto consiste em tratar alguns dados e plotar um mapa de calor nos locais onde ocorrem mais acidentes.

** A base de dados está nesse repositório e foi baixada do site: https://dadosabertos.poa.br/dataset/acidentes-de-transito-acidentes **

## Primeiramente para iniciarmos a análise, foi importado a biblioteca Pandas no google colab e visualizando a base:
```
import pandas as pd
df = pd.read_csv('cat_acidentes.csv', sep=';')
df
```

## Após isso foi feito uma análise e visto que contém dados do tipo NaN na base, o que estava dificultando em uma análise correta dos dados, por esse motivo as linhas do DataFrame que continham esses dados NaN foi excluída.
```
df = df.dropna(subset=['latitude', 'longitude'], how='any')
```

## Foi feito então a importação da biblioteca Folium que foi usada para a plotagem do gráfico de calor.
```
import folium
from folium.plugins import HeatMap
```

## Criei uma variável chamada "Mapa" que recebeu a criação do mapa com a localização da cidade de Porto Alegre.
```
mapa = folium.Map(location=[-30.1, -51.15], zoom_start = 11)
```

## Criei uma variável chamada "coordenadas" que recebeu um "zip" das coordenadas do DataFrame.
#### zip() é uma função do Python que recebe um ou mais iteráveis e retorna como um iterador de tuplas onde cada elemento dos iteráveis são pareados.
```
coordenadas = list(zip(df.latitude, df.longitude))
```

## Foi criado então o mapa de calor recebendo como argumento a variável "coordenadas".
```mapa_calor = HeatMap(coordenadas, radius=9, blur=10)```

## O mapa de calor foi adicionado ao mapa inicial e por fim plotado.
```
mapa.add_child(mapa_calor)
```

## Após isso foi usado a mesma estrutura, porém, dessa vez a análise foi feita em clusters:
```
from folium.plugins import MarkerCluster
mapa = folium.Map(location=[-30.1, -51.15], zoom_start=11)
mapa_cluster = MarkerCluster(coordenadas)
mapa.add_child(mapa_cluster)
```

## Decidi fazer um gráfico de barras, com os valores da quantidade de acidentes por ano, mas para isso precisei tratar a coluna de datas e agrupar a quantidade de acidentes por ano.
```
df['data'] = pd.to_datetime(df['data'])
df_ano = df['data'].dt.year.value_counts()
```

## Foi observado que tinha um dado inconsistente de um ano que não existe, então esse dado foi descartado.
```
df_ano = df_ano.drop(2202)
```

## Como mais um passo da análise, decidi plotar os dados dados no gráfico de barras tendo como cor um gradiente, onde a menor quantidade era um tom de azul mais claro e a maior quantidade era um tom de azul mais escuro.
```
gradiente = df_ano/df_ano.max()
cores = plt.cm.Blues(gradiente)
```

## Por fim o gráfico foi plotado.
```
plt.bar(df_ano.index, df_ano.values, color = cores)
plt.show()
```
