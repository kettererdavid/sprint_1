import random
import numpy as np

adjectives = ['crooked', 'sleepy', 'exorbitant', 'iffy']
nouns = ['salamander', 'bastard', 'chimpanzee', 'firetruck']
num1 = [1,2,3]
num2 = [4,5,6]


def random_phrase(list1, list2):
    
    n = np.random.randint(len(list1))
    m = np.random.randint(len(list2))
    return str(list1[n])+ ' ' + str(list2[m])

if __name__ == '__main__':
    
    pass # print(random_phrase())