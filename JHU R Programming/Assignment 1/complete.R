complete <- function(directory, id = 1:332){
    # directory is a vector indicating location of CSV files
    # id is an integer vector containing the ID numbers to be used
    # function will return a data frame with the ID and complete cases
    
    files_list <-dir(directory)
    
    wd <- getwd()
    
    nobs <- numeric()
    
    for (item in id){
        data <-read.csv(file.path(wd,directory,files_list[item]))
        data <- complete.cases(data)
        nobs <- c(nobs, length(data[data == TRUE]))
    }
    
    data.frame(id, nobs)
}