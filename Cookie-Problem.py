# -*- coding: utf-8 -*-
#Need this lib
from thinkbayes import Pmf

class Bowl():
    #Initial bow1&bowl2 sugars
    def __init__(self,bowl):
        total=100
        if bowl==1:
            self.vanilla=75
            self.chocolate=25
        if bowl==2:
            self.vanilla=50
            self.chocolate=50
    #get the probability of two kinds of sugar
    def get_bowl_prob(self):
        self.vanilla_prob=float(self.vanilla)/(self.vanilla+self.chocolate)
        self.chocolate_prob=float(self.chocolate)/(self.vanilla+self.chocolate)
    #Every running(take out one vanilla from the bowl)
    def MM_change(self):
        self.vanilla-=1 
            
            
class Cookie(Pmf,Bowl):
    #Use PMF in mouduel 'thinkbayes' to initialize the proability
    #in https://github.com/AllenDowney/ThinkBayes/
    def __init__(self,hypos):
        Pmf.__init__(self)
        for hypo_k,hypo_v in hypos.items():
            self.Set(hypo_k,1)
        self.Normalize()
    #Update and get the probability we want
    def Update(self,data,hypos):
        for hypo in self.Values():
            like=self.LikeHood(data,hypo,hypos)
            self.Mult(hypo,like)
        for k,v in hypos.items():
            print "Bow 1 :vanilla {}   chocolate{}".format(v.vanilla_prob,v.chocolate_prob)
            v.MM_change()
            
        self.Normalize()
    #Get the likehood
    def LikeHood(self,data,hypo,hypos):
        if data=='vanilla':
            mix=hypos[hypo]
            like=mix.vanilla_prob
        if data=='chocolate':
            mix=hypos[hypo]
            like=mix.chocolate_prob
        return like
    
#Start running
Bow1=Bowl(1)
Bow1.get_bowl_prob()
Bow2=Bowl(2)
Bow2.get_bowl_prob()
#A dict with Class Bowl contain :vanilla,chocolate，and their prob
hypos={'Bowl 1':Bow1,'Bowl 2':Bow2}
pmf=Cookie(hypos)
#take 3 sugars and calculate the probability that if you take out a
#vanilla flavor ,what is the probability of where it from,bowl1,or bowl2
for i in range(3):
    print "After {} Times".format(i)
    pmf.Update('vanilla',hypos)
    for hypo,prob in pmf.Items():
        print hypo,prob