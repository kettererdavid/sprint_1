def random_phrase():
    adjectives = ['crooked', 'sleepy', 'exorbitant', 'iffy']
    nouns = ['salamander', 'bastard', 'chimpanzee', 'firetruck']
    n = np.random.randint(4)
    m = np.random.randint(4)
    return adjectives[n]+nouns[m]

def random_float(min_val, max_val):
    return np.random.uniform(min_val, max_val)  

def random_bowling_score():
    return np.random.randint(301) 

def silly_tuple():
    string1 = random_phrase()
    star_rating = np.random.uniform(0, 5)
    string2 = np.around(star_rating,decimals = 1)
    string3 = random_bowling_score()
    return (string1, string2, string3)

def silly_tuple_list(num_tuples):
    result = []
    for i in range (num_tuples):
        result.append(silly_tuple())

    return result



