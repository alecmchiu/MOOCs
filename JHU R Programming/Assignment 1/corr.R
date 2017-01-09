corr <- function(directory, threshold = 0){
    # directory is location of CSV files
    # threshold is value of complete cases required
    
    files_list <-dir(directory)
    
    wd <- getwd()
    
    correlations <- numeric()
    
    for (item in files_list){
        
        data <-read.csv(file.path(wd,directory,item))
        cases <- complete.cases(data)
        if(c(length(cases[cases == TRUE])) > threshold){
            correlations <- c(correlations,cor(data$sulfate, data$nitrate, use = "complete.obs"))
        }
    }
    
    correlations
}