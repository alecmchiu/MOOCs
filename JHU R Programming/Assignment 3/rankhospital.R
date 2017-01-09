rankhospital <- function(state,outcome,num){
    
    # read csv
    data <- read.csv("outcome-of-care-measures.csv",colClasses = "character")
    
    # check that state and outcome are valid
    valid = c("heart attack","heart failure", "pneumonia")
    valid_states <- unique(data$State)
    
    if(!(state %in% valid_states)){
        stop("invalid state")
    }
    
    if (!(outcome %in% valid)){
        stop("invalid outcome")
    }
    
    #set column
    if(outcome == "heart attack"){
        outcome = 11
    }
    else if (outcome == "heart failure"){
        outcome = 17
    }
    else if (outcome == "pneumonia"){
        outcome = 23
    }
    
    # numeric mode
    suppressWarnings(data[,outcome] <- as.numeric(data[,outcome]))
    
    # subsetting
    data_by_state <- data[which(data$State == state),]
    data_by_outcome <- data_by_state[,c(2,outcome)]
    final <- data_by_outcome[complete.cases(data_by_outcome),]
    final <- final[order(final[,1]),]
    final <- final[order(final[,2]),]
    
    # if num is a string
    if (num == "best"){
        num <- 1
    }
    else if (num == "worst"){
        num <- nrow(final)
    }
    else if (num > nrow(final)){
        return(NA)
    }
    
    # return hospital name in state with given rank
    final[num,]$Hospital.Name
}