import numpy as np
sentences = np.recfromcsv('glass_data.tsv', delimiter = '\t')


#trial numnbers
print "How many trials fo you want to do?"
trialnum = int(raw_input("> "))

#if no output file exist pick a random number i and display the ith sentence in the terminal
from random import randrange
from termcolor import colored

#initiate trial list
trial_list = list(xrange(len(sentences)))

# check for the existing output file and make trial list
import os
if os.path.isfile('output.txt'):
    #if output file exists, check for compeleted trials.
    f = open('output.txt','a')
    #get the first column (completed trials)
    idxdone = np.recfromcsv('output.txt', delimiter = '\t')
    x = idxdone['index'] - 1
    #removed completed trials
    trial_list = [i for j, i in enumerate(trial_list) if j not in x]
else:
    #first time test is taken
    f = open('output.txt','a')
    f.write('index\tsentence\tresponse\n')


#give specified number of trials
for num in range(trialnum):

    #psendorandomly pick one number from the remaining items on the list
    i = np.random.choice(trial_list)
    #without replacement
    trial_list.remove(i)

    print(colored(sentences['text'][i], 'blue'))

#get the user rating
    print "negative(b)-neutral(n)-positve(m)?"
    ans = raw_input("> ")

    if ans == "b":
        answer = "Negative"
    elif ans =="n":
        answer = "Neutral"
    elif ans =="m":
        answer = "Positive"
    else: answer = "Something is wrong"

    f.write('%d\t%s\t%s\n' % (sentences['index'][i], sentences['text'][i], answer))
f.close()









