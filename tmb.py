#######################################
# ----Tools and Page setup----
#######################################
import os
import stat
import time
import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt
from PIL import Image
import subprocess
import sys
import custom # This is a local file containing custom dictionaries
from custom import pub_search_code, project_header, date_updated
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
import plotnine
from plotnine.data import diamonds


# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/. 
# st.set_page_config(page_title="TMB Portfolio", page_icon=":sparkles:", layout = "wide")
st.set_page_config(
  page_title="TMB Portfolio", 
  page_icon=":outbox_tray:",
  layout = "wide")
  # layout = "centered")

# DICTIONARIES
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.markdown(
  """ 
  <style>
  footer {visibility: hidden;}
  </style> 
  """, 
  unsafe_allow_html=True)

def project_header():
  st.markdown(
    """
    <header style= 'background-color: #008080'; color: 'white';>
    <h1 
    style='
      text-align: center;
      color: white; 
      font-size: 3em; 
      '>
      TMB Professional Portfolio
    </h1>
    <!-- <logo><center>
      <a href='https://complexdatainsights.com'>
      <img src='https://complexdatainsights.com/wp-content/uploads/2022/10/logo_white.png' 
        alt=' page cover'
        width='35%' 
        style='padding: 10px; 
        float: center;'/></a>
      </center></logo> -->
    </header>
    
    """, unsafe_allow_html=True)
#------------------------------
# ----Assets----
#------------------------------

# Passion section
pubstats = Image.open("figures/pubmed_search_line_plot.png")

# Image objects: Use Image.open("")
wdcloud1 = Image.open("img/wordcloud.png")
gwas = Image.open("imgvideo/gwas_in_biome.png")
temp1 = Image.open("imgvideo/climate_nasa.png")
dna = Image.open("imgvideo/dna_composition.png")
# prot_align = Image.open("imgvideo/prot_align.png")

# GIF objects: Use open("")
abundgif1 = open("imgvideo/abund_bar.gif")

# Video objects: Use open("", "rb").read()
tempmp4 = open("imgvideo/climate_spiral_nasa.mp4", "rb").read()

contact_form = """
<form action="https://formsubmit.co/ndelly@gmail.com" class="contact-form" method="POST">
  <input type="text" required placeholder="Your Name" required>
  <input type="email" name="email" placeholder="Your email" required>
  <input type="text" required placeholder="Enter Subject" required>
  <textarea name="message" id="" cols="15" rows="6" placeholder="Enter Your Message Here..." required></textarea>
  <button type="submit">Submit</button>
</form>  
""" 

resume = """
<a href="https://complexdatainsights.com/cv-resumes/Teresia-Mrema-Buza_resume_20221006.pdf" class="main-btn">
  <span class="btn-text"><h4><center>View my Resume</center></h4></span>
</a>
""" 

#######################################
# ---- Header with salutation and introduction----

date_updated('./tmb.py')

if project_header():
  project_header()

st.write("##")
st.write("##")

#######################################
with st.container(): 

  st.subheader("Hi, I am Teresia Mrema Buza (TMB):wave:")
  left, right = st.columns((2, 1))
  with left:
    st.title("A Data Science, Microbiome, Machine learning, Bioinformatics, and Computational Biology Enthusiast, Consultant, and Mentor.") 
st.write("---")
  
