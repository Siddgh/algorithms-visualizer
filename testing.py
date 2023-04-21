import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from algorithms.bubble_sort import perform_and_display_bubble_sort
from algorithms.initial_chart import display_initial_chart

# Create some example data for the plots
x = np.linspace(0, 10, 100)
amount = 10
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

# Create a Streamlit app
st.set_page_config(page_title="Matplotlib Plots", layout="wide")

heading = st.markdown(
    """
        <h1 style='text-align: center; color: black;'>Sorting Algorithms Visualizer</h1>
    """,
    unsafe_allow_html=True,
)

m = st.markdown(
    """
<style>

div.stTitle{
    margin: auto;
    display: block;
    position:relative;
	top:3px;
}

div.stButton > button:first-child {
    background-color: #e67e22;
    color: white;
    height: 3em;
    width: 12em;
    border-radius:10px;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background-color:#e67e22;
    border:2px solid #000000;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""",
    unsafe_allow_html=True,
)

should_run = st.button("Run", type="primary")
col1, col2, col3, col4 = st.columns(4)

# Plot 1
with col1:
    st.subheader("Plot 1")
    if should_run == True:
        # Adjust the height of the plot
        plt.figure(figsize=(6, 3))
        perform_and_display_bubble_sort(x, lst)
    else:
        display_initial_chart(x, lst)

# Plot 2
with col2:
    st.subheader("Plot 2")
    if should_run == True:
        # Adjust the height of the plot
        plt.figure(figsize=(6, 3))
        perform_and_display_bubble_sort(x, lst)
    else:
        display_initial_chart(x, lst)

# Plot 3
with col3:
    st.subheader("Plot 3")
    if should_run == True:
        # Adjust the height of the plot
        plt.figure(figsize=(6, 3))
        perform_and_display_bubble_sort(x, lst)
    else:
        display_initial_chart(x, lst)

# Plot 4
with col4:
    st.subheader("Plot 4")
    if should_run == True:
        # Adjust the height of the plot
        plt.figure(figsize=(6, 3))
        perform_and_display_bubble_sort(x, lst)
    else:
        display_initial_chart(x, lst)


# Show the plots
plt.show()
