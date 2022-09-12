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
st.set_page_config(page_title="TMB Portfolio", page_icon=":sparkles:", layout = "wide")

# Using local files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# def defined_code(file_name):
#     with open(file_name) as f:
#         st.markdown(f"{f.read()}", unsafe_allow_html=True)
# 
# defined_code("defined.py")


#######################################
# ----Assets----
#######################################

# For Professional Passion
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

#######################################
# ---- Header with salutation and introduction----
#######################################
with st.container():
  header1, separator, header2 = st.columns((2, 0.5, 2))
  with header1:
    st.warning(":warning:... this is work in progress, not complete or proofread yet.")
    st.subheader("Hi, I am Teresia Mrema-Buza:wave:")
    st.title("A Data Science, Bioinformatics, and Computational Biology Enthusiast, Consultant, and Mentor.") 
    # Insert a divider
    st.header("Welcome to my Portfolio!")

    st.markdown(
    """
    #### I recently started compiling my minimal `PORTFOLIO` to remind myself of what I can do or share to support the fields of Science and Technology. With this reminder, I can dedicate more energy to developing practical user guides in my areas of expertise to help anyone interested in what I do.
    
    #### Feel free to explore my passion in this portfolio. `KARIBU`:tada:
    """)
    st.write("---")
    
  with separator: 
    st.write("")
    
  with header2:
    st.markdown(
    """
    """)
    
with st.container():    
  st.write("##")
  st.title(":gift_heart:Professional Passion")
  header1, separator, header2 = st.columns((2, 0.3, 2))
  with header1:
    html_string1 = "<h3 style='color:#005500; font-size:24px;'>I am passionate about developing resources for finding insights into complex data using modern techniques. Also, I am interested in providing mentorship to interested individuals, particularly in the fields related to: </h3>"
    st.markdown(html_string1, unsafe_allow_html=True)
    
    html_string2 = "<ol> \
    	<li>Microbiome Data Analysis</li> \
    	<li>Machine Learning</li> \
    	<li>Multi-Omics Bioinformatics</li> \
    	<li>Text Mining & Summarization</li> \
    	<li>Quantitative Data Analysis</li> \
    	<li>Qualitative Data Analysis</li> \
    	<li>Data Tidying and Transformation</li> \
    	<li>Data Visualization</li> \
    	<li>Statistical Analysis</li> \
    	<li>Feature Engineering</li> \
    	<li>Model Selection and Training</li> \
    	<li>Hyperparameter Tuning</li> \
    	<li>Predictive Modeling</li> \
    	<li>Deployment of Simple Models</li> \
    	<li>Report Generation</li> \
    	<li>AOB Related to Data Insights</li> \
    </ol>"
    st.markdown(html_string2, unsafe_allow_html=True)
      
    with separator: 
        st.write("")

    with header2:
        st.success(
          """
          ## Did you know?
          ### Machine Learning & Microbiome
          ...are fields getting lots of attention recently. PubMed metrics can prove this theory!
          """)
        image = Image.open("figures/pubmed_search_bar_plot.png")
        st.image(image)
        st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
        # st.subheader("Creating a plot using `ggplot2`")
        with st.expander("Click to see or copy the R code"):
          st.code(pub_search_code, language="R")
    
    
# ---- WHAT I DO ----
with st.container():
    st.title("What I Currently Do")
    st.write("---")
    left_column, separator, right_column = st.columns((2, 0.5, 2))
    with left_column:
        st.write("##")
        st.write(
            """
            ### On my [GitHub account](https://github.com/tmbuza?tab=repositories):
              - I am developing multiple practical user guides for various analyses.
              - Most of these guides are under development in my private repositories and will be shared publicly once completed.
              - The intended audience is users who:
                  - ...are looking for friendly solutions to leverage their daily analytical tasks.
                  - ...are struggling to understand how to efficiently process raw data and transform it into actionable insights.
                  - ...are eager to learn more about going beyond traditional data analysis by integrating multiple compatible tools to achieve a more significant impact.
                  - ...are looking for better solutions to visualize the data and create shareable reports and dashboards.
                  - ...are looking for ways of transforming static images into interactive ones.
                  - ...are interested in developing and deploying simple data exploratory apps.
                  - ...are enthusiastic about developing skills to advance their career in Data Science, Machine Learning, or Bioinformatics.
           """)
        st.info(
            """
            If what I do sounds interesting to you, [get in touch](https://complexdatainsights.com/#contactus). Also, consider subscribing to my [website](https://complexdatainsights.com) (currently under active development) to benefit from the available DIY resources. Don\'t forget to turn on the notifications to receive updates.
            """)

    with separator:
        st.write("")


    with right_column:
        st.header("")
        st.write("##")
        st.image(fig1)
    