with st.container():
  header1, separator, header2 = st.columns((2, 0.2, 1.5))
  with header1:
    st.header("Welcome to my Portfolio!")
    st.markdown(
    """
    #### My minimal Portfolio displays areas of my expertise, accomplishment and work in-progress.
    """)
    
    st.write("##")
    
    st.success("""
    ## My Passion
    - Briefly, I am passionate about **finding insights into complex data** using integrated approaches.
    - My prime interest is to dedicate more energy in developing __open-source user guides__ to support diverse communities dealing with simple to complex data.
    - I am also interested in providing Consultanting Services and Mentorship in selected areas, including: 
      - Microbiome Bioinformatics
      - Machine Learning
      - Quantitative and Qualitative Data Analysis
      - Data Visualization
      - Web Applications
      - AOB as Requested...

    """)
    
    st.success("""
    ### Additionally, I routinely work with different data types to perform: 
      - Data Tidying, Transformation & Analysis
      - Quantitative Data Analysis
      - Qualitative Data Analysis
      - Statistical Data Analysis
      - Static Data Visualization
      - Interactive Data Visualization
      - AOB Related to Data Insights
    """)
    st.markdown(
      """
      #### [View my Partial Resume](https://complexdatainsights.com/cv-resumes/Teresia-Mrema-Buza_resume_20221004.pdf)
      """)
      
    st.write(
      """
      #### Feel free to explore the entire portfolio. `KARIBU SANA!`:tada:      
      """)

  with header2:
    st.write("##")
    st.image(wdcloud1, width=550)

    st.write("##")
    st.write("##")
    st.info(
    """
    #### Did you know? Microbiome & Machine Learning
    ...are the top fields getting lots of attention recently.
    """)
    
    st.image(pubstats, width=600)
    st.caption("""**The publication trend in PubMed**. This line chart was created using an `R script`, then imported into this web app generated 
    using `Python` and `streamlit` library. Integration of different tools demonstrates robust solutions 
    for gaining insights into complex data.""")
    with st.expander("View Partial R code"):
      st.code(pub_search_code, language="R")

    st.markdown("""Source: [TMB Github repo](https://github.com/tmbuza/pubmed-article-stats/blob/main/02_plot_article_count.Rmd)""")
        
st.write("---")  


# ---- WHAT I DO ----
with st.container():
    st.write(
      """
      # What I Do
      """)
      
    left_column, separator, right_column = st.columns((2, 0.5, 2))
    with left_column:
        st.write("##")
        st.write(
          """
          ### On my `personal` [GitHub accounts](https://github.com/tmbuza/):
          
          """)
        
        st.info(
          """
            - I develop DIY practical user guides that provides integrated diverse analysis solutions for better results.
            - Most of these guides are in progress and I will share publicly once completed.
            - The intended audience is:
                - ... researchers who need reproducible tools to analyze data for their manuscripts, theses, dissertations, or presentations.
                - ... academic members who need reproducible workflows for teaching and training purposes.
                - ... users looking for friendly solutions to leverage their daily analytical tasks.
                - ... users who struggle to understand how to efficiently process raw data and transform it into actionable insights.
                - ... users eager to learn more about going beyond traditional data analysis by integrating multiple compatible tools to achieve a more significant impact.
                - ... users looking for better solutions for visualizing the data and creating shareable reports and dashboards.
                - ... users interested in developing and deploying simple data-related web apps.
                - ... users enthusiastic about developing skills to advance their career in Data Science, Machine Learning, or Bioinformatics.
         """)
           
    with right_column:
      st.write("##")
      # st.image(wdcloud1, width=300)
      # st.image("https://complexdatainsights.com/wp-content/uploads/2022/08/cdifrontimg-1-e1660417963487.png", width=300)
      # st.image("https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/figures/lefse_fig-1.png")
      # st.image("https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/figures/lefse_fig-1.png")
      # st.caption("Simple example showing significant biomarkers identified using the Linear discriminant analysis Effect Size (LEfSe) based on the LDA scores")
      st.subheader("Let's Collaborate!")
      st.info(
        """
        We can collaborate at many levels if what I do interests you. 
        Feel free to contact me by filling out the contact form at the end of this page to let me know if we need to collaborate or need a mentor in specific fields.
        """)
      
      st.subheader("Outsource or DIY ")
      st.info(
        """
        Outsourcing can increase efficiency and save time. Feel free to contact me by filling out the contact form at the end of this page to discuss the logistics.

        """)   
        
      st.subheader("Subscribe for Updates")
      st.info(
        """
        Consider subscribing to my [website](https://complexdatainsights.com) (currently 
        under construction) to benefit from the available DIY resources. 
        """) 
        
st.write("##")
st.markdown("<h1 style='text-align: center; color: white; font-size: 2.5em; background-color: #008080'>Achievements and Projects in Progress</h1>", unsafe_allow_html=True)
st.write("##")

with st.container():
  st.success(
    """
    # Microbiome Bioinformatics
    """)
