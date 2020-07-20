from .Basic_Stats import Distribution as DIS
import math
# import matplotlib.pyplot as plt


class Gaussian(DIS):

    def __int__(self, data, sigma=1):
        """ The gaussian class can be used to perform a couple of statistical
            analysis such as standard deviation, variance, etc.
        Attributes:
            Stdev : the standard deviaton of the data set
            mean : average value of the data set
            var : variance of the set of values
        """
        DIS.__init__(self, data, sigma)
        try:
            self.data = data
            x = sum(data)
        except Exception as e:
            print(f'Error : {e}')
        self.mean = self.mean()
        self.stdev
        self.var

    def Standard_Dev(self, sample=True):
        """This function calculates the standard deviaton of each value in the
            data set. It is calculated thus;
            standard deviaton = sqrt(((x-mean)^2)/n)
            where n = number of data set
                  x = each value in the data set
        Args:
            sample (bool) : determines whether the data is a sample or population

        Returns:
            stdev (float) : the value of the standard deviaton

        """
        no_of_value = len(self.data)
        sigma = 0
        mean = self.mean
        for i in range(len(self.data)):
            sigma += (self.data[i] - mean)**2
        if sample:
            stdev = sigma/(no_of_value + 1)
        else:
            stdev = sigma/(no_of_value)
        self.stdev = math.sqrt(stdev)

        return(self.stdev)

    def Variance(self, sample=True):
        """Calculates the variance of the data set_title
        Args:
            sample(bool): checks if the data is a sample or a population

        Returns:
            var (float): the variance of the value

        """
        sigma = 0
        no_of_value = len(self.data)
        mean = self.mean
        for i in range(len(self.data)):
            sigma += (self.data[i] - mean)**2
        if sample:
            var = sigma/(no_of_value + 1)
        else:
            var = sigma/(no_of_value)
        self.var = var

        return(self.var)

    def __repr__(self):
        """ Returns the characteristicsof the class, all the calculated values
        Args:
            None
        Returns:
            Attributes of gaussian class
        """
        return (f"Mean: {self.mean}\nStandard Deviation: {self.stdev}\nMode:{self.mode}\nMedian: {self.median}\nVariance: {self.var}")
