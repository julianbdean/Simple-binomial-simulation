## library
library(tidyverse)
library(scales)

## set underlying parameters
n <- 10000 # number of trials
p <- 0.48 # baseline probability
bw <- 0.001 # bin width

## create table
tab <- data.frame(matrix(ncol = 2, nrow = 10000))
colnames(tab) <- c("sim", "wins")
tab$sim <- 1:10000

## simulate
for (i in 1:10000){
  tab$wins[i] <- sum(rbinom(n,1,p))
}

## Calculate the 95% CI
lower_bound <- quantile(tab$wins / n, 0.025)
upper_bound <- quantile(tab$wins / n, 0.975)

#plot

tab %>% 
  ggplot(aes(x = wins/10000)) +
  geom_freqpoly(binwidth = bw) +
  geom_vline(xintercept = lower_bound, linetype = 'dashed', color = 'red') +
  geom_vline(xintercept = upper_bound, linetype = 'dashed', color = 'red') +
  geom_area(data = tab %>% filter((wins/10000) >= lower_bound & (wins/10000) <= upper_bound),
            stat = "bin", binwidth = bw, aes(y = after_stat(count)), fill = 'gray', alpha = 0.2) +  # Shaded area
  xlab("Simulated Trump win probability") +
  ylab("Relative frequency") +
  scale_x_continuous(labels = scales::percent_format(scale = 100)) +
  theme_bw() +
  theme(
    panel.grid.major = element_blank(), 
    panel.grid.minor = element_blank(),
    axis.text.y = element_blank(),      
    axis.ticks.y = element_blank(),     
    axis.title.y = element_blank(),     
    axis.line.y = element_blank()      
  )