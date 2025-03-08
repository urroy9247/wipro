score=[23,45,67,89,12]
pcnt=0
ncnt=0
for i in score:
    if i>=50:
       pcnt=pcnt+1
    else:
       ncnt=ncnt+1
print(pcnt)
print(ncnt)