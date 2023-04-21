import streamlit as st
from PIL import Image
from time import sleep

pl = st.empty()
img1 = Image.open("img1.jpg")
pl.image(img1, use_column_width=True)
sleep(2)
img2 = Image.open("img2.jpg")
pl.image(img2, use_column_width=True)
pl.plotly_chart()
