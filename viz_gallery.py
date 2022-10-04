#---------------------------------------------
# Tools and Page setup
#---------------------------------------------
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
st.set_page_config(
  page_title="TMB Gallery", 
  page_icon=":bar_chart:", 
  layout = "wide")

# Using local files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---------------------------------------------
# Assets
#---------------------------------------------
pubmed_stats = Image.open("figures/pubmed_search_bar_plot.png")
wcloud1 = Image.open("imgvideo/wordcloud.png")
gwas = Image.open("imgvideo/gwas_in_biome.png")

# For microbiome data analysis
gif1 = open("imgvideo/abund_bar.gif")

# For quantitative data analysis
fig1 = Image.open("imgvideo/climate_nasa.png")

vid1 = open("imgvideo/climate_spiral_nasa.mp4", "rb").read()


# For the NGS section
fig2 = Image.open("imgvideo/dna_composition.png")

#---------------------------------------------
# Main Body
#---------------------------------------------
with st.container(): 
  st.markdown("<h1 style='text-align: center; color: grey;'>TMB Data Visualization and Web Apps Gallery</h1> <h3 style='text-align: center; color: grey;'>Selected Images with Collapsible Code</h3>", unsafe_allow_html=True)
  
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>1. Microbiome Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...All images are spaceholhers...</h3>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with panel1:
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
  
#---------------------------------------------
#---------------------------------------------

with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>2. Interactive & Web Apps</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...All images are spaceholhers...</h3>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with panel1:
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
  
#---------------------------------------------
#---------------------------------------------

with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>3. Machine Learning</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...All images are spaceholhers...</h3>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with panel1:
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
  
#---------------------------------------------
#---------------------------------------------
with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>4. Quantitative Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...All images are spaceholhers...</h3>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with panel1:
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
  
#---------------------------------------------
#---------------------------------------------

with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>5. Flow Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='color: red;'>...All images are spaceholhers...</h3>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
  with panel1:
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
  
#---------------------------------------------
#---------------------------------------------
with st.container(): 
  st.write("##")
  st.markdown("<h1 style='text-align: left; color: skyblue;'>6. NGS Exploration</h1>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3, separator3, panel4 = st.columns((1.5, 0.2, 1.5, 0.2, 1, 0.2, 1))
  with panel1:
    st.info(
    """
    ### :question:Nucleotides in a DNA Sequence
    """)
    st.image(fig2)
    st.caption("Example of a DNA sequence with colors representing different nucleotide; A, T, C, G. How many each of these nucleotides are in a FASTA sequence?")
    
  with panel2:
    st.info(
      """
      ### Nucleotide Count APP
      """)
    st.markdown(
    """
    This web app quickly computes the number of nucleotides present in a FASTA sequence.
    `Give it a try!`
    """
    )

    sequence_input = ">Sequence1\nCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAGCACAGAGAGCTTGCTCTTGGGTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCCGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAACGTCTACGGACCAAAGT\GGGGGACCTTCGGGCCTCACACCATCGGATGTGCCCAGATGGGATTAGCTGGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGAT"
    
    sequence = st.text_area("Enter Fasta Sequence", sequence_input, height=150)
    sequence = sequence.splitlines()
    sequence = sequence[1:] # Skips the sequence name (first line)
    sequence = ''.join(sequence) # Concatenates list to string
    
    st.text_area("Clean Query Sequence", sequence, height=150)
    

  with panel3:
    st.success(
      """
      ### APP Output
      """)
    
    def DNA_nucleotide_count(seq):
      d = dict([
                ('A',seq.count('A')),
                ('T',seq.count('T')),
                ('G',seq.count('G')),
                ('C',seq.count('C'))
                ])
      return d
    
    X = DNA_nucleotide_count(sequence)
    
    # ### Nucleotide Count
    # st.subheader('1. Observation')
    # st.write('There are  ' + str(X['A']) + ' adenine (A)')
    # st.write('There are  ' + str(X['T']) + ' thymine (T)')
    # st.write('There are  ' + str(X['G']) + ' guanine (G)')
    # st.write('There are  ' + str(X['C']) + ' cytosine (C)')

    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'Count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'Nucleotide'})
    st.write(df)
    
  with panel4:
    st.success(
      """
      ### NT Count Bar Chart
      """)
      
    p = alt.Chart(df).mark_bar().encode(
        x='Nucleotide',
        y='Count'
    )
    p = p.properties(
        width=alt.Step(75)  # controls width of bar.
    )
    st.write(p)
    st.caption("Bar chart showing the number of nucleotide composition in a given DNA sequence.")
  
 
#---------------------------------------------
#---------------------------------------------
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

