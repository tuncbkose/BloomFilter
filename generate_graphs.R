library(readr)
library(ggplot2)

# Part 1

setwd("data/")

files_all <- list.files(pattern="*all.txt") # Ends with all, not all the files in directory
files_first <- list.files(pattern="*first.txt")
files <- c(files_all, files_first)

for (file in files){
  data <- read_csv(file, 
                   col_names = FALSE)
  data <- cbind(data, i=1:dim(data)[1])
  ggplot(data, aes(x=i, y=X1)) + geom_col(width=0.85)
  filename <- paste(substr(file, 1, nchar(file)-3),"png", sep="")
  ggsave(filename)
}