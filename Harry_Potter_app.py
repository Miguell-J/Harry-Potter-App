import streamlit as st
import pandas as pd
import plotly.express as px

feiticost_data = {
    'Feitiço': [
        'Expelliarmus', 'Expecto Patronum', 'Accio', 'Lumos', 'Nox', 
        'Alohomora', 'Wingardium Leviosa', 'Avada Kedavra', 'Protego', 'Riddikulus',
        'Stupefy', 'Impedimenta', 'Aguamenti', 'Legilimens', 'Obliviate',
        'Sectumsempra', 'Lumos Solem', 'Muffliato', 'Incarcerous', 'Crucio',
        'Imperio', 'Diffindo', 'Episkey', 'Avis', 'Reducto',
        'Aparecium', 'Silencio', 'Evanesco', 'Furnunculus', 'Langlock',
        'Locomotor Mortis', 'Petrificus Totalus', 'Reparo', 'Tarantallegra', 'Bombarda',
        'Colloportus', 'Deletrius', 'Densaugeo', 'Lumos Maxima', 'Ferula',
        'Arania Exumai', 'Brackium Emendo', 'Aqua Eructo', 'Nox', 'Sonorus',
    ],
    'Descrição': [
        'Desarma o oponente', 'Invoca um Patrono', 'Atrai objetos', 'Ilumina a varinha', 'Apaga a luz',
        'Abre portas e fechaduras', 'Levita objetos', 'Mata instantaneamente', 'Cria um escudo mágico', 'Transforma o Bicho-Papão em algo engraçado',
        'Stupefy - Atordoa o alvo', 'Impedimenta - Impede movimentos do alvo', 'Aguamenti - Produz água', 'Legilimens - Lê mentes', 'Obliviate - Apaga memórias',
        'Sectumsempra - Corta profundamente o alvo', 'Lumos Solem - Feixe de luz solar', 'Muffliato - Evita que outros ouçam', 'Incarcerous - Amarra o alvo', 'Crucio - Causa dor excruciante',
        'Imperio - Controla a mente do alvo', 'Diffindo - Corta objetos', 'Episkey - Cura ferimentos leves', 'Avis - Conjure aves', 'Reducto - Quebra objetos',
        'Aparecium - Revela texto invisível', 'Silencio - Silencia objetos ou criaturas', 'Evanesco - Faz objetos desaparecerem', 'Furnunculus - Causa furúnculos no alvo', 'Langlock - Cola a língua no céu da boca',
        'Locomotor Mortis - Prende as pernas do alvo', 'Petrificus Totalus - Petrifica o alvo', 'Reparo - Repara objetos', 'Tarantallegra - Faz o alvo dançar', 'Bombarda - Causa explosões',
        'Colloportus - Trava portas', 'Deletrius - Desfaz encantamentos', 'Densaugeo - Faz os dentes crescerem', 'Lumos Maxima - Ilumina intensamente', 'Ferula - Conjure ataduras',
        'Arania Exumai - Afasta aranhas', 'Brackium Emendo - Cura ossos quebrados', 'Aqua Eructo - Produz jatos de água', 'Nox - Apaga a luz', 'Sonorus - Aumenta o volume da voz',
    ],
    'Categoria': [
        'Desarmamento', 'Defesa contra as Artes das Trevas', 'Encantamento', 'Encantamento', 'Feitiço',
        'Feitiço', 'Feitiço', 'Maldição', 'Feitiço', 'Feitiço',
        'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
        'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
        'Maldição', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
        'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
        'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
        'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
        'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço', 'Feitiço',
    ],
    'Livro/Filme': [
        'Pedra Filosofal', 'Prisioneiro de Azkaban', 'Cálice de Fogo', 'Ordem da Fênix', 'Enigma do Príncipe', 
        'Pedra Filosofal', 'Prisioneiro de Azkaban', 'Ordem da Fênix', 'Relíquias da Morte', 'Prisioneiro de Azkaban',
        'Ordem da Fênix', 'Prisioneiro de Azkaban', 'Cálice de Fogo', 'Relíquias da Morte', 'Cálice de Fogo',
        'Enigma do Príncipe', 'Cálice de Fogo', 'Enigma do Príncipe', 'Prisioneiro de Azkaban', 'Ordem da Fênix',
        'Relíquias da Morte', 'Enigma do Príncipe', 'Prisioneiro de Azkaban', 'Ordem da Fênix', 'Pedra Filosofal',
        'Cálice de Fogo', 'Pedra Filosofal', 'Prisioneiro de Azkaban', 'Cálice de Fogo', 'Prisioneiro de Azkaban',
        'Cálice de Fogo', 'Relíquias da Morte', 'Prisioneiro de Azkaban', 'Cálice de Fogo', 'Prisioneiro de Azkaban',
        'Ordem da Fênix', 'Cálice de Fogo', 'Relíquias da Morte', 'Pedra Filosofal', 'Enigma do Príncipe',
        'Ordem da Fênix', 'Pedra Filosofal', 'Enigma do Príncipe', 'Cálice de Fogo', 'Ordem da Fênix',
    ],
}

