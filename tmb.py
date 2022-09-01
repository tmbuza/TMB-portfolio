import json
import requests
import streamlit as st


# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/. Select an Object including the two :: eg :tada: or :trophy: 
# st.set_page_config(page_title="My Portifolio", page_icon=":trophy:", layout = "wide")
st.set_page_config(page_title="My Portifolio", page_icon=":trophy:")

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
