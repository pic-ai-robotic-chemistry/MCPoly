from scipy.stats import rankdata
import os
import re

class irfig:

    """
    The method to get the information about infrared spectrum in Hessian data file.
    irfig(file, loc='./'))
    file: The name of Hessian data file.
    loc: Your location of Hessian data file.

    Functions:
    freq: All frequencies in the Hessian data file.
    intensity/I: All intensities of relevant frequencies in the Hessian data file. Add '_R' to get the reversed data.
    peaks_freq: The frequencies of all peaks in the Hessian data file.
    peaks: The intensities of all peaks in the Hessian data file. Add '_R' to get the negative data.

    Example 1:
        Input:
            from MCPoly.irmole import irfig
            a = irfig('et.hess.ir.dat')
            print(a.freq)
            print(a.intensity) # You can use a.I instead.
        Output:
            [300.0, 303.62, 307.23, 310.85, 314.47, 318.08, 321.7, 325.32, 328.93, 332.55, 336.17, 339.78, 343.4, 347.02, 350.64, 354.25, 
             357.87, 361.49, 365.1, 368.72, ... , 3981.92, 3985.53, 3989.15, 3992.77, 3996.38, 4000.0]
            [-9.899281394609716e-09, -9.996028893510811e-09, -9.805148692976218e-09, -9.342898010800127e-09, -8.647816684970167e-09, 
             -7.775497579132207e-09, -6.791310624976177e-09, -5.761989996244665e-09, -4.748926585307345e-09, -3.801915227086283e-09, 
             -2.9568809623015113e-09, -2.2338326743920334e-09, -1.6392505131079815e-09, -1.1685870049404912e-09, -8.092229109024629e-10,
             -5.443325790110976e-10, -3.5572611523093656e-10, -2.2578205971512944e-10, ... ]

    Example 2:
        Input:
            from MCPoly.irmole import irfig
            a = irfig('et.hess.ir.dat')
            print(a.peaks)
            print(a.peaks_R)
            print(a.peaks_freq)
        Output:
            [-9.996028893510811e-09, -0.001404185549745307, -0.0002438024389448401, -0.004000540678362086, -0.012333505576975767,
             -0.026633530207618605]
            [9.996028893510811e-09, 0.001404185549745307, 0.0002438024389448401, 0.004000540678362086, 0.012333505576975767,
             0.026633530207618605]
            [303.62, 828.05, 1410.36, 1504.4, 3030.69, 3095.8]

    Tip: You can use toprank to get the highest peak in the spectrum.
    
    """

    def __init__(self, file, loc='./'):
        f = open(loc+file, 'r')
        freq = []
        intensity = []
        peaks = []
        peaks_freq = []

        for line in f:
            a = re.findall(r'[0-9]+\.[0-9]+', line)
            if len(a) == 2:
                freq.append(eval(a[0]))
                intensity.append(eval(a[1])-1000)

        self.freq = freq
        self.intensity = intensity
        self.I = intensity
        self.intensity_R = [-i for i in intensity]
        self.I_R = [-i for i in intensity]

        for i, fq in enumerate(self.intensity):
            if i == 0 or i == len(self.intensity) - 1:
                continue
            try:
                if self.intensity[i] < self.intensity[i-1] and self.intensity[i] < self.intensity[i+1]:
                    peaks.append(self.intensity[i])
                    peaks_freq.append(self.freq[i])
            except:
                continue

        self.peaks = peaks
        self.peaks_R = [-i for i in peaks]
        self.peaks_freq = peaks_freq
        
        f.close()

    def toprank(self, num):
        """
        The method to get the highest peak in the spectrum.
        toprank(num)
        num: numbers of peaks. e.g. If num = 3, it will output the first three highest peak in the spectrum.

        After using it, two new data will be created.
        tops_freq: The frequencies of highest peaks in the Hessian data file.
        tops: The intensities of highest peaks in the Hessian data file. Add '_R' to get the negative data.

        Example:
            Input:
                from MCPoly.irmole import irfig
                a = irfig('et.hess.ir.dat')
                a.toprank(3)
                print(a.tops)
                print(a.tops_R)
                print(a.tops_freq)
            Output:
                [-0.026633530207618605, -0.012333505576975767, -0.004000540678362086]
                [0.026633530207618605, 0.012333505576975767, 0.004000540678362086]
                [3095.8, 3030.69, 1504.4]

        Tip: If you use code 'a.toprank(3)' above, it will directly output self.tops and tops_freq
        """
        
        rankorder = rankdata(self.peaks)
        #print(rankorder)
        
        tops = []
        tops_freq = []
        
        for j in range(1, num+1):
            for i,rank in enumerate(rankorder):
                if rank == j:
                    tops.append(self.peaks[i])
                    tops_freq.append(self.peaks_freq[i])

        self.tops = tops
        self.tops_R = [-i for i in tops]
        self.tops_freq = tops_freq
        return tops, tops_freq