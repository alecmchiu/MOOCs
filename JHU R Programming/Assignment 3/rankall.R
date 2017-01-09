rankall <- function(outcome, num = "best"){
    
    # read csv
    data <- read.csv("outcome-of-care-measures.csv",colClasses = "character")
    
    # check that state and outcome are valid
    valid = c("heart attack","heart failure", "pneumonia")
    
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
    new_data <- data[,c(2,7,outcome)]
    new_data <- new_data[complete.cases(new_data),]
    new_data <- new_data[order(new_data[,1]),]
    new_data <- new_data[order(new_data[,3]),]
    
    # extracting the data
    final
    states <- unique(data$State)
    
    if (num == "best"){
        num <- 1
    }

    for (each in states){
        state_data <- new_data[(new_data$State == each),]
        if (num == "worst"){
            final <- rbind(final, tail(state_data[,1:2], n = 1))
        }
        else {
            if (is.na(state_data[num,1:2]$Hospital.Name)){
                null_state <- state_data[num,1:2]
                null_state[2] <- each
                final <- rbind(final,null_state)
            }
            final <- rbind(final, state_data[num,1:2])
        }
    }
    
    # return hospital name in state with given rank
    final <- final[which(!is.na(final$State)),]
    final <- final[order(final[,2]),]
    names(final) <- c("hospital","state")
    return(final)
}