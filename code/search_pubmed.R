library(tidyverse, suppressPackageStartupMessages())

# Pubmed searches
# Tidying, filtering, transformation, and plotting
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
  scale_color_manual(name = "FIELD",
                     values = c("red", "green4", "gray", "orange", "blue4", "green2", "magenta", "purple", "maroon", "blue1")) +
  labs(x = "Year", y = "Percentage of articles in PubMed", color = "FIELD") +
  theme_classic()

ggsave("figures/pubmed_search_line_plot.png", width = 8, height = 5)
