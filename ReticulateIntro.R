## getting approach with reticulate and python
## https://rstudio.github.io/reticulate/

install.packages("reticulate")


#  The use_python() function enables you to specify an alternate version, for example:
  
library(reticulate)
use_condaenv()


### how to install a python library using R
py_install("pandas")
py_install("SciPy")
