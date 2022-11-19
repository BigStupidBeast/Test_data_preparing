from allpairspy import AllPairs

#https://pypi.org/project/allpairspy/#basic-usage

parameters = [
    ["Brand X", "Brand Y"],
    ["98", "NT", "2000", "XP"],
    ["Internal", "Modem"],
    ["Salaried", "Hourly", "Part-Time", "Contr."],
    [6, 10, 15, 30, 60],
]
'''
    We have
    radio gender: male female other
    check box: drive license
    radio favorite fruit: peach banana
    int field age 21-120
    text field name
    drope down list: bold short hairy
'''
raw_dictionari = {

}


if __name__ == '__main__':



    print("PAIRWISE:")
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{:2d}: {}".format(i, pairs))


