#######################################
# ----Tools and Page setup----
#######################################
import json
import requests
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/. Select an Object including the two :: eg :tada: or :trophy: 
st.set_page_config(page_title="TMB Portfolio", page_icon=":sparkles:", layout = "wide")


def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

# Use local CSS
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#######################################
# ----Assets----
#######################################
lottie_coding = "https://iconscout.com/lottie/data-analysis-4876889"
lottie_coding = "https://iconscout.com/lottie/data-analysis-3647751"
lottie_coding = "https://iconscout.com/lottie/data-analysis-4179002"

from PIL import Image
# For Professional Passion
omics_ml = Image.open("imgvideo/omics_ml.png")
# wcloud1 = Image.open("imgvideo/wordcloud.png")
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
  header1, header2 = st.columns((2, 1))
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
  with header2:
    st.markdown(
    """
    """)
    
with st.container():    
  st.write("##")
  # st.title("Professional Passion") 
  header1, header2 = st.columns((1, 2))
  with header1:
    html_string1 = "<h1>Professional Passion</h1><h3 style='color:#007755; font-size:24px;'>I am passionate about developing resources for finding insights into complex data using modern techniques. Also, I am interested in providing mentorship to interested individuals, particularly in the fields related to: </h3>"
    st.markdown(html_string1, unsafe_allow_html=True)
    
    html_string2 = "<ol> \
    	<li><h4>Microbiome Data Analysis</h4></li> \
    	<li><h4>Machine Learning</h4></li> \
    	<li><h4>Multi-Omics Bioinformatics</h4></li> \
    	<li><h4>Quantitative Data Analysis</h4></li> \
    	<li><h4>Qualitative Data Analysis</h4></li> \
    	<li>Data Tidying and Transformation</li> \
    	<li>Data Visualization</li> \
    	<li>Statistical Analysis</li> \
    	<li>Feature Engineering</li> \
    	<li>Model Selection and Training</li> \
    	<li>Hyperparameter Tuning</li> \
    	<li>Predictive Modeling</li> \
    	<li>Deployment of Simple Models</li> \
    	<li>AOB Related to Data Insights</li> \
    </ol>"
    st.markdown(html_string2, unsafe_allow_html=True)
  
  with header2:
    st.write("##")
    st.success(
      """
      ## Did you know?
      ### Machine Learning & Microbiome
      are fields getting lots of attention recently. PubMed is the Proof!
      """)
    st.image(omics_ml)
    st.write("##")
  st.write("---")
    
    
with st.container():

  st.title("Practical User Guides in Pipeline")
  st.markdown(
    """
    On my [GitHub](https://github.com/tmbuza?tab=repositories), I am developing multiple practical user guides for various analyses. These guides intend to help users who:
      
    - ...are looking for friendly solutions to leverage their daily analytical tasks.
    - ...are struggling to understand how to efficiently process raw data and transform it into actionable insights.
    - ...are eager to learn more about going beyond traditional data analysis by integrating multiple compatible tools to achieve a more significant impact.
    - ...are looking for better solutions to visualize the data and create shareable reports in HTML, PDF, Word format, and dashboard using R-Markdown.
    - ...are looking for ways of transforming static images into interactive ones.
    """)

  st.write("---")


    
#######################################
# ----My Projects----
#######################################
with st.container():  
  st.title("Bioinformatics Projects")
  st.write("---")

  column1, column2 = st.columns((1, 2)) 
  with column1:
    st.header("Microbiome Projects")
    st.image("https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/figures/stacked_bar_fig-.gif")
    st.caption("Example of Microbial abundance profiles at Taxon-level. This image show only the most abundant taxa and the remaining are in the other category.")
    
    st.image("https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/figures/lefse_fig-1.png")
    st.caption("Minimal example showing significant biomarkers identified using the Linear discriminant analysis Effect Size (LEfSe)  based on the LDA scores")
    st.markdown("""
    """)
      
  with column2:
    st.header(":fireworks:Achievements")
    st.markdown(
      """
      ### 1. Publications
      - [Paper 1](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2965-4): iMAP: an integrated bioinformatics and visualization pipeline for microbiome data analysis. 
        - See the current [iMAP manuscript dimensions](https://badge.dimensions.ai/details/id/pub.1117740326)
      - [Paper 2](https://www.nature.com/articles/s41598-019-53969-7): Microbial Diversity in Bushmeat Samples Recovered from the Serengeti Ecosystem in Tanzania.
      - [eBook 1](https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/): Systematic Microbiome Data Analysis (SMDA)...In progress.
      """)
          
    st.write("##")
    st.markdown(
      """
      ### 2. GitHub Repositories
      
      |Repo| Description| Description|
      |-------------------------|---------------------------------------------------|-----------------|
      | iMAP | Integrated Microbiome Analysis Pipeline | [GitHub Page](https://tmbuza.github.io/iMAP/) |
      ||||
      
      """)
      
    st.write("##")
    st.markdown(
      """
      ### 3. Microbiome Analysis eBooks
      """)
    st.success("Investigating the role of microbial communities in health and disease requires a thorough knowledge of the entire analytical process. \
    Using the wrong approaches can cost a significant amount of dollars and make a lengthy process to achieve the desired results.\
    The Table below shows four iMAP practical user guides that systematically provide analytical support to the microbiome research community. \
    Each guide is reproducible, allowing **R-users** to follow along easily.")

    st.markdown(
      """   
    |Repo| Description| Repo Output|
    |-------------------------|---------------------------------------------------|-----------------|      
    | iMAP-PART1 | How to Get Started with Microbiome Data Analysis | [eBook](https://complexdatainsights.com/books/microbiome-analysis/getting-started) |
    | iMAP-PART2 | Bioinformatics Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis) |
    | iMAP-PART3 | Data Preprocessing | [eBook](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing) |
    | iMAP-PART4 | Exploratory Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis) |
    """)
    st.write("---")