#######################################
with st.container():
  st.write("##")
  column1, separator, column2 = st.columns((1, 0.5,  2.5)) 
  with column1:
    # st.header("Microbial profiling")
    st.info("""
    Investigating the role of microbial communities in health and disease requires a thorough knowledge of the entire 
    analytical process. Using the wrong approaches can cost a significant amount of dollars and make a lengthy process 
    to achieve the desired results.
    """)
    st.image("https://complexdatainsights.com/wp-content/uploads/2022/09/bookcover.png")
    st.caption("In progress: Systematic Microbiome Data Analysis in R. This eBook provides an end-to-end practical user guide \
    for analyzing microbiome data. It comprises iMAP-Part 1, 2, 3, & 4 described in the next section")

  with column2:
    st.write(
    """
      ### 1. Publications
      - [Paper 1](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2965-4): iMAP: an integrated bioinformatics and visualization pipeline for microbiome data analysis. 
        - See the current [iMAP manuscript dimensions](https://badge.dimensions.ai/details/id/pub.1117740326).
      - [Paper 2](https://www.nature.com/articles/s41598-019-53969-7): Microbial Diversity in Bushmeat Samples Recovered from the Serengeti Ecosystem in Tanzania.


      
      ### 2. GitHub Repositories
      
      |Repo| Description| Description|
      |-------------------------|---------------------------------------------------|-----------------|
      | [iMAP](https://github.com/tmbuza/iMAP/) | Original Pipeline linked to [iMAP manuscript](https://rdcu.be/bIxrg) | [GitHub Page](https://tmbuza.github.io/iMAP/) |
      """)
      
    st.info("""
      The original iMAP is being restructured and updated with more improved workflows. The updated version will replace the existing pipeline. Please consider this an ongoing process of finding better and integrated solutions for microbiome data analysis.
      """)

    st.write("""
      ### Improved iMAP in Four-Tiers!
      The Table below shows four iMAP practical user guides that systematically provide analytical support to the microbiome research community.
      Each guide is reproducible, allowing **R-users** to follow along easily.

      |Repo| Description| :books:Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | [iMAP-PART1](https://github.com/tmbuza/iMAP-part1/) | How to Get Started with Microbiome Data Analysis | [eBook](https://complexdatainsights.com/books/microbiome-analysis/getting-started) |
      | [iMAP-PART2](https://github.com/tmbuza/iMAP-part2/) | Bioinformatics Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis) |
      | [iMAP-PART3](https://github.com/tmbuza/iMAP-part3/) | Data Preprocessing | [eBook](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing) |
      | [iMAP-PART4](https://github.com/tmbuza/iMAP-part4/) | Exploratory Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis) |
      """)

    st.write("##")
    st.write("""
      ### 3. End-to-End Microbiome Analysis eBooks

    
      |Repo| Description| :books:Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | SMDA | Systematic Microbiome Data Analysis (SMDA)...In progress.| [eBook 1](https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/) |
      """)
    
st.write("---")




#######################################
def ml_apps():
  with st.container():
    st.write("##")
    st.success(
    """
    # Machine Learning
    """)
  with st.container():
    st.write("##")
    column1, separator, column2 = st.columns((1, 0.5,  2.5)) 
    with column1:
      st.write("...In Progress...")
    with column2:
      st.write(
        """
        |Repo| Description| Web App|
        |-------------------------|---------------------------------------------------|-----------------|
        | [eda-ml-app](https://github.com/tmbuza/eda-ml-app) | Basic data exploration for Machine Learning Models | https://tmbuza-eda-ml-app-app1-tns9rv.streamlitapp.com/ |
        # | [eda-ml-app](https://github.com/tmbuza/eda-ml-app) | Data Preprocessing for Machine Learning Models | https://tmbuza-eda-ml-app-app1-tns9rv.streamlitapp.com/ |
        # | [eda-ml-app](https://github.com/tmbuza/eda-ml-app) | Data Preprocessing for Machine Learning Models | https://tmbuza-eda-ml-app-app1-tns9rv.streamlitapp.com/ |
  
        """)
    
      st.write("---")

# if ml_count():
#   ml_count()

