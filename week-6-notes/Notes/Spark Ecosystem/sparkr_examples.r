# SparkR example
library(SparkR)

sparkR.session(appName = "SparkRDemo")

df <- createDataFrame(data.frame(
  name = c("Asha", "Bala"),
  salary = c(60000, 72000)
))

showDF(df)
sparkR.session.stop()