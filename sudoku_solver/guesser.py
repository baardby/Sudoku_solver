import numpy as np

def findMostImportantRow(mask): #Finner raden som er mest utfylt uten å være helt utfylt
    dummy = np.zeros(mask[0].size)
    for i in range(mask[0].size):
        dummy[i] = np.sum(mask[i])
    return np.argmax(dummy)

def findMostImportantCol(mask): #Finner kolonnen som er mest utfylt uten å være helt utfylt
    dummy = np.zeros(mask[0].size)
    for i in range(mask[0].size):
        temp = mask.transpose()
        dummy[i] = np.sum(temp[i])
    return np.argmax(dummy)