def quantitative():  
  with st.container():
    st.write("##")
    st.success(
    """
    # Quantitative Data Analysis
    """)
  with st.container():
    st.write("##")
    column1, separator, column2 = st.columns((1, 0.5,  2.5)) 
    with column1:
      st.write("...In Progress...")
    with column2:
      st.write(
        """
        |Repo| Description| Repo Output|
        |-------------------------|---------------------------------------------------|-----------------|
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
    
        """)
    
      st.write("---")
    
# if quantitative():
#   quantitative()  

def qualitative():  
  with st.container():
    st.write("##")
    st.success(
    """
    # Qualitative Data Analysis
    """)
  with st.container():
    st.write("##")
    column1, separator, column2 = st.columns((1, 0.5,  2.5)) 
    with column1:
      st.write("...In Progress...")
    with column2:
      st.write(
        """
        |Repo| Description| Repo Output|
        |-------------------------|---------------------------------------------------|-----------------|
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
        | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) |
    
        """)
    
      st.write("---")
    
# if qualitative():
#   qualitative()
#---------------------------------------------

with st.container():
  def nt_count():
    st.write("##")
    st.success(
      """
      # Next Generation Sequencing
      """)
    st.header("1. Nucleotide Count App")
  
  # with st.container(): 
  #   st.write("##")
  #   st.markdown("<h1 style='text-align: left; color: #000000;'>Web Applications</h1>", unsafe_allow_html=True)
  
    panel1, separator1, panel2, separator2, panel3, separator3, panel4 = st.columns((1, 0.2, 1.5, 0.2, 1, 0.2, 1.5))
    with panel1:
      st.image(dna)
      st.caption("Example of a DNA sequence with colors representing different nucleotide; A, T, C, G. How many each of these nucleotides are in a FASTA sequence?")
      
    with panel2:
      st.write(
        """
        #### NT Count APP
        """)
      st.markdown(
      """
      This web app computes the number of nucleotides present in a FASTA sequence.\n
      `Test the App by replacing the default DNA fasta sequence in the text area!`
      """
      )
  
      dna_query = ">Sequence1\nCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAGCACAGAGAGCTTGCTCTTGGGTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCCGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAACGTCTACGGACCAAAGT\GGGGGACCTTCGGGCCTCACACCATCGGATGTGCCCAGATGGGATTAGCTGGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGAT"
      
      sequence = st.text_area("Enter a DNA Fasta Sequence", dna_query, height=150)
      sequence = sequence.splitlines()
      sequence = sequence[1:] # Skips the sequence name (first line)
      sequence = ''.join(sequence) # Concatenates list to string
      
      st.text_area("Clean Query Sequence", sequence, height=150)
      
  
    with panel3:
      st.write(
        """
        #### NT Count Output
        """)
      
      def DNA_nucleotide_count(seq):
        d = dict([
                  ('A',seq.count('A')),
                  ('T',seq.count('T')),
                  ('G',seq.count('G')),
                  ('C',seq.count('C'))
                  ])
        return d
      
      nt_count = DNA_nucleotide_count(sequence)
      df = pd.DataFrame.from_dict(nt_count, orient='index')
      df = df.rename({0: 'Count'}, axis='columns')
      df.reset_index(inplace=True)
      df = df.rename(columns = {'index':'NT'})
      st.write(df)
      
    with panel4:
      st.write(
        """
        #### NT Count Bar Chart
        """)
        
      p = alt.Chart(df).mark_bar().encode(
          x='NT',
          y='Count'
      )
      p = p.properties(
          width=alt.Step(25)  # controls width of bar.
      )
      st.write(p)
      st.caption("Bar chart showing the number of nucleotide composition in a given DNA FASTA sequence.")
    
# if nt_count():
#   nt_count()

#---------------------------------------------

