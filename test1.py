import streamlit as st
st.write("Hello ,Edunet Foundation")
 
 
st.write("st.write(): This function is used to add anything to a web app")

import streamlit as st
st.title("Edunet - APP")
st.header("Content Quality Team")
st.markdown("Skill4Future")
st.subheader("TSP")
st.caption("Micro Degree")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''') 

import streamlit as st
st.title("Edunet - APP")
st.header("Content Quality Team")
st.markdown("Skill4Future")
st.subheader("TSP")
st.caption("Micro Degree")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''') 


import streamlit as st
 
st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 100)
 
import numpy as np 
st.number_input('Pick a number between (1-10)', 0,10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('Office time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

import streamlit as st
st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))


import streamlit as st
st.sidebar.markdown("This is the sidebar content")
st.sidebar.title("DDRS")
st.sidebar.button("click")
st.sidebar.radio("Pick your team",["TSP","S4F","EY","CU"])
 
container = st.container()
container.write("This is written inside the container")
 
st.write("This is written outside the container") 

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
 
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
 
 
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df, color=(0,255,255))
 
st.bar_chart(df, color=(0,255,0))
 
st.area_chart(df)
 
df1 = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df1).mark_circle().encode(x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(chart, use_container_width=True)
 
 
df3 = pd.DataFrame(np.random.randn(600, 2) / [50, 50] + [37.76, -87.4], columns=['lat', 'lon'])
st.map(df3)