df_feiticost = pd.DataFrame(feiticost_data)

# Estilo da página
st.set_page_config(
    page_title="Feitiços de Harry Potter",
    page_icon="✨",
    layout="centered",
)

# Estilo do Streamlit
st.markdown(
    """
    <style>
        .css-1l02zno {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
        }

        .st-bj {
            padding: 0.5rem;
            border-radius: 5px;
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
            background-color: #ffffff;
        }

        .st-cq {
            background-color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image('https://cdn.folhape.com.br/img/pc/1100/1/dn_arquivo/2020/04/0956331-copia-2.jpg', use_column_width=True)

# Título
st.title('Feitiços de Harry Potter 🧙🏼‍♂️')

# Sidebar
st.sidebar.title('Filtros')

# Busca por nome
busca_nome = st.sidebar.text_input('Buscar por Nome:')
if busca_nome:
    df_feiticost = df_feiticost[df_feiticost['Feitiço'].str.contains(busca_nome, case=False)]

# Estatísticas
st.sidebar.subheader('Estatísticas')
st.sidebar.write(f"Total de Feitiços: {len(df_feiticost)}")
st.sidebar.write(f"Categorias: {', '.join(df_feiticost['Categoria'].unique())}")

# Filtrar dados com base na categoria selecionada
categoria_selecionada = st.sidebar.selectbox('Selecionar Categoria', df_feiticost['Categoria'].unique())
df_categoria = df_feiticost[df_feiticost['Categoria'] == categoria_selecionada]

# Filtrar por livro/filme
livro_selecionado = st.sidebar.selectbox('Selecionar Livro/Filme', df_feiticost['Livro/Filme'].unique())
df_livro = df_feiticost[df_feiticost['Livro/Filme'] == livro_selecionado]

# Selecionar um feitiço aleatório da categoria
feiticost_aleatorio = st.sidebar.button('Sortear Feitiço Aleatório da Categoria')

if feiticost_aleatorio:
    feitico_selecionado = df_categoria.sample(1)
    st.subheader('Feitiço Selecionado:')
    st.write(feitico_selecionado['Feitiço'].values[0])
    st.write('Descrição:', feitico_selecionado['Descrição'].values[0])
    st.write('Categoria:', feitico_selecionado['Categoria'].values[0])
    st.write('Livro/Filme:', feitico_selecionado['Livro/Filme'].values[0])

# Gráfico de distribuição por categoria
fig_categoria = px.histogram(df_feiticost, x='Categoria', title='Distribuição de Feitiços por Categoria')
st.plotly_chart(fig_categoria, use_container_width=True)

# Gráfico de distribuição por livro/filme
fig_livro = px.histogram(df_feiticost, x='Livro/Filme', title='Distribuição de Feitiços por Livro/Filme')
st.plotly_chart(fig_livro, use_container_width=True)

# Lista de feitiços
st.subheader('Lista de Feitiços:')
st.table(df_categoria)