import math
nucs = {'A':0,'C':1,'G':2,'T':3}

def map_gene(val): 
    for key, value in nucs.items(): 
         if val == value: 
             return key

        
        
def NumberToPattern(Number,k):
    answer = ''
    quotient = Number
    remainder = Number%4
    pattern = [0]*k
    for i in range(len(pattern)):
        remainder = quotient%4
        quotient = math.floor(quotient/4)
        pattern[i] = remainder
    pattern = pattern[::-1]
    for i in range(len(pattern)):
        answer+=map_gene(pattern[i])
    return answer


def PatternToNumber(Pattern):
    index = 0
    power = []
    for i in range(len(Pattern)-1,-1,-1):
        power.append(i)
    for i in range(len(Pattern)):
        index += nucs[Pattern[i]]*(4**power[i])
    return index  

def ComputingFrequencies(Text,k):
    FrequencyArray = [0]*(4**k)
    for i in range(len(Text)-(k-1)):
        Pattern = Text[i:i+k]
        index = PatternToNumber(Pattern)
        FrequencyArray[index] += 1
    return FrequencyArray
    
    
def FasterFrequentWords(Text,k):
    FrequentPatterns = []
    FrequencyArray = ComputingFrequencies(Text,k)
    maxCount = max(FrequencyArray)
    for i in range((4**k)-1):
        if FrequencyArray[i]==maxCount:
            Pattern = NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns
