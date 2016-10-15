import argparse
import random

import names

def genSurname():
    rnd7 = random.randint(0, len(names.surname_prefix) - 1)
    rnd8 = random.randint(0, len(names.surname_suffix) - 1)

    return names.surname_prefix[rnd7] + names.surname_suffix[rnd8];

def generateName(sex):
    rnd2 = random.randint(0, len(names.nm2) - 1)

    if(sex == "male"):
        rnd4 = random.randint(0, len(names.nm4) - 1)
        rnd6 = random.randint(0, len(names.nm6) - 1)
        firstname = names.nm4[rnd4] + names.nm2[rnd2] + names.nm6[rnd6]
    else:
        rnd4 = random.randint(0, len(names.nm1) - 1)
        rnd6 = random.randint(0, len(names.nm3) - 1)
        firstname = names.nm1[rnd4] + names.nm2[rnd2] + names.nm3[rnd6]

    return "{} {}".format(firstname, genSurname())

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--sex", choices=["male", "female"], required=True,  help="The sex of the character")
    parser.add_argument("-n", "--number", default=1, type=int)

    arguments = parser.parse_args()

    names = []
    for i in range(arguments.number):
        names.append(generateName(arguments.sex))

    print names

if __name__ == '__main__':
    main()
