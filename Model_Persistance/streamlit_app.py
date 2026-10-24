import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

pkfile = open(r"C:\Users\PGCP-AI.STUDENTSDC\Desktop\Machine_Learning\BreastCancer_rfc.pkl","rb")
load_model = pkl.load(pkfile)
pkfile.close()

st.title('Breast Cancer')
col1, col2, col3, = st.columns([0.3,0.3,0.3])

with col1:
    Clump = st.slider(label='Clumb Thickness :', min_value=0, max_value=10,step=1)
    UniCell_Size = st.slider(label='Uniformity Of Cell Size :', min_value=0, max_value=10,step=1)
    Uni_CellShape = st.slider(label='Uniformity Of Cell Shape :', min_value=0, max_value=10,step=1)

with col2:
    MargAdh = st.slider(label='Marginal Adhesion :', min_value=0, max_value=10,step=1)
    SEpith =  st.slider(label='Single epithelial Cell Size :', min_value=0, max_value=10,step=1)
    BareN =  st.slider(label='Bare Nuclei :', min_value=0, max_value=10,step=1)

with col3:
    BChromatin =  st.slider(label='Bland Chromatin :', min_value=0, max_value=10,step=1)
    NoemN =  st.slider(label='Normal Nucleoli :', min_value=0, max_value=10,step=1)
    Mitoses =  st.slider(label='Mitoses :', min_value=0, max_value=10,step=1)

df = pd.DataFrame(
    {
        'Clump':[Clump], 
        'UniCell_Size':[UniCell_Size], 
        'Uni_CellShape':[Uni_CellShape], 
        'MargAdh':[MargAdh], 
        'SEpith':[SEpith], 
        'BareN':[BareN],
        'BChromatin':[BChromatin], 
        'NoemN':[NoemN], 
        'Mitoses':[Mitoses]
    }
)

pred = load_model.predict(df)[0]
st.write('Predicted Class : {}'.format(pred))