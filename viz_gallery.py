#######################################
# ----Tools and Page setup----
#######################################
import json
import requests
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import subprocess
import sys
import defined
from defined import pub_search_code


# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/. 
# st.set_page_config(page_title="TMB Show Case Gallery", page_icon=":sparkles:", layout = "wide")
st.set_page_config(page_title="TMB Show Case Gallery", page_icon=":sunflower:", layout = "wide")

# Using local files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


with st.container(): 
  st.markdown("<h1 style='text-align: center; color: grey;'>Template: TMB Visualization Gallery</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: black;'>Selected Images with Collapsible Code</h3>", unsafe_allow_html=True)
  
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>1. Microbiome Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...Spaceholder Images...</h3>", unsafe_allow_html=True)

  header1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with header1:
      st.success(
        """
        ### Stacked Bar plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
          
  with separator1: 
      st.write("")

  with panel2:
      st.success(
        """
        ### Box plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
        
  with separator2: 
      st.write("")

  with panel3:
      st.success(
        """
        ### Histogram
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
  
##################################
##################################

with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>2. Interactive & Web Apps</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...Spaceholder Images...</h3>", unsafe_allow_html=True)

  header1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with header1:
      st.success(
        """
        ### Stacked Bar plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
          
  with separator1: 
      st.write("")

  with panel2:
      st.success(
        """
        ### Box plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
        
  with separator2: 
      st.write("")

  with panel3:
      st.success(
        """
        ### Histogram
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
  
##################################
##################################

with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>3. Machine Learning</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...Spaceholder Images...</h3>", unsafe_allow_html=True)

  header1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with header1:
      st.success(
        """
        ### Stacked Bar plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
          
  with separator1: 
      st.write("")

  with panel2:
      st.success(
        """
        ### Box plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
        
  with separator2: 
      st.write("")

  with panel3:
      st.success(
        """
        ### Histogram
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
  
##################################
##################################
with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>4. Quantitative Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...Spaceholder Images...</h3>", unsafe_allow_html=True)

  header1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with header1:
      st.success(
        """
        ### Stacked Bar plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
          
  with separator1: 
      st.write("")

  with panel2:
      st.success(
        """
        ### Box plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
        
  with separator2: 
      st.write("")

  with panel3:
      st.success(
        """
        ### Histogram
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
  
##################################
##################################

with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>5. Flow Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...Spaceholder Images...</h3>", unsafe_allow_html=True)

  header1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with header1:
      st.success(
        """
        ### Stacked Bar plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
          
  with separator1: 
      st.write("")

  with panel2:
      st.success(
        """
        ### Box plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
        
  with separator2: 
      st.write("")

  with panel3:
      st.success(
        """
        ### Histogram
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
  
##################################
##################################
with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>5. GIS Mapping</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...Spaceholder Images...</h3>", unsafe_allow_html=True)

  header1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with header1:
      st.success(
        """
        ### Stacked Bar plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
          
  with separator1: 
      st.write("")

  with panel2:
      st.success(
        """
        ### Box plot
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
        
  with separator2: 
      st.write("")

  with panel3:
      st.success(
        """
        ### Histogram
        """)
      image = Image.open("figures/pubmed_search_bar_plot.png")
      st.image(image)
      st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
      # st.subheader("Creating a plot using `ggplot2`")
      with st.expander("Click to see or copy the R code"):
        st.code(pub_search_code, language="R")
  
##################################
##################################
st.write("##")
st.write("##")
with st.container():
  st.write("---")
  st.markdown("<h2 style='text-align: left; color: orange;'>Let\'s Collaborate to Make Stronger Impacts</h2>", unsafe_allow_html=True)
  
  # Contact Documentation: https://formsubmit.co/ Change the email address
  contact_form = """
  <form action="https://formsubmit.co/ndelly@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
  </form>
  """
  
# Use local css file
  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
      
  local_css("style/style.css")
  
  
  left_column, right_column = st.columns(2)
  with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
  with right_column:
    # st.empty()
    st.image("https://complexdatainsights.com/wp-content/uploads/2020/09/contactNewk.png")

