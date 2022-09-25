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
# st.set_page_config(page_title="TMB Portfolio", page_icon=":sparkles:", layout = "wide")
st.set_page_config(page_title="TMB Portfolio", page_icon=":sunflower:", layout = "wide")

# Using local files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#######################################
# ----Assets----
#######################################

# For Professional Passion
pubstats = Image.open("figures/pubmed_search_bar_plot.png")

# Image objects: Use Image.open("")
wdcloud1 = Image.open("imgvideo/wordcloud.png")
gwas = Image.open("imgvideo/gwas_in_biome.png")
temp1 = Image.open("imgvideo/climate_nasa.png")
dna = Image.open("imgvideo/dna_composition.png")
# prot_align = Image.open("imgvideo/prot_align.png")

# GIF objects: Use open("")
abundgif1 = open("imgvideo/abund_bar.gif")

# Video objects: Use open("", "rb").read()
tempmp4 = open("imgvideo/climate_spiral_nasa.mp4", "rb").read()

#######################################
# ---- Header with salutation and introduction----
#######################################
with st.container(): 
  st.markdown("<h1 style='text-align: center; color: grey;'>TMB Professional Portfolio</h1>", unsafe_allow_html=True)
  st.write("##")
  st.write("##")
  st.subheader("Hi, I am Teresia Mrema-Buza:wave:")
  left, right = st.columns((2, 1))
  with left:
    st.title("A Microbiome,  Data Science, Bioinformatics, and Computational Biology Enthusiast, Consultant, and Mentor.") 
st.write("---")
  