with st.container():
  def aa_count():
    st.header("Amino Acid Count App")
    panel1, separator1, panel2, separator2, panel3, separator3, panel4 = st.columns((1, 0.2, 1.5, 0.2, 1, 0.2, 1.5))
    # panel1, separator1, panel2 = st.columns((1, 0.2, 2))
    with panel1:
      st.image("https://complexdatainsights.com/wp-content/uploads/2022/09/aligments.png")
      # st.image("https://complexdatainsights.com/wp-content/uploads/2022/09/amino_acid_abbr.png", width=250)
      st.caption("A typical protein sequence contains 20 unique amino acids represented with single or three letter code. What is the composition of each amino acid?")
      
      st.subheader("The 20 Amino Acid Code")
      df = pd.read_csv('data/aa.csv')
      st.dataframe(df)
  
    with panel2:
      st.write(""" #### AA Count APP""")
      st.markdown(
      """
      This web app interactively computes the number of amino acids in a protein FASTA sequence.\n
      `Test the App by replacing the default protein fasta sequence in the text area!`
      """
      )
      aa_query = ">QRG27454.1 hemagglutinin, Influenza A virus\n \
  MKTIIALSYILCLVFAQKIPGNDNSTATLCLGHHAVPNGTIVKTITNDRIEVTNATELVQNSSIGEICDS \
  PHQILDGENCTLIDALLGDPQCDGFQNKKWDLFVERSKAYSNCYPYDVPDYASLRSLVASSGTLEFNNES \
  FNWTGVKQNGTSSACIRKSSSSFFSRLNWLTHLNYTYPALNVTMPNNEQFDKLYIWGVHHPGTDKDQIFL \
  YAQSSGRITVSTKRSQQAVIPNIGSRPRIRDIPSRISIYWTIVKPGDILLINSTGNLIAPRGYFKIQSGK \
  SSIMRSDAPIGKCKSECITPNGSIPNDKPFQNVNRITYGACPRYVKHSTLKLATGMRNVPEKQTRGIFGA \
  IAGFIENGWEGMVDGWYGFRHQNSEGRGQAADLKSTQAAIDQINGKLNRLIGKTNEKFHQIEKEFSEVEG \
  RIQDLEKYVEDTKIDLWSYNAELLVALENQHTIDLTDSEMNKLFEKTKKQLRENAEDMGNGCFKIYHKCD \
  NACIGSIRNGTYDHHVYRDEALNNRFQIKGVELKSGYKDWILWISFAISCFLLCVALLGFIMWACQKGNI \
  RCNICI"
  
      # aa_query = ""
      sequence = st.text_area("Enter a Protein Fasta Sequence", aa_query, height=150)
      sequence = sequence.splitlines()
      sequence = sequence[1:] # Skips the sequence name (first line)
      sequence = ''.join(sequence) # Concatenates list to string
      
      st.text_area("Clean Query Sequence", sequence, height=150)
      
    # panel3, separator1, panel4 = st.columns((1, 0.2, 2))
    with panel3:
      st.write(
        """
        #### AA Count Output
        """)
      
      def aa_count(seq):
        aa = dict([
                  ('A',seq.count('A')),
                  ('R',seq.count('R')),
                  ('N',seq.count('N')),
                  ('D',seq.count('D')),
                  ('C',seq.count('C')),
                  ('E',seq.count('E')),
                  ('Q',seq.count('Q')),
                  ('G',seq.count('G')),
                  ('H',seq.count('H')),
                  ('I',seq.count('I')),
                  ('L',seq.count('L')),
                  ('K',seq.count('K')),
                  ('M',seq.count('M')),
                  ('F',seq.count('F')),
                  ('P',seq.count('P')),
                  ('S',seq.count('S')),
                  ('T',seq.count('T')),
                  ('W',seq.count('W')),
                  ('Y',seq.count('Y')),
                  ('V',seq.count('V'))
                  ])
        return aa
      
      aa_count = aa_count(sequence)
      df = pd.DataFrame.from_dict(aa_count, orient='index')
      df = df.rename({0: 'Count'}, axis='columns')
      df.reset_index(inplace=True)
      df = df.rename(columns = {'index':'AA'})
      st.write(df)
      
    with panel4:
      st.write(
        """
        #### AA Count Bar Chart
        """)
        
      p = alt.Chart(df).mark_bar().encode(
          x='AA',
          y='Count'
      )
      p = p.properties(
          width=alt.Step(20)  # controls width of bar.
      )
      st.write(p)

