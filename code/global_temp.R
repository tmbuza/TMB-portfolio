library(tidyverse, suppressPackageStartupMessages())
library(gganimate)
library(av)
library(plotly, suppressPackageStartupMessages())
library(glue)
library(htmlwidgets)
library(scales)
library(R.utils)
library(ncdf4) 
library(data.table)
library(lubridate)
library(ggridges)


readr::read_csv("https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv", skip = 1, na = "***", show_col_types = FALSE) %>%
  select(Year, month.abb) %>%
  pivot_longer(-Year, names_to="month", values_to="temp_diff") %>%
  drop_na() %>%
  saveRDS("data/climate_1880_2022.rds")

  temp_diff <- readRDS("data/climate_1880_2022.rds")
  next_jan <- temp_diff %>%
    filter(month == "Jan") %>%
    mutate(Year = Year - 1,
           month = "next_Jan")

  temp_data <- bind_rows(temp_diff, next_jan) %>%
    mutate(month = factor(month, levels = c(month.abb, "next_Jan")),
           month_number = as.numeric(month)) %>%
    arrange(Year, month) %>%
    filter(Year != 1879) %>%
    mutate(step_number = 1:nrow(.))

  annotation <- temp_data %>%
    slice_max(Year) %>%
    slice_max(month_number)

  temp_lines <- tibble(
    x = 12,
    y = c(1.5, 2.0),
    labels = c("1.5\u00B0C", "2.0\u00B0C")
  )

  month_labels <- tibble(
    x = 1:12,
    labels = month.abb,
    y = 2.7
  )

  anim <- temp_data %>% 
    ggplot(aes(x=month_number, y=temp_diff, group=Year, color=Year)) +
    geom_rect(aes(xmin=1, xmax=13, ymin=-2, ymax=2.4),
              color="black", fill="black",
              inherit.aes = FALSE) +
    geom_hline(yintercept = c(1.5, 2.0), color="red") +
    geom_label(data = temp_lines, aes(x=x, y=y, label=labels),
               color = "red", fill = "black", label.size = 0,
               inherit.aes=FALSE) +
    geom_text(data = month_labels, aes(x=x, y=y, label = labels),
              inherit.aes = FALSE, color="white",
              angle = seq(360 - 360/12, 0, length.out = 12)) +
    geom_label(aes(x = 1, y=-1.3, label = Year),
               color="white", fill="black",
               label.padding = unit(50, "pt"), label.size = 0,
               size=6) +
    geom_line() +
    scale_x_continuous(breaks=1:12,
                       labels=month.abb, expand = c(0,0),
                       sec.axis = dup_axis(name = NULL, labels=NULL)) +
    scale_y_continuous(breaks = seq(-2, 2, 0.2),
                       limits = c(-2, 2.7), expand = c(0, -0.7), 
                       sec.axis = dup_axis(name = NULL, labels=NULL)) +
    scale_color_viridis_c(breaks = seq(1880, 2020, 20),
                          guide = "none") +
    coord_polar(start = 2*pi/12) +
      labs(x = NULL,
         y = NULL,
         title = "Global Temperature Change (1880-2022)") +
    theme(
      panel.background = element_rect(fill="#444444", size=1),
      plot.background = element_rect(fill = "#444444", color="#444444"),
      panel.grid = element_blank(),
      axis.text.x = element_blank(),
      axis.text.y = element_blank(),
      axis.title.y = element_blank(),
      axis.ticks = element_blank(),
      axis.title = element_text(color="white", size=13),
      plot.title = element_text(color="white", hjust = 0.5,size = 15)
    ) +
    transition_manual(frames = Year, cumulative = TRUE)
  animate(anim, width=4.155, height=4.5, unit="in", res=300,)
  anim_save("imgvideo/climate_spiral.gif")

  animate(anim, width=4.155, height=4.5, unit="in", res=300,
          renderer = av_renderer("imgvideo/climate_spiral.mp4")
          )
