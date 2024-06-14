# Parte Prática - Prova 2 (Módulo 6)

## Prova de Conceito
### Instruções para execução
#### Clone o Repositório
Coloque esse comando no terminal

```git clone https://github.com/cecigonca/prova2-m6.git```

#### Ative o Ambiente Virtual (terminal Windows)
Navegue até o diretorio

```/../prova2-m6/```

Rode os comandos seguintes

```python -m venv venv```

```./venv/Scripts/activate```

#### Instale as dependências
```python -m pip install -r requirements.txt```

#### Executar
No diretorio ```/../prova2-m6/```

Rode o seguinte comando ```python prova.py```


## Perguntas Técnicas
### 2.1
O método de detecção escolhido foi o Haar Cascade, esse método é baseado em recursos visuais já aprendidos, nesse caso, com diversas imagens com rostos e sem rostos. Para acelerar o processamento, os frames do vídeo original foram convertidos para escala de cinza. A partir disso, é aplicado um quadro para reconhecimento de padrões e posteriormente são aplicados filtros retângulares para finalmente fazer a detecção do que está sendo procurado. Essa deteccção é feita com base na intensidade de pixels e demandam ajustes conforme condições de iluminação e orientação das faces.

### 2.2

#### 1º - **CNN**
Justificativa: Eficaz no reconhecimento facial por sua alta capacidade de aprendizado de características complexas, resultando em uma alta viabilidade técnica. Além disso, pode ser adaptada para diferentes tipos de imagens e é facilmente escalável. Único contraponto seria a dificuldade de implementação, exige um treinamento e requer conhecimento alguns frameworks.
#### 2º - **HAAR Cascade**
Justificativa: É uma técnica mais simples se implementar e não demanda muito tempo, além disso, é eficiente para detecção de rostos. O ponto negativo seria sua limitação em reconhecer faces que não estão no padrão de posicão esperado.
#### 3º - **Filtros de Correlação Cruzada**
Justificativa: Funcionam para detcção de fces mas são menos eficazes que CNN e Haar Cascade. Tem uma implementação fácil, mas não são práticos devido a sua limitação a detecções mais complexas. Funciona bem quando o rosto está em destaque, mas pode falhar quando há muitas alterações.
#### 4º - **NN Linear**
Justificativa: Por mais que sejam muito fáceis de implementar, é a opção menos viável para esse tipo de tarefa. São muito limitadas e assumem uma relação linear entre as entradas e saídas, o que não é a solução indicada para detecção de faces. 


### 2.3

#### 1º - **CNN**
Justificativa: Pelo seu processo de treinamento, capacidade de aprendizado e interpretação de padrões, é a opção mais indicada para deteccão de expressões faciais.
#### 2º - **HAAR Cascade**
Justificativa: Menos eficaz na detecção de emoções específicas justamente pelo limitação em reconhecer faces fora da orientação esperada e muitas vezes por não ter o treinamento necessário. 
#### 3º - **NN Linear**
Justificativa: Por assumirem uma relação linear entre as entradas e saídas, não possuem a capacidade de identificar características mais complexas.
#### 4º - **Filtros de Correlação Cruzada**
Justificativa: Esse tipo de abordagem é focado em características simples, dificultando a detecção de expressões faciais.

### 2.4
- 

### 2.5
Vini Jr