with st.container():
  header1, separator, header2 = st.columns((2, 0.2, 1.5))
  with header1:
    st.header("Welcome to my Portfolio!")
    st.markdown(
    """
    #### My minimal PORTFOLIO displays areas of expertise and accomplishment. I want to dedicate more energy to developing \
    `open-source` user guides to support the scientific and analytics communities and anyone interested in what I do.
    """)
    
    st.write("##")
    st.success("""
    # My Passion
    ### Briefly, I am passionate about finding insights into complex data using integrated approaches.
    ### I am also interested in providing Mentorship in selected areas, including: 
      - Microbiome Bioinformatics
      - Machine Learning
      - Data Analysis in General
      - Data Visualization
      - Simple Web Applications... my new passion
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

    st.write(
      """
    #### Feel free to explore the entire portfolio. `KARIBU`:tada:      
      """)
    
  with header2:
    st.info(
    """
    #### Did you know? Microbiome & Machine Learning
    ...are fields getting lots of attention recently. The publication trend in PubMed is genuine proof!
    """)
    
    st.image(pubstats, width=600)
    # st.caption("This line chart was created using an `R script`, then imported into this web app generated using `streamlit` library and `Python`. Integration of different tools demonstrates robust solutions for gaining insights into complex data.")
    # st.subheader("Creating a plot using `ggplot2`")
    # with st.expander("Click to see or copy the R code"):
    #   st.code(pub_search_code, language="R")
    st.write("##")
    st.image(wdcloud1, width=550)
        
        
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
          ### On my `personal` and `organization` GitHub accounts:
          
          """)
        
        st.info(
          """
            - I am developing DIY practical user guides to support diverse data analytics communities.
            - Most of these guides are under development in my private repositories and will be shared publicly once completed.
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
st.write("##")
st.write("##")

with st.container():
  st.success(
    """
    # Achievements & In-Progress
    """)
#######################################
with st.container():
  st.write("##")
  column1, separator, column2 = st.columns((1, 0.5,  2.5)) 
  with column1:
    st.header(":books:Microbiome Bioinformatics")
    st.info("""
    Investigating the role of microbial communities in health and disease requires a thorough knowledge of the entire 
    analytical process. Using the wrong approaches can cost a significant amount of dollars and make a lengthy process 
    to achieve the desired results.)
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

      |Repo| Description| Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | [iMAP-PART1](https://github.com/tmbuza/iMAP-part1/) | How to Get Started with Microbiome Data Analysis | [eBook](https://complexdatainsights.com/books/microbiome-analysis/getting-started) |
      | [iMAP-PART2](https://github.com/tmbuza/iMAP-part2/) | Bioinformatics Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis) |
      | [iMAP-PART3](https://github.com/tmbuza/iMAP-part3/) | Data Preprocessing | [eBook](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing) |
      | [iMAP-PART4](https://github.com/tmbuza/iMAP-part4/) | Exploratory Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis) |
      """)

    st.write("##")
    st.write("""
      ### 3. End-to-End Microbiome Analysis eBooks

    
      |Repo| Description| Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | SMDA | Systematic Microbiome Data Analysis (SMDA)...In progress.| [eBook 1](https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/) |
      """)
    
st.write("---")




#######################################
#######################################
#######################################
with st.container():
  st.write("##")
  st.header(":books:Machine Learning")
  st.write("...In Progress...")
  st.write(
    """
    |Repo| Description| Repo Output| Remarks|
    |-------------------------|---------------------------------------------------|-----------------|-----------|
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||

    """)

  st.write("---")
  
with st.container():
  st.write("##")
  st.header(":books:Qualitative Data Analysis")
  st.write("...In Progress...")
  st.write(
    """
    |Repo| Description| Repo Output| Remarks|
    |-------------------------|---------------------------------------------------|-----------------|-----------|
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    """)

  st.write("---")
  
with st.container():
  st.write("##")
  st.header(":books:Quantitative Data Analysis")
  st.write("...In Progress...")
  st.write(
    """
    |Repo| Description| Repo Output| Remarks|
    |-------------------------|---------------------------------------------------|-----------------|-----------|
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    | [Repo goes here](https://github.com/tmbuza/addrepohere/) |  | [eBook goes here](https://complexdatainsights.com/books/addebookhere) ||
    """)

  st.write("---")
  # video_column, separator, text_column = st.columns((2, 0.5, 2))
  # with video_column:
  #   st.info("Click the image below to see how \nthe temperature is changing stepwise from 1880 to 2022!")
  #   st.video(tempmp4)
  #   st.write(
  #     """
  #     I used a custom R script to generate the MP4.
  #     """)
  #   st.write(
  #     """
  #     ...Inspired by [`code club Youtube video tutorials`](https://riffomonas.org/code_club/) presented by Pat Schloss\'s.
  #     """)
  #   
  # with separator:
  #   st.write("")
  #   
  # with text_column:
  #   st.subheader("Reproducible Research")
  #   st.write(
  #     """
  #     **The climate data can be replaced with any quantitative or time series data to reproduce similar image.**
  #     
  #     - Get the same experience. I will be happy to provide you with a reproducible and easily customizable practical user guide. 
  #     - If you are interested in outsourcing or consulting services, I can help you get the results faster. 
  #     - You will also have the option to request a source code associated with the sought analysis. 
  #     """
  #     )
  #     # - Explore a variety of climate data visualization available [**here!**](https://complexdatainsights.com/books/climate-analysis/climate-viz.html#plotly-image)
  # 

# with st.container():
#   video_column, text_column = st.columns((1, 2))
#   with video_column:
#     st.info("Click the image below to see how \nthe static image was generated stepwise from 1880 to 2022!")
#     st.video(tempmp4)
#     st.write(
#       """
#      I used a custom R script to generate the MP4.
#       """)

#---------------------------------------------

with st.container():
  st.write("##")
  st.header(":books:NGS Feature Annotation")
  st.write(""" ### 1. DNA Nucleotide Count App""")

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
      #### Nucleotide Count APP
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
  

#---------------------------------------------

with st.container():
  st.write("##")
  st.write(""" ### 2. Amino Acid Count App""")

# with st.container(): 
#   st.write("##")
#   st.markdown("<h1 style='text-align: left; color: #000000;'>Web Applications</h1>", unsafe_allow_html=True)

  panel1, separator1, panel2, separator2, panel3, separator3, panel4 = st.columns((1, 0.2, 1.5, 0.2, 1, 0.2, 1.5))
  # panel1, separator1, panel2 = st.columns((1, 0.2, 2))
  with panel1:
    st.image("https://complexdatainsights.com/wp-content/uploads/2022/09/aligments.png")
    # st.image("https://complexdatainsights.com/wp-content/uploads/2022/09/amino_acid_abbr.png", width=300)
    st.caption("A typical protein sequence contains 20 unique amino acids represented with single letter code. What is the composition of each amino acid?")
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

#---------------------------------------------
  st.write("##")
  st.write(""" ### 2. Exploratory Analysis App""")
  st.write("In progress...")
#---------------------------------------------  
 
#---------------------------------------------
  st.write("##")
  st.write(""" ### 3. Target Prediction App""")
  st.write("In progress...")
#---------------------------------------------



st.write("##")
st.write("##")
with st.container():
  st.write("---")
  st.header("Get In Touch")
  st.write(
    """
    - Let's collaborate and work together in telling stories using data...
    - Together, we can make an impact when transforming complex data into **ACTIONABLE INSIGHTS**.
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
  
# Use local CSS file
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


