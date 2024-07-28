# genedist/genedist/calculate.py

import pandas as pd

def calculate_dist(fastafile_path, segment_name):
    f = open(fastafile_path, 'r')
    sequences = {}
    for line in f:
        if line[0] == ">":
            name = line.strip()
            sequences[name] = ''
        else:
            sequences[name] = sequences[name] + line.strip()
    f.close()
    df = pd.DataFrame()
    for key, value in sequences.items():
        i = 0
        j = 8
        end = len(value)
        NormalDictArray = []
        while j <= end and i <= (end - 8):
            NormalDict = {}
            s = value[i:j]
            NormalDict[key] = s
            alphaOne = s[:7]
            alphaTwo = s[1:]
            denominator = s[1:7]
            fAlphaOne = (value.count(alphaOne))
            fAlphaTwo = (value.count(alphaTwo))
            fDenominator = (value.count(denominator))
            LminusKplusOne = end - 9
            pAlphaOne = float((fAlphaOne) / (LminusKplusOne))
            pAlphaTwo = (fAlphaTwo) / (LminusKplusOne)
            pDenominator = (fDenominator) / (LminusKplusOne)
            if pDenominator == 0:
                ExpectedProbability = 0
            else:
                ExpectedProbability = pAlphaOne * pAlphaTwo / pDenominator
            ObservedFrequency = (value.count(s))
            ObservedProbability = ObservedFrequency / end
            FinalResult = (ObservedProbability - ExpectedProbability) / ExpectedProbability
            NormalDict[key] = FinalResult
            NormalDictArray.append(NormalDict)
            i += 1
            j += 1

        if df.empty:
            df = pd.DataFrame(NormalDictArray)
        else:
            df = pd.concat([df, pd.DataFrame(NormalDictArray)], axis=1)
    df.to_excel('output_{}.xlsx'.format(segment_name), index=False)
