import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        difference = without_drug - with_drug
        mean = sum(difference) / len(difference) 
        sig = ( len(difference) / (len(difference) - 1 ) )*( sum(difference*difference) / len(difference) - mean*mean )
        stat = ( mean ) / np.sqrt( sig / len(difference) )
        self.assertTrue( np.abs( stat - testStatistic( without_drug, with_drug) )<1e-7, "your function to compute the test statistic is not correct" )
        
    def test_testStatII(self) : 
        difference = with_drug - without_drug
        mean = sum(difference) / len(difference) 
        sig = ( len(difference) / (len(difference) - 1 ) )*( sum(difference*difference) / len(difference) - mean*mean )
        stat = ( mean ) / np.sqrt( sig / len(difference) )
        self.assertFalse( np.abs( stat - testStatistic( without_drug, with_drug) )<1e-7, "Your function to compute the test statistic is incorrect as you have calculated with_drug-without_drug.  In this case, a POSITIVE test result would indicate that the null hypothesis should be rejected, which is at odds with the information in the description." )
    
    def test_pvalue(self) : 
        stat = testStatistic( without_drug, with_drug )
        pval = scipy.stats.t.cdf(stat,len(without_drug)-1)
        self.assertTrue( np.abs( pval - pvalue( without_drug, with_drug ) )<1e-7, "The function you have written to compute the p-value is not correct"  )
