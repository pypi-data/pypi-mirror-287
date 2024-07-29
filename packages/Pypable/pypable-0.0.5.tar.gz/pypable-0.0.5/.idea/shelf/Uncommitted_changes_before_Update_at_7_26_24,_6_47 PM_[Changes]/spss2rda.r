Sys.setlocale(category = "LC_ALL", "en_US.iso88591")
library(foreign)
dastudy.ds<-read.spss("hermesout.sav", use.value.labels=FALSE, to.data.frame=TRUE, use.missings=TRUE)
save(dastudy.ds, file="rout.rda")
