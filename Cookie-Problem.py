# -*- coding: utf-8 -*-
#Need this lib
from thinkbayes import Pmf

class Bowl():
    def __init__(self,bowl):
        total=100
        if bowl==1:
            self.vanilla=75
            self.chocolate=25
        if bowl==2:
            self.vanilla=50
            self.chocolate=50
    def get_bowl_prob(self):
        self.vanilla_prob=float(self.vanilla)/(self.vanilla+self.chocolate)
        self.chocolate_prob=float(self.chocolate)/(self.vanilla+self.chocolate)
    def MM_change(self):
        self.vanilla-=1 
            
            
class Cookie(Pmf,Bowl):
    def __init__(self,hypos):
        Pmf.__init__(self)
        for hypo_k,hypo_v in hypos.items():
            self.Set(hypo_k,1)
        self.Normalize()
        
    def Update(self,data,hypos):
        for hypo in self.Values():
            like=self.LikeHood(data,hypo,hypos)
            self.Mult(hypo,like)
        for k,v in hypos.items():
            print "Bow 1 :vanilla {}   chocolate{}".format(v.vanilla_prob,v.chocolate_prob)
            v.MM_change()
            
        self.Normalize()
    def LikeHood(self,data,hypo,hypos):
        if data=='vanilla':
            mix=hypos[hypo]
            like=mix.vanilla_prob
        if data=='chocolate':
            mix=hypos[hypo]
            like=mix.chocolate_prob
        return like
    
    
Bow1=Bowl(1)
Bow1.get_bowl_prob()
Bow2=Bowl(2)
Bow2.get_bowl_prob()
hypos={'Bowl 1':Bow1,'Bowl 2':Bow2}
pmf=Cookie(hypos)
for i in range(3):
    print "After {} Times".format(i)
    pmf.Update('vanilla',hypos)
    for hypo,prob in pmf.Items():
        print hypo,prob