#!/usr/bin/env python


import pickle


try :
    with open('pickle.txt', 'wb') as mfile : 
        pickle.dump([1,2,'apple','pie'], mfile)

    with open('pickle.txt', 'rb') as mfile :
        a_list = pickle.load(mfile)

except pickle.PickleError as perr :
    print('Pickling Error: ' + str(perr))

print(a_list)