#######################################
#######################################
#######################################
with st.container():
  st.write("---")
  st.header("Quantitative Data Analysis")
  st.write("##")
  image_column, text_column = st.columns((1, 2))
  with image_column:
   st.image(fig1)
   st.write("""
   ...Inspired by [`code club Youtube video tutorials`](https://riffomonas.org/code_club/) presented by Pat Schloss\'s Lab at the University of Mic.
   """)
  with text_column:
    st.subheader("Climate Data")
    st.write(
      """
      - Get the same experience. I will be happy to provide you with a reproducible and easily customizable practical user guide. 
      - If you are interested in outsourcing or consulting services, I can help you get the results faster. 
      - You will also have the option to request a source code associated with the sought analysis. 
      - Explore a variety of climate data visualization available [**here!**](https://complexdatainsights.com/books/climate-analysis/climate-viz.html#plotly-image)
      """
      )

with st.container():
  video_column, text_column = st.columns((1, 2))
  with video_column:
    st.info("Click the image below to see how \nthe static image was generated stepwise from 1880 to 2022!")
    st.video(vid1)
    st.write(
      """
     I used a custom R script to generate the MP4.
      """)

#######################################
#######################################
#######################################
with st.container():
  st.write("---")
  st.write("---")
  st.header("NGS: Next Generation Sequence Analysis")
  st.write("##")
  image_column, text_column = st.columns((1, 2))
  with image_column:
   st.image(fig2)
   st.caption("A DNA sequence with colors representing different nucleotide; A, T, C, G.")

  with text_column:
    st.title("APP to Count Nucleotides")
    st.markdown(
      """
      This web app quickly computes the number of nucleotides present in a given DNA sequence. 
      
      `Give it a try!`
      """
    )
    st.write("##")
    st.subheader('Enter query sequence in the box below')
    sequence_input = ">LC557153.1 Erwinia amylovora Eaap3-1 gene for 16S rRNA, partial sequence\nCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAGCACAGAGAGCTTGCTCTTGG \
  GTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCCGATGGAGGGGGATAACTACTGGAAACG \
  GTAGCTAATACCGCATAACGTCTACGGACCAAAGTGGGGGACCTTCGGGCCTCACACCATCGGATGTGCC \
  CAGATGGGATTAGCTGGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGAT"

    #sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
    sequence = st.text_area("Fasta sequence with header in line 1", sequence_input, height=250)
    sequence = sequence.splitlines()
    sequence = sequence[1:] # Skips the sequence name (first line)
    sequence = ''.join(sequence) # Concatenates list to string
    
    
    ## Prints the input DNA sequence
    st.subheader('DNA Query')
    sequence




with st.container():
  st.write("##")
  text_column, figure_column = st.columns((1, 2))
  
  with text_column:
    st.header("Nucleotides Count")
    
    # ### 1. Output
    # st.subheader('1. Total nucleotide count')
    def DNA_nucleotide_count(seq):
      d = dict([
                ('A',seq.count('A')),
                ('T',seq.count('T')),
                ('G',seq.count('G')),
                ('C',seq.count('C'))
                ])
      return d
    
    X = DNA_nucleotide_count(sequence)
    #X
    
    ### 1. Observation
    st.subheader('1. Observation')
    st.write('There are  ' + str(X['A']) + ' adenine (A)')
    st.write('There are  ' + str(X['T']) + ' thymine (T)')
    st.write('There are  ' + str(X['G']) + ' guanine (G)')
    st.write('There are  ' + str(X['C']) + ' cytosine (C)')
    

    ### 2. DataFrame
    st.subheader('2. DataFrame')
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'nt_count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'gene1'})
    st.write(df)
    
  with figure_column:
    st.header("Nucleotides Distribution")
    ### 3. Bar chart
    st.subheader('3. Bar chart')
    p = alt.Chart(df).mark_bar().encode(
        x='gene1',
        y='nt_count'
    )
    p = p.properties(
        width=alt.Step(100)  # controls width of bar.
    )
    st.write(p)
    st.caption("Bar chart showing the number of nucleotide composition in a given DNA sequence.")
  
  ### Save data frame locally
  df.to_csv("data/gene_seq1.csv")




with st.container():
  st.write("---")
  st.header("Get In Touch")
  st.write("##")
  
  # Contact Documentation: https://formsubmit.co/ Change the email address
  contact_form = """
  <form action="HTTPS://formsubmit.co/ndelly@gmail.com" method="POST">
  # <form action="HTTPS://formsubmit.co/7cdcf796dc9b14d3ac7f61c897996979" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
  </form>
  """
  
  left_column, right_column = st.columns(2)
  with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
  with right_column:
    st.empty()


##################################
st.balloons()
##################################
