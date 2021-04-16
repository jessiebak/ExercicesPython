#jouer la melodie de frère jacques

import winsound

help(winsound)
  
blanche = 1000
noire = 500
croche = 250
do, re, mi, fa, sol, la, si, sol2 = 130, 146, 164, 174, 195, 220, 246, 96
winsound.Beep(si,1000)
melody = [do, re, mi, do, do, re, mi, do, mi, fa, sol, mi, fa, sol, sol, la, sol, fa, mi, do, sol, la, sol, fa, mi, do, do,sol2, do, do, sol2,do]
duration = [noire, noire, noire, noire, noire, noire, noire, noire, noire,noire, blanche, noire, noire, blanche, croche, croche, croche, croche, noire, noire, croche, croche, croche, croche, noire, noire, noire, noire, blanche, noire, noire, blanche]
i = 0
for item in melody:

    winsound.Beep(item,duration[i])
    i+= 1





