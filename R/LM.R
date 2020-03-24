LM <- function(X,y)
{
  X <- cbind(rnorm(50,160,sd = 15), sample(0:1,50,replace=TRUE))
  y <- 80+1.02*X[,1]+rnorm(50,0,1)
  dat=data.frame(y=y,X) 
  
  
  #  define X matrix and y vector
  X <- as.matrix(cbind(1,X))
  
  y <- as.matrix(y)
  dim(y)
  #  estimate the coeficients beta
  #  beta = ((X'X)^(-1))X'y
  beta <- solve(t(X)%*%X)%*%t(X)%*%y
  ## calculate residuals
  #  res = y - beta1 - beta2*X2
  res <- as.matrix(y-X%*%beta)
  
  ## define the number of observations (n) and the number of arameters (p)
  n <- nrow(X)
  p <- ncol(X)
  
  ## calculate the Variance-Covariance matrix (VCV)
  #  VCV = (1/(n-p))res'res(X'X)^(-1)
  VCV <- (1/(n-p))*as.numeric(t(res)%*%res)*solve(t(X)%*%X)
  print(VCV)
  ## calculate standard errors (se) of coefficients
  se <- sqrt(diag(VCV))
  
  ## calculate t
  t<- beta/se
  
  ## calculate the p-values
  p_value_beta0 <- 2*pt(abs(beta[1]/se[1]),df=n-p,lower.tail = F)
  p_value_beta1 <- 2*pt(abs(beta[2]/se[2]),df=n-p,lower.tail = F)
  p_value_beta2 <- 2*pt(abs(beta[3]/se[3]),df=n-p,lower.tail = F)
  p_value <- rbind(p_value_beta0,p_value_beta1,p_value_beta2)
  
  ## combine all necessary information
  output <- as.data.frame(cbind(beta,se,t,p_value))
  names(output) <- c("Estimate", "Std. Error","t","p-values")
  return(output)
}






