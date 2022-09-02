import json
import requests
import streamlit as st


# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/. Select an Object including the two :: eg :tada: or :trophy: 
st.set_page_config(page_title="My Portifolio", page_icon=":trophy:", layout = "wide")

# 
# def load_lottieurl(url):
#   r = requests.get(url)
#   if r.status_code != 200:
#     return None
#   return r.json()

# Use local css
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#----Load Assets----
lottie_coding = "https://iconscout.com/lottie/data-analysis-4876889"
lottie_coding = "https://iconscout.com/lottie/data-analysis-3647751"
lottie_coding = "https://iconscout.com/lottie/data-analysis-4179002"

from PIL import Image
fig1 = Image.open("imgvideo/climate_nasa.png")
vid1 = open("imgvideo/climate_spiral_nasa.mp4", "rb").read()
# For NGS section
fig2 = Image.open("img/dna_nucleotides.jpeg")

# ---- Header section----
with st.container():
  st.subheader("Hi there, I am Teresia Mrema-Buza:wave:")
  st.title("A Data Science Enthusiast, Consultant, and Mentor")
  st.subheader("Welcome to my Portfolio! ")
  
  st.write(
  """
  I am passionate about developing resources for finding insights into complex data using the **State-of-the-Art** techniques, including:
    
  - **Bioinformatictics**
  - **Statistics**
  - **Machine learning**
  """
  )
  
  
  st.info("Learn more [Here >](https://complexdatainsights.com)")

# ---- What I do----

with st.container():
  # Insert a divider
  st.write("---")

  # Insert two spaces
  st.write("##")

  st.write(
    """
    
  On my GitHub I am developing multiple practical user guides for a variety of analysis of different types od data. These guides are particularly intended for users who:
    - are looking for user-friendly solutions in R or python to leverage their daily analytical tasks.
    - are struggling to understand how to efficiently process raw data and transform it into actionable insights.
    - are eager to learn more on how to go beyond the traditional data analysis by integrating multiple compartible tools to achieve a greter impact.
    - are looking for better solutions to visusalize the data and create sheareable reports in HTML, PDF or Word format and dashboard using R-Markdown.
  
  > If this sound interestiong to you, consider subscribing and turning on the notifications.
  
    """
  )
  
  
 # ----My Projects----
 
with st.container():
  st.write("---")
  st.header("NGS Bioinformatics Analysis in R")
  st.write("##")
  video_column, text_column = st.columns((1, 2))
  with video_column:
    st.video('https://www.youtube.com/watch?v=VzPD009qTN4')
    st.write("""
Video: Courtesy of [Kurzgesagt.Org ](https://kurzgesagt.org/) and is displayed here for educational purposes only!.
   """)
  with text_column:
    st.subheader("Microbiome Data")
    st.write(
      """
      - [Part 1](https://complexdatainsights.com/books/microbiome-analysis/getting-started): Getting started withe microbiome data analysis.
      - [Part 2](https://complexdatainsights.com/books/microbiome-analysis/bioinformatics-analysis): Bioinformatics analysis of amplicon and metagenomics data.
      - [Part 3](https://complexdatainsights.com/books/microbiome-analysis/data-preprocessing): Microbiome data tidying and transformation
      - [Part 4](https://complexdatainsights.com/books/microbiome-analysis/exploratory-analysis): Exploratory analysis and visualization.
      """
      )
      


with st.container():
  st.write("---")
  st.header("Quantitative Data Analysis")
  st.write("##")
  image_column, text_column = st.columns((1, 2))
  with image_column:
   st.image(fig1)
   st.write("""
   Inspired by Dr. Pat Scholl\'s tutorials at the [`code club`](https://riffomonas.org/code_club/). This image was generated using `R script`.
   """)
  with text_column:
    st.subheader("Climate Data")
    st.write(
      """
      - Get the same experience. I will be happy to provide you with reproducible and easily customizable practical user guide. 
      - If interested in outsoucing or consulting services I can help you get the results faster. 
      - You will also have the option to request a source code associated with the soughted analysis. 
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
      This MP4 was generated using an `R script`.
      """)


import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

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
      This web app quickly computes the number of nucleotide present in a given FASTA sequence. 
      
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
    st.caption("Bar chart showing number of nucleotide composition in a FASTA files.")
  
  ### Save dataframe locally
  df.to_csv("data/gene_seq1.csv")




with st.container():
  st.write("---")
  st.header("Get In Touch")
  st.write("##")
  
  # Contact Documentation: https://formsubmit.co/ Change the email address
  contact_form = """
  <form action="https://formsubmit.co/yndelly@gmail.com" method="POST">
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


