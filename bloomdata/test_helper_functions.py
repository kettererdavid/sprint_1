import bloomdata.helper_functions as hf

adjectives = ['crooked', 'sleepy', 'exorbitant', 'iffy']
nouns = ['salamander', 'bastard', 'chimpanzee', 'firetruck']

num1 = [1,2,3]
num2 = [4,5,6]


def test_random_phrase():
    assert type(hf.random_phrase(num1, num2)) == str
