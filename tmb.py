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
# ----Assetes----
#######################################
lottie_coding = "https://iconscout.com/lottie/data-analysis-4876889"
lottie_coding = "https://iconscout.com/lottie/data-analysis-3647751"
lottie_coding = "https://iconscout.com/lottie/data-analysis-4179002"

from PIL import Image
# For Professional Passion
wcloud1 = Image.open("imgvideo/wordcloud.png")
gwas = Image.open("imgvideo/gwas_in_biome.png")

# For microbiome data analysis
gif1 = open("imgvideo/abund_bar.gif")

# For quantitative data analysis
fig1 = Image.open("imgvideo/climate_nasa.png")

vid1 = open("imgvideo/climate_spiral_nasa.mp4", "rb").read()

# For the NGS section
fig2 = Image.open("img/dna_nucleotides.jpeg")

#######################################
# ---- Header with salutation and introduction----
#######################################
with st.container():
  header1, header2 = st.columns((2, 1))
  with header1:
    st.text(" ...work in progress...")
    st.subheader("Hi, I am Teresia Mrema-Buza:wave:")
    st.title("A Data Science, Bioinformatics and Computational Biology Enthusiast, Consultant and Mentor.") 
    # Insert a divider
    st.header("Welcome to my Portfolio!")

    st.markdown(
    """
    #### I started compiling my minimal `Portfolio` to remind myself of what I can do in science and technology. I can then dedicate more energy to developing practical user guides in areas of expertise to help anyone interested in what I do.
    #### Feel free to explore my passion in this portfolio. `KARIBU`:tada:
    """)
    st.write("---")
  with header2:
    st.markdown(
    """
    """)
    
with st.container():    
  st.write("##")
  st.title("Professional Passion") 
  header1, header2 = st.columns((2, 1))
  with header1:
    st.success(
        """
        I am passionate about developing resources for finding insights into complex data using **State-of-the-Art** techniques, including:
        
      - **Bioinformatictics**
      - **Statistics**
      - **Machine learning**
      
      On my GitHub, I am developing multiple practical user guides for a variety of analyses of different types of data. These guides intend to help users who: 
        - are looking for user-friendly solutions in R or python to leverage their daily analytical tasks.
        - are struggling to understand how to process raw data and transform it into actionable insights efficiently.
        - are eager to learn more about going beyond traditional data analysis by integrating multiple compatible tools to achieve a more significant impact.
        - are looking for better solutions to visualize the data and create shareable reports in HTML, PDF, or Word format and dashboard using R-Markdown.
        """
        )  

  with header2:
    st.image(wcloud1)

    
