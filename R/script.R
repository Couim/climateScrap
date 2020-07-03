library(rvest)
library(magrittr)
library (stringr)


infoclimatPage <- read_html("https://www.infoclimat.fr/climatologie-mensuelle/00014/juillet/2020/saint-martin-d-heres.html")

dayList <- infoclimatPage %>% 
  html_nodes(css="#resptable-releves > tbody:nth-child(2)") %>%
  extract2(1) %>%
  html_nodes(css = "tr > th > a:nth-child(3)")
dayList

dayList <- html_text(dayList)
dayList

# [31] "\n                    Vendredi 31\n                "
# dayList <- str_replace_all(dayList, "^(\n)+|\n$|(?!\b)( )+|[\n]*", "")

dayList <- str_replace_all(dayList, "^(\n)+( )+|(\n)+( )+$", "")
dayList

# dayList <- str_replace_all(dayList, "( )+$", "")
# dayList