#######################################
# ----My Projects----
#######################################
with st.container():  
  st.title("Microbiome Bioinformatics Projects")
  st.write("---")

  column1, separator, column2 = st.columns((2, 0.5,  2)) 
  with column1:
    st.header("Microbial Profiling")
    st.image("https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/figures/stacked_bar_fig-.gif")
    st.caption("Simple example of Microbial relative abundance profiles at Taxon-level. This image show only the most abundant taxa and the remaining are in the other category.")
    
    st.header("Biomarker Discovery")    
    st.image("https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/figures/lefse_fig-1.png")
    st.caption("Simple example showing significant biomarkers identified using the Linear discriminant analysis Effect Size (LEfSe) based on the LDA scores")
    st.markdown("""
    """)
    
  with separator:
    st.write("")
    
  with column2:
    st.header(":fireworks:Achievements")
    st.success(
    """
      ### 1. Publications
      - [Paper 1](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2965-4): iMAP: an integrated bioinformatics and visualization pipeline for microbiome data analysis. 
        - See the current [iMAP manuscript dimensions](https://badge.dimensions.ai/details/id/pub.1117740326).
      - [Paper 2](https://www.nature.com/articles/s41598-019-53969-7): Microbial Diversity in Bushmeat Samples Recovered from the Serengeti Ecosystem in Tanzania.


      
      ### 2. GitHub Repositories
      
      |Repo| Description| Description|
      |-------------------------|---------------------------------------------------|-----------------|
      | iMAP | Original Pipeline linked to [iMAP manuscript](https://rdcu.be/bIxrg) | [GitHub Page](https://tmbuza.github.io/iMAP/) |
      > The original iMAP is being restructured and updated with more improved workflows. The updated version will replace the existing pipeline. Please consider this an ongoing process of finding better and integrated solutions for microbiome data analysis.
 

     
      ### :tada: Improved iMAP in Four-Tiers!
           

      > Investigating the role of microbial communities in health and disease requires a thorough knowledge of the entire analytical process.
      Using the wrong approaches can cost a significant amount of dollars and make a lengthy process to achieve the desired results.
      The Table below shows four iMAP practical user guides that systematically provide analytical support to the microbiome research community.
      Each guide is reproducible, allowing **R-users** to follow along easily.

      |Repo| Description| Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | [iMAP-PART1](https://github.com/tmbuza/iMAP-part1/) | How to Get Started with Microbiome Data Analysis | [eBook](https://complexdatainsights.com/books/microbiome-analysis/getting-started) |
      | [iMAP-PART2](https://github.com/tmbuza/iMAP-part2/) | Bioinformatics Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis) |
      | [iMAP-PART3](https://github.com/tmbuza/iMAP-part3/) | Data Preprocessing | [eBook](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing) |
      | [iMAP-PART4](https://github.com/tmbuza/iMAP-part4/) | Exploratory Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis) |



      ### 3. End-to-End Microbiome Analysis eBooks

    
      |eBook| Description| Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | SMDA | Systematic Microbiome Data Analysis (SMDA)...In progress.| [eBook 1](https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/) |
      """)
    
st.write("---")




