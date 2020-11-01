import numpy as np
import scipy.stats

def testStatistic( data1, data2 ) :
  # Your code to compute the test statistic goes here
  # you also need to replace the return statement with the 
  # correct code
  return 1
  
def pvalue( data1, data2 ) :
  # Your code to calculate the p-value goes here.
  # you also need to replace the return statement with the 
  # correct code
  return 1
  
without_drug= np.array([131, 124, 132, 127, 124, 126, 135])
with_drug = np.array([132, 129,  126, 127, 126, 122, 123])
print("Blood pressure results:")
for i in range(len(with_drug)) : 
  print( "Patient", i, "without drug", without_drug[i], "and with", with_drug[i] )
  
# This part of the code does the hypothesis test
print("The null hypothesis is that the data is that the drug has no effect")
print("The alternative hypothsis is that the drug lowers patient's blood pressures")
print("The p-value for this hypothesis test is", pvalue(without_drug, with_drug) )