# if aa_count():
#   aa_count()
#---------------------------------------------
# 
# def eda_1_app():
#   with st.container():
#     st.success(
#       """
#       # Exploratory Data Analysis App
#       """)
#     panel1, separator1, panel2, separator2, panel3 = st.columns((2, 0.2, 2, 0.2, 2))
#     with panel1:
#       st.markdown(
#         """
#         ### Simple EDA App:
#         - Reads the `data` uploaded by user and automatically starts exploration.
#         - Displays the `head` and `tail` of the uploaded data (input dataframe).
#         - Shows the dataframe `dimension`, `variable names` and `missing values`.
#         - Perform `descriptive` statistical analysis of the numerical variables.
#         - Plots a `correlation` heatmap.
#         """)
#         
#     with panel2:
#       st.write("""
#         ### Getting started""")
#       st.markdown(
#         """
#         - Upload input file using the provided user\'s widget. 
#         - Make sure that the uploaded data is tidy.
#         - You may start by testing the app using a demo data.
#         - To test the app click on the `Test EDA App` button.
#         """)
#       
#       # if st.button('Test EDA App'):
#       #   # Using a demo data
#       #   @st.cache
#       #   def load_data():
#       #       a = pd.read_csv('data/preprocessed_diamonds.csv')
#       #       return a
#       # 
#       #   df = load_data()
#       #   st.write(""" > This demo uses a preprocessed `diamond dataset` for demonstration only.""")
#       #   st.header("""Demo Data Exploration""")
#       #   st.subheader("""Input DataFrame""")
#       #   st.write("Head", df.head())
#       #   st.write("Tail", df.tail())
#       # 
#       #   st.subheader("""Dataframe dimension""")
#       #   st.markdown("> Note that 0 = rows, and 1 = columns")
#       #   st.dataframe(df.shape)
#       # 
#       #   st.subheader("""Variable names""")
#       #   st.dataframe(pd.DataFrame({'Variable': df.columns}))
#       #   
#       #   st.subheader("""Missing values""")
#       #   missing_count = df.isnull().sum()
#       #   value_count = df.isnull().count() #denominator
#       #   missing_percentage = round(missing_count/value_count*100, 2)
#       #   missing_df = pd.DataFrame({'Count': missing_count, 'Missing (%)': missing_percentage})
#       #   st.dataframe(missing_df)
#       # 
#       #   st.subheader("""Descriptive statistics""")
#       #   st.dataframe(df.describe())
#       # 
#       #   st.subheader("""Correlation heatmap""")    
#       #   fig, ax = plt.subplots()
#       #   sns.heatmap(df.corr(), ax = ax)
#       #   st.write(fig, use_container_width=False) 
#       # 
#       with panel3: 
#         st.write("""
#           ### User input widget""")
#         st.markdown(
#           """ """)
#         uploaded_file = st.file_uploader("Please choose a CSV file", type=["csv"])
#         if uploaded_file is not None:    
#           def load_data():
#               a = pd.read_csv(uploaded_file)
#               return a
#           df = load_data()
#           st.header("""Data Exploration""")
#           st.subheader("""Input DataFrame""")
#           st.write("Head", df.head())
#           st.write("Tail", df.tail())
#       
#           st.subheader("""Dataframe dimension""")
#           st.markdown("> Note that 0 = rows, and 1 = columns")
#           st.dataframe(df.shape)
#       
#           st.subheader("""Variable names""")
#           st.dataframe(pd.DataFrame({'Variable': df.columns}))
#           
#           st.subheader("""Missing values""")
#           missing_count = df.isnull().sum()
#           value_count = df.isnull().count() #denominator
#           missing_percentage = round(missing_count/value_count*100, 2)
#           missing_df = pd.DataFrame({'Count': missing_count, 'Missing (%)': missing_percentage})
#           st.dataframe(missing_df)
#       
#           st.header("""Basic Statistics""")    
#           st.subheader("""Descriptive statistics""")
#           st.dataframe(df.describe())
#       
#           st.subheader("""Correlation heatmap""")    
#           fig, ax = plt.subplots()
#           sns.heatmap(df.corr(), ax = ax)
#           st.write(fig, use_container_width=False) 
#         else:
#           st.warning(':exclamation: Awaiting user\'s input file')
# 
# # if eda_1_app():
# #   eda_1_app()

