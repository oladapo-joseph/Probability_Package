""" Aim of this project is to practice what I have learnt in AWS
    on producing good modular codes, git commit and all
    This project will change as I progress sha, hopefully i do something
    good with it.
"""
import math

class Distribution():
    """This is supposed to contain all the distribution functions i can
        find sha as simple as they seem.
        Attributes:
        Mean : represents the average of the data
        stdev: standard deviation of the data set
        data: comprises of the data set
    """

    def __init__(self, data):
        '''To check the validity of the data we are given, its checks the sum
            and returns the error message if any error.
        '''

        try:
            self.data = data
            x = sum(data)
        except Exception as e:
            print(f'Error in the data input, error type {e}')
        self.mean
        self.mode
        self.median

    def mean(self):
        """ This is a method that returns the mean of the data in its input,
        sum of the integers divided by the number of integers in the list
        """
        mean_value = sum(self.data)/len(self.data)
        self.mean = mean_value
        return (self.mean)

    def median(self):
        """ This is a method that returns the median value of the list of
        integers, if number of integers are odd, returns the median, if even
        it will return the mean of the two middle values.
        """
        datas = sorted(self.data)
        if len(datas)% 2 > 0:
            n = int(len(datas)/2)
            mid1 = datas[n]
            mid2 = datas[n+1]
            median_value = (mid1+mid2)/2
        else:
            median_value = datas[int(len(datas)/2)]
        self.median = median_value
        return(self.median)

    def mode(self):
        """ This is a function that returns the most common value out of the
            set.
        """

        mode_count= 0
        for i in self.data:
            count = self.data.count(i)
            if count> mode_count:
                mode_count = count
                mode_value = i
        self.mode = mode_value
        return (mode_value)
