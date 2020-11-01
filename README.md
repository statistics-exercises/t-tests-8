# Paired comparison test

Lets now suppose that we want to design a hypothesis test that will determine whether a drug that is designed to reduce patients blood pressures is effective or not.  We are given a list of values for patients average blood pressure during a week where they are not taking the drug.  We are also given a second list of average systolic blood pressure values for those same patients during a week during which they are taking the drug.  I have provided you with these two sets of systolic blood pressure values in the two NumPy arrays in the code in `main.py` that are called `without_drug` and `with_drug`.  If you run the code now it will print out the data.  Looking at this data now will help you understand what I will tell you next (N.B. Ignore what it writes out about the hypothesis test for the moment.  Until you write the code to do the test that part of the output does not make sense.)  

What you can see from the data is that some patients had lower systolic blood pressures when they were taking the drug but some did not as there is some randomness in the data.  As we have learned throughout this course we can account for this randomness by using the tools of statistics.  In this case, we can look at the distribution of values for the difference in the average blood pressure for each patient in the week they did not take the drug and in the week they took the drug.  If the drug has no effect this distribution will be centred on zero as the patient blood pressure each week is essentially random.  If, by contrast, the drug has the desired effect the expectation for this difference will be less than zero as the net effect of the is to lower the patient's blood pressure.

This business of determining whether the drug is effective or not is thus simply a matter of determining the differences in the patients' systolic blood pressures during the week they took the drug and the week they did not take the drug.  The null and alternative hypotheses for the tests we need to perform are thus:

* `null hypothesis`: the expectation for the distribution of differences is zero
* `alternative hypothesis`: the expectation for the distribution of differences is negative.  

Notice, finally, that we have only tested the drug on a small number of patients.  In this case, we thus need to assume that the __statistic__ is a sample from a __t-distribution__ under the assumption of the null hypothesis.
  
__To complete this task you must write code in the cell on the right to perform the hypothesis test described above.__  In practise, completing this exercise amounts to writing the code that goes inside the two functions:

1. `testStatistic` - this function has two arguments `data1` and `data2`.  These are both NumPy arrays with the same length.  The first contains the data on the patients' blood pressures in the week the drug was not administered, while the second contains data on the patients' blood pressures during the week the drug was administered.  This code should calculate and return the test statistic on which the hypothesis test is defined.
2. `pvalue` - this function has two arguments `data1` and `data2`.  These are both NumPy arrays with the same length.  The first contains the data on the patients' blood pressures in the week the drug was not administered, while the second contains data on the patients' blood pressures during the week the drug was administered. This function should call `testStatistic`.  The value returned from this function should then be used to determine the __p-value__ for the statistical test 