with st.container():
  st.success(
    """
    # Data Visualizations
    """)
with st.container():
  st.write("##")
  st.write("""### Interactive with Plotly """)

  uploaded_file = st.file_uploader("Please choose a CSV file", type=["csv"])
  if uploaded_file is not None:    
    def load_data():
        a = pd.read_csv(uploaded_file)
        return a
    df = load_data()
    st.header("""Data Exploration""")
    st.subheader("""Input DataFrame""")
    st.write("Head", df.head())
    st.write("Tail", df.tail())

    st.subheader("""Dataframe dimension""")
    st.markdown("> Note that 0 = rows, and 1 = columns")
    st.dataframe(df.shape)

    st.subheader("""Variable names""")
    st.dataframe(pd.DataFrame({'Variable': df.columns}))
    
    st.subheader("""Missing values""")
    missing_count = df.isnull().sum()
    value_count = df.isnull().count() #denominator
    missing_percentage = round(missing_count/value_count*100, 2)
    missing_df = pd.DataFrame({'Count': missing_count, 'Missing (%)': missing_percentage})
    st.dataframe(missing_df)

    st.header("""Basic Statistics""")    
    st.subheader("""Descriptive statistics""")
    st.dataframe(df.describe())

    col1, col2, separator, col3, corr = st.columns((0.5, 0.5, 0.2, 2, 2))
    
    x_axis_val = col1.selectbox('Select data for the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select data for the Y-axis', options=df.columns)
    
    with corr:
      st.write("""Correlation heatmap""")    
      fig, ax = plt.subplots()
      sns.heatmap(df.corr(), ax = ax)
      st.write(fig, use_container_width=False) 
    
    with col3:
      st.write("""Scatter charts""")      
      plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
      st.plotly_chart(plot, use_container_width=True)
    
    col4, col5, col6, col7 = st.columns(4)
    
    with col4:
      st.write("""Line charts""")
      st.line_chart(df, x=x_axis_val, y=y_axis_val)
    with col5:
      st.write("""Bar charts""")
      st.bar_chart(df, x=x_axis_val, y=y_axis_val)
    with col6:
      st.write("""Area charts""")
      st.area_chart(df, x=x_axis_val, y=y_axis_val)
    with col7:      
      st.write("""Scatter charts""")      
      plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
      st.plotly_chart(plot, use_container_width=True)      

  else:
    st.warning(':exclamation: Awaiting user\'s input file')

st.write("##")

with st.container():
  st.write("---")
  # st.header("Get In Touch")
  # st.write(
    # """
    # - Let's collaborate and work together in telling stories using data...
    # - Together, we can make an impact when transforming complex data into **ACTIONABLE INSIGHTS**.
    # - Feel free to contact me by filling out the form below to let me know if we need to collaborate or need a mentor in specific fields of my expertise.
    # """)
  
  # Contact Documentation: https://formsubmit.co/ Change the email address
  # contact_form = """
  # <form action="https://formsubmit.co/ndelly@gmail.com" method="POST">
  #   <input type="hidden" name="_captcha" value="false">
  #   <input type="text" name="name" placeholder="Your name" required>
  #   <input type="email" name="email" placeholder="Your email" required>
  #   <textarea name="message" placeholder="Your message here" required></textarea>
  #   <button type="submit">Submit</button>
  # </form>
  # """
  

# Use local CSS file
  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
      
  local_css("style/style.css")
  
  
  col1, col2, col3 = st.columns((1, 1, 1))
  with col2:
    st.header("Get In Touch")
    # st.write(
    # """
    # - Let's collaborate and work together in telling stories using data...
    # - Together, we can make an impact when transforming complex data into **ACTIONABLE INSIGHTS**.
    # - Feel free to contact me by filling out the form below to let me know if we need to collaborate or need a mentor in specific fields of my expertise.
    # """)
    st.markdown(contact_form, unsafe_allow_html=True)
    st.write("##")
    st.image("https://complexdatainsights.com/wp-content/uploads/2020/09/contactNewk.png")
