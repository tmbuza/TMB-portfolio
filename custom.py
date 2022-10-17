pub_search_code ="""
  library(tidyverse)
  
  # Importing preprocessed Pubmed searches
  read_csv("data/search_counts.csv", show_col_types = TRUE) %>% 
    select(year, ends_with("_res")) %>%  
    filter(year >= 1991) %>% # Filter as you please!
    mutate(
      Microbiome = 100 * (microb_res / all_res),
      Genomics = 100 * (genom_res / all_res),
      Proteomics = 100 * (proteo_res / all_res),
      Metabolomics = 100 * (metabol_res / all_res),
      Lipidomics = 100 * (lipid_res / all_res),
      Phenomics = 100 * (pheno_res / all_res),
      Transcriptomics = 100 * (transcr_res / all_res),
      MachineLearning = 100 * (ml_res / all_res),
      Bioinformatics = 100 * (bioinfo_res / all_res),
      Pharmacogenomics = 100 * (pharma_res / all_res),
      AllArticles = all_res) %>% 
    select(-AllArticles, -ends_with("_res")) %>% 
    pivot_longer(-year) %>%
    filter(value > 0) %>% 
    ggplot(aes(x = year, y = value, group = name, color = name)) +
    geom_line(size = 1.2) +
    
    # Optional color scaling
    scale_color_manual(name = "FIELD",
                       values = c("red", "green4", "gray", "orange", "blue4", "green2", "magenta", "purple", "maroon", "blue1")) +
    labs(x = "Year", y = "Percentage of articles in PubMed", color = "FIELD") +
    theme_classic()
  
  ggsave("figures/pubmed_search_bar_plot.png", width = 8, height = 5)
"""

def add_margin(ax,x=0.05,y=0.05):
  xlim = ax.get_xlim()
  ylim = ax.get_ylim()
  xmargin = (xlim[1]-xlim[0])*x
  ymargin = (ylim[1]-ylim[0])*y
  ax.set_xlim(xlim[0]-xmargin,xlim[1]+xmargin)
  ax.set_ylim(ylim[0]-ymargin,ylim[1]+ymargin)

import streamlit as st      
def project_header():
  st.markdown(
    """
    <header style= 'background-color: #008000'; color: 'white'>
    <h1 
    style='
      text-align: center;
      color: white; 
      font-size: 4em; 
      '>
      Enter Header Title Here
    </h1>
    
    <h2 
    style='
      text-align: center; 
      color: #BBBBBB;
      font-size: 35px;'> 
      Enter sub header title here
    </h2>
    
    <h3 
    style='
      text-align: center; 
      color: #CCCCCC; 
      font-size: 20px;'>
      Developer: Enter Name of author or developer here
    </h3>
  
    <logo><center>
      <a href='https://complexdatainsights.com'>
      <img src='https://complexdatainsights.com/wp-content/uploads/2020/10/logo-1.png' 
        alt=' page cover'
        width='20%' 
        style='padding: 0 15px; 
        float: center;'/></a>
      </center></logo>
    </header>
    
    """, unsafe_allow_html=True)

import os
import stat
import time
import datetime

def date_updated(pathtofile):
  modTimesinceEpoc = os.path.getmtime(pathtofile)
  modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
  st.write("Last Modified: ", modificationTime )
  return modificationTime

