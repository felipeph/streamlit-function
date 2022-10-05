# Import the streamlit library to the app as st
import streamlit as st
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
from sympy.abc import *
from sympy import *
import matplotlib as mpl

# ------------- CONFIGURATIONS -----------------

# Set matplotlib parameters to default
mpl.rcParams.update(mpl.rcParamsDefault)

# Set the configuration of the page with TITLE and ICON
st.set_page_config(
    page_title="Functions",
    page_icon="👨‍🏫",
)

# ------------------------------------------------


# ----------- TEXT PARAMETERS -----------------
# Write down the function you want to analyze and press ENTER
txt_input = "Write the function you want to analyze. You can use x, y and z as variables."
# ----------------------------------------------

# Write the title of the page
st.title("Functions")

# Get the input of the user and save into the session state
function_input = st.text_input(txt_input, "x^2 + 3x + exp(x)", key="function_input")

if not function_input:
    st.stop()


# ------------- OPERATIONS WITH THE INPUT -------------------
# Parse the string of the raw input
function_parsed = parse_expr(function_input, transformations='all')

# Convert function to latex
function_latex = latex(function_parsed)

# Derivative with respect to x
derivative = diff(function_parsed, x)

# Integral of the function with respect to x
integral = integrate(function_parsed, x)

function_plot_instructions = plot(function_parsed, show = False)
function_plot = function_plot_instructions.show()


# -----------------------------------------------------------

# Show the function parsed
st.write("The parsed input:")
st.latex(function_latex)

# Show the derivative
st.write("Derivative of the function with respect to x")
st.latex(derivative)

# Show the integral
st.write("Integral of the function with respect to x")
st.write(integral)

# Show the latex code
st.write("LaTeX expression for this function")
st.write(function_latex)

st.write(function_plot_instructions)

st.pyplot(function_plot)

# Show the data saved
"Data saved"
st.session_state