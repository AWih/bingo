'''
Created on 29.4.2016

@author: Alvar
'''

'''
bingoarvonta
'''

import random



class bingolappu:
    
    

    def __init__(self):

        #alustetaan bingolappu nollilla
        #ts. luodaan 5x5-nollamatriisi

        self.__SARAKKEEN_PITUUS = 5
        self.__RIVIN_PITUUS = 5
        self.__MAXNRO = 75
        

        self.numerot = [0] * self.__SARAKKEEN_PITUUS
        #[0,0,0,...,0]

        for i in range(5):
            self.numerot[i] = [0] * self.__RIVIN_PITUUS
            #[[0,0,0,...,0] ,0,0,0,...,0]
            #nyt on valmis 5 x 5 -suuruinen bingotaulukko

        self.sisaltavat_luvut = [0]


    def arvo_numerot(self, arvontamoodi,):

        if arvontamoodi == 'tavallinen':
            self.numerot = self.tavallinen()
        
        if arvontamoodi == 'sarakkeet':
            self.numerot = self.sarakkeet()


    def tavallinen(self):

        # muodostetaan lista luvuista, joita voidaan lisata
        #lappuun.

        arvottavat_luvut = [0]
        for n in range(1,self.__MAXNRO + 1):
            arvottavat_luvut.append(n)
        
        for i in range(self.__SARAKKEEN_PITUUS):
            for j in range(self.__RIVIN_PITUUS):
                lisattava_luku = random.choice(arvottavat_luvut)
                self.numerot[i][j] = lisattava_luku
                
                self.sisaltavat_luvut.append(lisattava_luku)
                
                #juuri lisatty luku poistetaan listasta,
                # jotta samoja lukuja ei tulisi monta kertaa.
                arvottavat_luvut.remove(lisattava_luku)
                
                
        return self.numerot
    
    
    
    
    def sarakkeet(self, valit = []):
        '''
        valit on 2-ulott. lista sarakkeiden luvuista
        
        Esim. 1. sarakkeessa saa olla nrot 1-15:
        valit[0] = [1,2,3,...,15]
        
        
            
            
        Jos listaa ei ole annettu, kaytetaan oletusarvoja.
        '''
        
        if valit == []:
            valit = [1,16,31,46,61,self.__MAXNRO]
        
        #alustetaan arvottavien lukujen lista
        arvottavat_luvut = [0] * len(valit) # = 5  Siis listaan tulee 5 listaa.
        
        for i in range(len(valit)-1):
            
            arvottavat_luvut[i] = [0] * (valit[i+1]-valit[i])  #esim. 16-1 = 15
            
            
            for n in range(valit[i+1]-valit[i]):
                arvottavat_luvut[i][n] = n + valit[i]
                
                #arvottavat_luvut on siis muotoa
                #[[1,2,3,...,v_1], [v_1+1, v_1+2, ...,v_2], ..., [v_(k-1)+1, v_(k-1)+2, ...,v_k]]
                
        
        #arvotaan valitut luvut valeilta
        #iteroidaan lista sarake kerrallaan
        
        for j in range(self.__RIVIN_PITUUS):
            for i in range(self.__SARAKKEEN_PITUUS):
                arvottu_nro = random.choice(arvottavat_luvut[j])    #arvottu luku valitaan kyseisen sarakkeen
                                                                    #sallituista arvoista
                self.numerot[i][j] = arvottu_nro
                arvottavat_luvut[j].remove(arvottu_nro)
                
        return self.numerot
        
        
                
    def tulosta(self):
        
        for rivi in self.numerot:
            print('{:2} {:2} {:2} {:2} {:2}'.format(rivi[0], rivi[1], rivi[2], rivi[3], rivi[4]))
            

        


