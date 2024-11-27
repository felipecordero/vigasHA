import webbrowser

import constants
import streamlit as st
from calculator import calculate
from svg_generator import create_beam_svg

def webfelipe():
    webbrowser.open("https://felipecordero.cl")

st.set_page_config(
    page_title="Beam Calculator - Felipe Cordero",
    page_icon="👷",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'https://felipecordero.com',
        'Get help': "https://linkedin.com/in/felipe-cordero-osorio",
    }
)
col1, col2 = st.columns((1,2), vertical_alignment="center")
with col1:
    st.title("👷 Beam Calculator 🏗️")
with col2:
    st.markdown("[**felipecordero.com**](https://felipecordero.com)")

# st.markdown("""
# <style>
# button {
#     height: 100px;
#     width: 100px;
#     color: blue;
# }
# </style>
# """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([0.5, 0.5, 0.5, 1])

results = None

# st.session_state.first_run = True

with col1:
    with st.container(border=True):
        st.subheader("Design Parameter", anchor=False)
        fc = st.selectbox("Concrete:", options=constants.fc.keys(), index=2)
        fy = st.selectbox("Steel: ", options=constants.fy.keys(),)
        tipo = st.selectbox("Beam type", options=constants.res.keys())
with col2:
    with st.container(border=True):
        st.subheader("Dimensions", anchor=False)
        L = st.number_input("Span [m]", value=5.0, step=0.5)
        B = st.number_input("Beam Width [cm]", value=30., step=5.)
        H = st.number_input("Beam Height [cm]", value=50., step=5.)
        r = st.number_input("Concrete Cover [cm]", value=2)

with col3:
    with st.container(border=True):
        st.subheader("Loads", anchor=False)
        a = st.number_input("Tributary width [m]", value=3.0, step=0.5)
        e = st.number_input("Slab tickness [cm]", value=15., step=5.)
        cm = st.number_input("Dead Load [kg/m²]", value=100., step=25.)
        sc = st.number_input("Live Load [kg/m²]", value=200., step=25.)

with col4:

    if st.button("**Calculate 📐**",type="primary") or "first_run" not in st.session_state:
        results, qu = calculate(float(constants.fc[fc]),
                                float(constants.fy[fy]),
                                float(constants.E[fc]) * 101.972,  # ton/m2
                                L,
                                B,
                                H,
                                r,
                                a,
                                e,
                                cm,
                                sc,
                                tipo
                            )
        st.session_state["first_run"] = True

if results is not None:

    # Función para dividir el contenido de las celdas en nuevas líneas
    def split_cells(cell):
        return '<br>'.join(cell.split('; '))
    
    # # Aplicar la función a la columna deseada
    # results['Left Side'] = results['Left Side'].apply(split_cells)
    # results['Center Side'] = results['Center Side'].apply(split_cells)
    # results['Right Side'] = results['Right Side'].apply(split_cells)

    # The results
    c1, _ = st.columns((1, 0.25))
    r = c1.container(border=True)
    r.subheader("Results 📈")
    r.dataframe(results, hide_index=True, use_container_width=True) 
    # r.write(results.to_html(escape=False, index=False), unsafe_allow_html=True)

    # # Explode only the cells with lists
    # def explode_mixed_cells(df, col):
    #     df[col] = df[col].apply(lambda x: x if isinstance(x, list) else [x])
    #     return df.explode(col, ignore_index=True)

    # # Apply the function to the 'Hobbies' column
    # expanded_df = explode_mixed_cells(results, 'Left Side')
    # r.dataframe(expanded_df)

    col1, col2 = st.columns((1, 1))

    svg_cross_sec, svg_elev = create_beam_svg(L, B, H, a, e, qu, tipo)

    # The cross section
    r = col1.container(border=True)
    r.subheader("Cross Section")
    r.image(svg_cross_sec, width=600)

    # The Elevation
    r = col2.container(border=True)
    r.subheader("Elevation")
    r.image(svg_elev, width=600)