#######################################
#######################################
#######################################
with st.container():
  st.write("---")
  st.header("Quantitative Data Analysis Projects")
  st.write("##")
  video_column, separator, text_column = st.columns((2, 0.5, 2))
  with video_column:
    st.info("Click the image below to see how \nthe temperature is changing stepwise from 1880 to 2022!")
    st.video(vid1)
    st.write(
      """
      I used a custom R script to generate the MP4.
      """)
    st.write(
      """
      ...Inspired by [`code club Youtube video tutorials`](https://riffomonas.org/code_club/) presented by Pat Schloss\'s.
      """)
    
  with separator:
    st.write("")
    
  with text_column:
    st.subheader("Reproducible Research")
    st.write(
      """
      **The climate data can be replaced with any quantitative or time series data to reproduce similar image.**
      
      - Get the same experience. I will be happy to provide you with a reproducible and easily customizable practical user guide. 
      - If you are interested in outsourcing or consulting services, I can help you get the results faster. 
      - You will also have the option to request a source code associated with the sought analysis. 
      """
      )
      # - Explore a variety of climate data visualization available [**here!**](https://complexdatainsights.com/books/climate-analysis/climate-viz.html#plotly-image)


# with st.container():
#   video_column, text_column = st.columns((1, 2))
#   with video_column:
#     st.info("Click the image below to see how \nthe static image was generated stepwise from 1880 to 2022!")
#     st.video(vid1)
#     st.write(
#       """
#      I used a custom R script to generate the MP4.
#       """)

#######################################
#######################################
#######################################
with st.container():
  st.write("---")
  st.title("Next Generation Sequence Exploration Projects")
  st.write("##")
  image_column, separator, output_column = st.columns((2, 0.5, 2))
  with image_column:
    st.image(fig2)
    st.caption("Example of a DNA sequence with colors representing different nucleotide; A, T, C, G. How many each of these nucleotides are in a FASTA sequence?")
    
    # with query_column:
    st.header("APP to Count Nucleotides")
    st.markdown(
    """
    This web app quickly computes the number of nucleotides present in a FASTA sequence.
    `Give it a try!`
    """
    )
    
    st.subheader('Enter query sequence in the box below')
    sequence_input = ">Partial sequence\nCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAGCACAGAGAGCTTGCTCTTGGGTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCCGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAACGTCTACGGACCAAAGT\GGGGGACCTTCGGGCCTCACACCATCGGATGTGCCCAGATGGGATTAGCTGGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGAT"
    
    sequence = st.text_area("Fasta sequence", sequence_input, height=250)
    sequence = sequence.splitlines()
    sequence = sequence[1:] # Skips the sequence name (first line)
    sequence = ''.join(sequence) # Concatenates list to string
    
    # with seq_column:
    ## Print the input DNA sequence
    st.subheader('DNA Query')
    sequence
    
    


# with st.container():
#   st.write("##")
#   text_column, figure_column = st.columns((1, 2))
#   
  with separator:
    st.write("")
  with output_column:
    st.subheader("App Output")
    
    def DNA_nucleotide_count(seq):
      d = dict([
                ('A',seq.count('A')),
                ('T',seq.count('T')),
                ('G',seq.count('G')),
                ('C',seq.count('C'))
                ])
      return d
    
    X = DNA_nucleotide_count(sequence)
    
    ### 1. Nucleotide Count
    st.subheader('1. Observation')
    st.write('There are  ' + str(X['A']) + ' adenine (A)')
    st.write('There are  ' + str(X['T']) + ' thymine (T)')
    st.write('There are  ' + str(X['G']) + ' guanine (G)')
    st.write('There are  ' + str(X['C']) + ' cytosine (C)')

    ### 2. Count Matrix
    st.subheader('2. DataFrame')
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'NT-Count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'Sequence'})
    st.write(df)
    
  # with figure_column:
    # st.header("Nucleotides Distribution")
    ### 3. Graphical Distribution
    st.subheader('3. Bar chart')
    p = alt.Chart(df).mark_bar().encode(
        x='Sequence',
        y='NT-Count'
    )
    p = p.properties(
        width=alt.Step(100)  # controls width of bar.
    )
    st.write(p)
    st.caption("Bar chart showing the number of nucleotide composition in a given DNA sequence.")
  
  ### Save data frame locally
  df.to_csv("data/gene_seq1.csv")



st.write("##")
st.write("##")
with st.container():
  st.write("---")
  st.header("Get In Touch")
  st.write(
    """
    - Let's collaborate and work together in this world of Data Science and many more...
    - Together we can transform complex data into **ACTIONABLE INSIGHTS**.
    - Feel free to contact me by filling out the form below to let me know if we need to collaborate or need a mentor in specific fields of my expertise.
    """)
  
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

