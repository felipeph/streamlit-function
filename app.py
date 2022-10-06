# Framework that creates the app
import streamlit as st

# Parser that correct the users writing
from sympy.parsing.sympy_parser import parse_expr

# Plotting library from sympy
from sympy.plotting.plot import plot

# All the letters as symbols
from sympy.abc import *

# Makes the algebraic computation
import sympy as sp

# Plot the functions
import matplotlib as mpl

# ------------- CONFIGURATIONS -----------------

# Set matplotlib parameters to default
mpl.rcParams.update(mpl.rcParamsDefault)
# plt.rcParams['figure.figsize'] = [8.0, 8.0]
# plt.rcParams['figure.dpi'] = 120

# Set the configuration of the page with TITLE and ICON
st.set_page_config(
    page_title="Functions",
    page_icon="👨‍🏫",
)

st.set_option('deprecation.showPyplotGlobalUse', False)


# ------------------------------------------------


# ----------- TEXT PARAMETERS -----------------
# Write down the function you want to analyze and press ENTER
txt_input = "Write the function you want to analyze. You can use x, y and z as variables."
# ----------------------------------------------

# Write the title of the page
st.title("Functions")


with st.form("input"):
    input_area, submit_button_area = st.columns([10,1], gap="small")
    
    with input_area:
        function_input = st.text_input(txt_input, "x^2 + 50", key="function_input")    
    
    with submit_button_area:
        st.write(" ")
        st.write(" ")
        submitted = st.form_submit_button("✔")

# Get the input of the user and save into the session state
# function_input = st.text_input(txt_input, "x^2 + 3x + exp(x)", key="function_input")

#if not function_input:
#    st.stop()


# ------------- OPERATIONS WITH THE INPUT -------------------
# Parse the string of the raw input and convert to latex
function_parsed = parse_expr(function_input, transformations='all')
function_latex = sp.latex(function_parsed)

# Derivative with respect to x and convert to latex
derivative = sp.diff(function_parsed, x)
derivative_latex = sp.latex(derivative)

# Integral of the function with respect to x and convert to latex
integral = sp.integrate(function_parsed, x)
integral_latex = sp.latex(integral)

# -----------------------------------------------------------

tab_function, tab_derivative, tab_integral, tab_plot = st.tabs(["Function", "Derivative", "Integral", "Plot"])

# Show the function parsed
with tab_function:
    st.latex(r'''f(x)=''' + function_latex)

# Show the derivative
with tab_derivative:
    st.latex(r'''\frac{d}{dx} \left(''' + function_latex + r'''\right) = ''' + derivative_latex)

# Show the integral
with tab_integral:
    st.latex(r'''\int \left(''' + function_latex + r'''\right)dx = ''' + integral_latex + r'''+C''')

# Plot the function
with tab_plot:
    function_plot = plot(function_parsed, title="$f(x) = " + function_latex + "$", xlabel="", ylabel="", axis_center=(0,0), adaptive=False, nb_of_points=1000)
    st.pyplot(function_plot.show())
    

# Show the latex code
#st.write("LaTeX expression for this function")
#st.write(function_latex)


# Show the data saved
"Data saved"
st.session_state