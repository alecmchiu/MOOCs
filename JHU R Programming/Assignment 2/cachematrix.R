## Put comments here that give an overall description of what your
## functions do

## Write a short comment describing this function

# special matrix object that can cache/store its inverse
makeCacheMatrix <- function(x = matrix()) {
    
    # set initial inverse to NULL as it has not been calculated
    inv <- NULL
    
    # set function that will set the matrix x to the input and
    # initialize the inverse as NULL as it has not been calculated
    set <- function(y){
        x <<- y
        inv <<- NULL
    }
    
    # a get function that simply returns the matrix x
    get <- function() x
    
    # a function that will set the inverse based on
    # the built-in solve function
    setinverse <- function(solve) inv <<- solve
    
    # getinverse function that simply retrieves the inverse
    # that will be NULL if not solved before or the solved value
    getinverse <- function() inv
    
    # a list to all the functions within the special matrix object
    list(set = set, get = get, setinverse = setinverse, 
         getinverse = getinverse)
}


## Write a short comment describing this function

# computes the inverse of the special matrix objects
# will retrieve cached inverse if already solved
cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
    
    # retrieve the value of the inverse object using previously
    # built function
    inv <- x$getinverse()
    
    # if the value of the inverse is not NULL,
    # return the cached/stored value
    if (!is.null(inv)){
        message("getting cached data")
        return (inv)
    }
    
    # if is NULL, then store the matrix x in data
    data <- x$get()
    
    # call the solve function to obtain the inverse from data
    inv <- solve(data, ...)
    
    # set the inverse property of the special matrix object to
    # the calculated inverse value
    x$setinverse(inv)
    
    # return the inverse
    inv
}
