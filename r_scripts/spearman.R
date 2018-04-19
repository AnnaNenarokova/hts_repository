f <- "/home/anna/bioinformatics/blasto/p57_last_annotation_stop_analysis_for_r.csv"
f <- "/home/anna/bioinformatics/blasto/p57_full_stop_analysis_for_r.csv"
data <- read.csv(file=f, head=TRUE, sep=",")

pep = data$peptide_cov
stop = data$stop_part
cov = data$rna_dna
gc = data$gc
len = data$len

plot(density(pep))
qqnorm(pep);qqline(pep)
plot(density(stop))
qqnorm(stop);qqline(stop)
shapiro.test(pep); shapiro.test(stop)

cor.test(data$peptide_cov, data$stop_part, method = "spearman")
cor.test(pep, stop, method = "kendall")
cor.test(cov, stop, method = "kendall")
cor.test(gc, stop, method = "kendall")
cor.test(cov, gc, method = "kendall")
cor.test(cov, pep, method = "kendall")
cor.test(len, pep, method = "kendall")
cor.test(len, cov, method = "kendall")
cor.test(len, gc, method = "kendall")
cor.test(len, stop, method = "kendall")
plot(pep,stop)

