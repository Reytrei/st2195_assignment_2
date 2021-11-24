library(rvest)
cars_url <- "https://en.wikipedia.org/wiki/Comma-separated_values"
html <- read_html(cars_url)
cars_table <- html_node(html, ".wikitable")
table <-html_table(cars_table)

write.csv(table,"D:/Juanma/Juanma/Universidad/Programacion/st2195_assignment_2/r_csv//CSV_file.csv",row.names =FALSE)
