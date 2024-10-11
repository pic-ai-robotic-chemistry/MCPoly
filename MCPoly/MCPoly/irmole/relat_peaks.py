def relat_peaks(selected_freq, intensity, freq, tolerance=10.0, neednum=False):

    """
    The method to get related peaks between the infrared spectrum in Hessian data file and/or output file.
    relat_peaks(selected_freq, intensity, freq, tolerance=10.0, neednum=False)
    selected_freq: Frequencies of selected peaks.
    intensity: Prepared intensity list.
    freq: Prepared frequency list.
    tolerance: The frequency deviation between the peak. The default is 10 cm^-1.
    neednum: When it is 'True', it will show the number of peak in prepared list. The default is False.

    Example:
        Input:
            from MCPoly.irmole import irfig
            from MCPoly.irmole import irout
            from MCPoly.irmole import relat_peaks

            a = irfig('2_0.000.hess.ir.dat')
            b = irout('2_0.000')
            a.toprank(3)
            real_tops, real_tops_freq, js = relat_peaks(a.tops_freq, b.I, b.freq, neednum=True)
            # When neednum = False, there are only two outputs, real_tops and real_tops_freq.
            print(real_tops)
            print(real_tops_freq)
            print(js)
        Output:
            [67.14, 61.64, 10.14]
            [3096.23, 3028.07, 1504.91]
            [23, 19, 17]
    """
    
    real_tops = []
    real_tops_freq = []
    js = []
    
    for t_fq in selected_freq:
        base = 0
        base_freq = 0
        j = 0
        for i,fq in enumerate(freq):
            if abs(t_fq-fq) < tolerance:
                #print(t_fq, fq, I[i])
                if intensity[i] > base:
                    base = intensity[i]
                    base_freq = freq[i]
                    j = i
        real_tops.append(base)
        real_tops_freq.append(base_freq)
        js.append(j)

    if neednum == True:
        return real_tops, real_tops_freq, js
    else:
        return real_tops, real_tops_freq