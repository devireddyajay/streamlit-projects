import streamlit as st
import time
import numpy as np
st.write(f"Streamlit version: {st.__version__}")

progress_bar=st.sidebar.progress(0)
status_text=st.sidebar.empty()


lastrow=np.random.randn(1,1)
chart = st.line_chart(lastrow)

for i in range(1,101):
    newrow=lastrow[-1,:]+np.random.randn(5,1).cumsum(axis=0)
    status_text.text("%i%% complete"%i)
    progress_bar.progress(i)
    chart.add_rows(newrow)
    lastrow=newrow
    time.sleep(0.1)
progress_bar.empty()    
st.button("Re-run")
