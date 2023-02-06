import pandas as pd
import numpy as np
import streamlit as st
from scipy.stats import hypergeom

st.markdown("""# Bienvenue dans le Magic""")

M = st.number_input('Combien de cartes te reste-t-il dans ton deck ?', 100)

n = st.number_input('Combien de cartes cibles te reste-t-il dans ton deck ?', 42)

if n > M :
    print(f"Tu dois faire un erreur, je doute serieusement qu'il te reste {n} cartes cible si ton deck n'a plus que {M} cartes")
nn = min (M,n)

N = st.number_input('Combien de cartes vas-tu piocher ?', 7)

if N > M :
    print(f"Attention, tu as de serieuses chances de perdre si tu pioches {N} cartes et que ton deck n'a plus que {M} cartes")
NN = min (M,N)
    
x = np.arange(0, NN+1)
hypergeom_law = hypergeom(M,nn,NN)

pmf = hypergeom_law.pmf(x)
cmf = np.cumsum(pmf)

hypergeom_dict = {
    'Nombre de cartes cibles piochées':x,
    'Probabilité de piocher exacteemnt ce nombre':pmf,
    'Probabilité de piocher au moins ce nombre':cmf
}

df = pd.DataFrame(hypergeom_dict).set_index('Nombre de cartes cibles piochées').apply(lambda x: 100 *x)


st.write(df)