#######################################
# ----My Projects----
#######################################
with st.container():  
  st.write("---")
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
      - [Paper 2](https://www.nature.com/articles/s41598-019-53969-7): Microbial Diversity in Bushmeat Samples Recovered from the Serengeti Ecosystem in Tanzania.
      - [eBook 1](https://complexdatainsights.com/books/microbiome-analysis/end-to-end-user-guide/): Systematic Microbiome Data Analysis (SMDA)...In progress.
      
      ### 2. GitHub Repositories

      #### Original iMAP
      
      |Repo| Description| Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|
      | iMAP | Integrated Mocrobiome Analysis pipeline | [GitHub Page](https://tmbuza.github.io/iMAP/) |
      ||||
     
      ## Improved iMAP
      ### Quick Glimpse
      > Investigating the role of microbial communities in health and disease requires a thorough knowledge of the entire analytical process. Using wrong approaches can cost a significant amount of dollars and lengthy process to achieve the desired results. This is <b>PART 1</b> of the practical user guides intended to provide analytical support to the microbiome research community. The entire guide is reproducible, allowing users to easily follow along. If interested, user may use this model to publish their findings in a book format.

      |Repo| Description| Repo Output|
      |-------------------------|---------------------------------------------------|-----------------|      
      | iMAP-PART1 | How to Get Started with Microbiome Data Analysis | [eBook](https://complexdatainsights.com/books/microbiome-analysis/getting-started) |
      | iMAP-PART2 | Bioinformatics Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis) |
      | iMAP-PART3 | Data Preprocessing | [eBook](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing) |
      | iMAP-PART4 | Exploratory Analysis of Microbiome Data | [eBook](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis) |



     ### 3. Web Applications 
     ...In Progress...
     
        """
        )
              # - Practical User Guides for improved `iMAP.`
      # The [original iMAP repo](https://tmbuza.github.io/iMAP/)
      #   - [Part 1](https://complexdatainsights.com/books/microbiome-analysis/getting-started): Getting started with microbiome data analysis.
      #   - [Part 2](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis): Bioinformatics analysis of amplicon and metagenomics data.
      #   - [Part 3](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing): Microbiome data tidying and transformation
      #   - [Part 4](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis): Exploratory analysis and visualization.


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
   st.caption("Image Source: https://www.biologydiscussion.com/")

  with text_column:
    st.title("Count Nucleotides APP")
    st.markdown(
      """
      This web app quickly computes the number of nucleotides present in a given FASTA sequence. 
      
      `Give it a try!`
      """
    )
    st.write("##")
    st.subheader('Enter query sequence in the box below')
    sequence_input = ">LC557153.1 Erwinia amylovora Eaap3-1 gene for 16S rRNA, partial sequence\nCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGAACGGTAGCACAGAGAGCTTGCTCTTGG \
  GTGACGAGTGGCGGACGGGTGAGTAATGTCTGGGAAACTGCCCGATGGAGGGGGATAACTACTGGAAACG \
  GTAGCTAATACCGCATAACGTCTACGGACCAAAGTGGGGGACCTTCGGGCCTCACACCATCGGATGTGCC \
  CAGATGGGATTAGCTGGTAGGTGGGGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGAT \
  GACCAGCCACACTGGAACTGAGACACGGTCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAA \
  TGGGCGCAAGCCTGATGCAGCCATGCCGCGTGTATGAAGAAGGCCTTCGGGTTGTAAAGTACTTTCAGCG \
  GGGAGGAAGGGGGAGAGGTTAATAACCTCTTCCATTGACGTTACCCGCAGAAGAAGCACCGGCTAACTCC \
  GTGCCAGCAGCCGCGGTAATACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAG \
  GCGGTCTGTCAAGTCGGATGTGAAATCCCCGGGCTTAACCTGGGAACTGCATTCGAAACTGGCAGGCTAG \
  AGTCTCGTAGAGGGGGGTAGAATTCCAGGTGTAGCGGTGAAATGCGTAGAGATCTGGAGGAATACCGGTG \
  GCGAAGGCGGCCCCCTGGACGAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATA \
  CCCTGGTAGTCCACGCCGTAAACGATGTCGACTTGGAGGCTGTTCCCCTGAGGAGTGGCTTCCGGAGCTA \
  ACGCGTTAAGTCGACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGC \
  ACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCTGGCCTTGACATCCACGGA \
  ATTCTGCAGAGATGCGGAAGTGCCTTCGGGAACCGTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTG \
  TTGTGAAATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCGATTCGGTCGGG \
  AACTCAAAGGAGACTGCCGGTGATAAACCGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTAC \
  GGCCAGGGCTACACACGTGCTACAATGGCGCATACAAAGAGAAGCGACCTCGCGAGAGCAAGCGGACCTC \
  ATAAAGTGCGTCGTAGTCCGGATCGGAGTCTGCAACTCGACTCCGTGAAGTCGGAATCGCTAGTAATCGT \
  AGATCAGAATGCTACGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGGAGTGGG \
  TTGCAAAAGAAGTAGGTAGCTTAACCTTCGGGAGGGCGCTTA"

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
    st.caption("Bar chart showing the number of nucleotide composition in a FASTA file.")
  
  ### Save data frame locally
  df.to_csv("data/gene_seq1.csv")




with st.container():
  st.write("---")
  st.header("Get In Touch")
  st.write("##")
  
  # Contact Documentation: https://formsubmit.co/ Change the email address
  contact_form = """
  <form action="HTTPS://formsubmit.co/yndelly@gmail.com" method="POST">
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


