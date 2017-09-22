#Python Program to Concatenate Two Dictionaries Into One
Age_of_Boys = {'Boy1': 10,
                 'Boy2': 20,
                 'Boy3': 30}
print("First Dictionary is : ", Age_of_Boys)
Age_of_Girls = {'Girl1':9,
                'Girl2':19,
                'Girl3':29}
print("Second Dictionary is : ", Age_of_Girls)
#Combined_Age = dict(Age_of_Boys.items() + Age_of_Girls.items())
Combined_Age = {}
Combined_Age.update(Age_of_Boys)
Combined_Age.update(Age_of_Girls)
print("Combined Dictionary is : ", Combined_Age)
