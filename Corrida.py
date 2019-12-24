import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import os
import time

def main():
    """ Sao Silvestre """

    # Titulo
    st.title("	STREAMLIT ")
    st.markdown("### Lib Python for Web Apps")

    st.title("Corrida de São Silvestre")
    #st.markdown("### Periodo: 1991 a 2018")

    st.sidebar.markdown("## by Silvio Lima")

    st.sidebar.markdown('## Dados Historicos')

    if st.sidebar.checkbox("História"):
        #st.markdown("### Fatos e Fotos ")
        option = st.sidebar.selectbox('Qual deseja: ', ['Fatos', 'Fotos'])
        st.write(option)
        if  (option == 'Fatos'):
            st.markdown('## 1925 - largada da Primeira corrida')
            st.markdown('Vencedor: Alfredo Gomes - Brasileiro')
            st.markdown('Distância: 6200m  Tempo: 0:23:10')
            st.markdown('146 participantes - 60 completaram')
            st.markdown('## 1946 - apenas atletas do continente eram convidados')
            st.markdown('O sucesso levou a abrir para todos paises em 1947')
            st.markdown('## 1975 - mulheres passaram a participar')
            st.markdown('Christa Vahlensieck, Alemã, primeira campeã.')
            st.markdown('Distância: 8900m Tempo: 0:28:39')
            st.markdown('14 atletas - 12 completaram.')
            st.markdown('## 1988 - prova passou a ser disputada de dia')
            st.markdown('## 1991 - o percurso é estabelecido como 15km')
            
        if (option == "Fotos"):
            st.text(" ")
            st.markdown("### Largada - 1925")
            my_placeholder = st.empty()
            my_placeholder.image('Largada1925.PNG')
            st.text(' ')
            st.markdown("### Última corrida noturna foi em 1988")
            my_placeholder = st.empty()
            my_placeholder.image('corrida_1968.png')
            st.text(" ")
            st.markdown("### Emil Zatopek _ a Locomotiva Humana - campeão em 1952")
            my_placeholder = st.empty()
            my_placeholder.image('Emil-1952.jpg')
            st.text(" ")
            st.markdown("### Primeira prova feminina - 1975")
            st.text(" ")
            my_placeholder = st.empty()
            my_placeholder.image('1975.png')
            st.text(" ")
            st.markdown("### Chegada noturna - 1972")
            my_placeholder = st.empty()
            my_placeholder.image('Capa.png')
            st.balloons()
        


    def ler_dados(dataset):
        loaded = pd.read_csv(os.path.join(dataset)) # index_col=0
        return loaded

    # Carregar dataset
    my_dataset = "dataset.csv"
    data = ler_dados(my_dataset)

    if st.sidebar.checkbox("Dataset"):
            st.markdown("## Periodo: 1991 a 2018")
            st.write("28 observações / 9 atributos")
            st.table(data.head(30))

    #Processando os dados
    df = data
    df[['hour_TempoM', 'minute_TempoM', 'second_TempoM']] = df['TempoM'].astype(str).str.split(':', expand=True).astype(int)
    df[['hour_TempoH', 'minute_TempoH', 'second_TempoH']] = df['TempoH'].astype(str).str.split(':', expand=True).astype(int)
    df.drop(['TempoM','TempoH','second_TempoM','second_TempoH'], axis=1, inplace=True)
    df= df.rename(columns={'hour_TempoM': 'minM', 'minute_TempoM': 'segM','hour_TempoH':'minH','minute_TempoH':'segH'} )
    df['SegM'] = df['minM']*60+df['segM']
    df['SegH'] = df['minH']*60+df['segH']
    df.drop(['minM','minH','segM','segH'], axis=1, inplace=True)
    df['Dif'] = df.SegM - df.SegH
    datap = df

    if (st.sidebar.checkbox("Vencedores")):
        st.markdown("## Periodo: 1991 a 2018")
        st.balloons()
        option = st.sidebar.selectbox('Qual deseja: ', ['Paises', 'Homens', 'Mulheres'])
        st.write(option)
        if  (option == 'Paises'):
            df_Pais_H = data['Pais-H'].value_counts()
            vitorias_P = df_Pais_H.to_frame(name = 'Vitórias')
            st.table(vitorias_P)
        if (option == "Homens"):
            df_H = data['Homens'].value_counts()
            vitorias_H = df_H.to_frame(name = 'Vitórias')
            st.table(vitorias_H)
        if (option == "Mulheres"):
            df_M = data['Mulheres'].value_counts()
            vitorias_M = df_M.to_frame(name = 'Vitórias')
            st.table(vitorias_M)


    if st.sidebar.checkbox("Gráficos"):
        st.markdown("## Periodo: 1991 a 2018")
        option = st.sidebar.selectbox('Qual deseja',['Idade','Tempo','Diferença'])
        st.write(option)
        if (option == 'Idade'):
            x = data['Ano']
            p = figure(title='Idade do vencedor(a)',x_axis_label='Ano',y_axis_label='Idade (anos)')
            p.line(x, data['Idade-M'], legend_label='Mulher', line_width=2, color='blue')
            p.line(x, data['Idade-H'], legend_label='Homem', line_width=2, color='red')
            st.bokeh_chart(p)
        if (option == "Tempo"):
            x = data['Ano']
            p = figure(title='Tempo de corrida de mulheres e homens',x_axis_label='Ano',y_axis_label='Tempo (segundos)')
            p.line(x, datap['SegH'], legend_label='Homem', line_width=2, color='red')
            p.line(x, datap['SegM'], legend_label='Mulher', line_width=2, color='blue')
            st.bokeh_chart(p)
        if (option == "Diferença"):
            x = data['Ano']
            p = figure(title='Diferença de Tempo entre mulheres e homens',x_axis_label='Ano',y_axis_label='Diferença de tempo(segundos)')
            p.line(x, datap['Dif'], legend_label='Diferença', line_width=2, color='red')
            st.bokeh_chart(p)
    
 

if __name__ == '__main__':
    main()
