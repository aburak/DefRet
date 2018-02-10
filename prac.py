#!/usr/bin/env python
import numpy as np
import subprocess

words = []
meanings = []
with open("/home/aburak/words.txt", "r") as f:
    for line in f:
        tmp = line.split("\t")
        tmp[-1] = tmp[-1].strip()
        words.append(tmp[0])
        meanings.append(tmp[1:])

n_opts = 5
n_true = 0
n_false = 0
inp = "y"
subprocess.call("clear")
while inp == 'y':
    m_ind = np.random.randint(0, high=len(meanings))
    aux = np.arange(len(words))
    np.random.shuffle(aux)
    w_ind = aux[:n_opts]

    if m_ind not in w_ind:
        tmp = np.random.randint(0, high=n_opts)
        w_ind[tmp] = m_ind

    print("Definition(s):")
    for i in xrange(len(meanings[m_ind])):
        print(meanings[m_ind][i])

    print("Options:")
    for i in xrange(len(w_ind)):
        print(str(i) + ". " + words[w_ind[i]])
    print("\nChoose the correct option: ")
    inp = raw_input()
    print(inp)

    if w_ind[int(inp)] == m_ind:
        print("Correct!\n")
        n_true += 1
    else:
        print("Wrong! The correct answer was " + words[m_ind] + "\n")
        n_false += 1

    print("To continue, input y: ")
    inp = raw_input()
    subprocess.call("clear")

print("Summary:\nNumber of correct answers: " + str(n_true) + "\nNumber of false answers: " + str(n_false))
