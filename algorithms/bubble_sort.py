import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time


def perform_and_display_bubble_sort(x, lst):
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color="blue")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Bubble Sort Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            bar_plot[j].set_color("orange")
            bar_plot[j + 1].set_color("orange")
            plot_placeholder.pyplot(fig)

            time.sleep(0.1)

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

            bar_plot[j].set_height(lst[j])
            bar_plot[j + 1].set_height(lst[j + 1])
            bar_plot[j].set_color("blue")
            bar_plot[j + 1].set_color("blue")
            plot_placeholder.pyplot(fig)
