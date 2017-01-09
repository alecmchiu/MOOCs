best <- function(state, outcome){
    # state = 2 letter state abreviation
    # outcome_name = outcome name
    
    valid = c("heart attack","heart failure", "pneumonia")
    
    # read outcome data
    data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
    valid_states <- unique(data$State)
    
    # check that state and outcome are valid
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
    
    # subset by state
    data_by_state <- data[which(data$State == state),]
    minimum = min(data_by_state[,outcome], na.rm = TRUE)
    
    #return hospital name in that state with lowest 30-day death rate
    hospital = subset(data_by_state,data_by_state[,outcome]==minimum)
    hospital$Hospital.Name
}