pollutantmean <- function(directory, pollutant, id = 1:332){
    # directory is the location of CSV files
    # pollutant is either "sulfate" or "nitrate"
    # id is an integer vector containing the ID numbers to be used
    # function will calculate the mean for a pollutant
    
    files_list <- dir(directory)
    
    wd <- getwd()
    
    for (item in id){
        if(item == id[1]){
            data <- read.csv(file.path(wd,directory,files_list[item]))
        }
        else {
            temp <-read.csv(file.path(wd,directory,files_list[item]))
            names(temp) <- names(data)
            data <-rbind(data, temp)
        }
    }
    
    mean(data[[pollutant]], na.rm = TRUE)
}