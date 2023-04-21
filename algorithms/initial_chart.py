import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time


def display_initial_chart(x, lst):
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color="blue")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Bubble Sort Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)
