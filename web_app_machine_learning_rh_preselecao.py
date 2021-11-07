#!/usr/bin/env python
# coding: utf-8

# # Construção de aplicação web
# 
# 
# # Objetivo geral:
# Rodar modelo de machine learning classificador para processo seletivo
# 
# # Objetivo específico:
# O modelo será usado para indicar quais candidatos permanecerão na empresa ao menos 2 anos

# In[2]:


#Importação das bibliotecas
import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.markdown('*__Observação: para mais informações, clique na seta no canto esquerdo superior da tela__* ')

st.sidebar.title('Projeto de portfólio de Ciência de Dados')
st.sidebar.markdown('Feito por : Bruno Rodrigues Carloto')
st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://br-cienciadedados.medium.com)")
st.sidebar.markdown("- [Github](https://github.com/brunnosjob)")

#Cabeçalho
st.title('Machine Learning para o RH')
st.markdown('#### Modelo de machine learning classificador para uso em pré-seleção a vaga de emprego')

#Título
st.write("O modelo tem como objetivo classificar para a próxima fase do processo seletivo somente os candidatos que ficarão ao menos dois anos na empresa")

#Criando variáveis 
candidato =  st.text_input('Digite o nome do candidato:')
cargo = st.selectbox('Vagas disponíveis', ['Analista Comercial I', 'Analista de Dados I', 'Auxiliar de Suporte de TI',
                                            'Contador I', 'Gerente Comercial', 'Gerente de BI'])
sexo = st.selectbox('Selecione o sexo', ['M', 'F'])
estado_civil = st.selectbox('Selecione o estado civil', ['Casado(a)', 'Solteiro'])
motivo_saida = st.selectbox('Selecione o motivo de saída da empresa anterior', ['Abandono', 'Excesso de Faltas', 'Infeliz', 'Mal comportamento',
                                                                                'Mudança de Carreira', 'N/A - Empregado', 'Performance',
                                                                                'Proposta do Concorrente'])
fonte_recrutamento = st.selectbox('Selecione a fonte de inscrição para a vaga', ['Feira de Contratação', 'Indicação Funcionários',
                                                                        'Site da Empresa', 'Site de Vagas'])
salario = st.number_input('Selecione a pretensão salarial', 0, 5000, 0)
projetos = st.number_input('Selecione a quantidade de projetos apresentados na empresa anterior', 0, 20, 0)
idade = st.number_input('Selecione a idade', 0, 70, 0)
tempo_empresa = st.number_input('Selecione o tempo de serviço na empresa anterior', 0, 60, 0)

#Criando variável com dados do candidato
#Retornando os dados

st.subheader('Resultado')

#Abrindo o modelo
with open('machine_learning_pre_selecao_rh.pkl', 'rb') as f:
    scaler, onehot, logistic_model_tomek = pickle.load(f)
    
#Variáveis categóricas
categoricos = [[cargo, sexo, estado_civil, motivo_saida, fonte_recrutamento]]
categoricos_df = pd.DataFrame(categoricos)

#Conversão e criação de dataframe com valores convertidos
X_categoricos = onehot.transform(categoricos)
X_categoricos_df = pd.DataFrame(X_categoricos)

#Variáveis numéricas
numericos = [[salario, projetos, idade, tempo_empresa]]
numericos_df = pd.DataFrame(numericos) 

#Concatenando tipos de variáveis
dados = pd.concat([X_categoricos_df, numericos_df], axis=1)

#Padronizando
candidato_padronizado = scaler.transform(dados) 

#Resultado
resultado = logistic_model_tomek.predict(candidato_padronizado)
if resultado == 0:
    if sexo == 'M':
        st.write('Candidato {} está classificado para a próxima fase.'.format(candidato) )
    else:
        st.write('Candidata {} está classificada para a próxima fase.'.format(candidato))
else:
    if sexo == 'M':
        st.write('Candidato {} não está classificado para a próxima fase.'.format(candidato) )
    else:
        st.write('Candidata {} não está está classificada para a próxima fase.'.format(candidato))

