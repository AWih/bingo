'''
Created on 2.5.2016

@author: Alvar
'''

from bingolappu import bingolappu


'''
Testailua:
-----------
lappu = bingolappu()
lappu.tulosta()

lappu.arvo_numerot('tavallinen')
lappu.tulosta()


i = 0
while i < 10:
    lappu = bingolappu()
    lappu.arvo_numerot('tavallinen')
    lappu.tulosta()
    
    i += 1
    
'''
def tulosta_tila(lappujen_maara, arvontamoodi):
    moodit = ['tavallinen', 'sarakkeet']
    
    if arvontamoodi not in moodit:
        arvontamoodi = 'ei_maaritelty'
    print('Valinnat:')
    print('Lappujen maara:', lappujen_maara)
    print('Arvontamoodi:', arvontamoodi)

    
def main():
    
    lappujen_maara = 0
    arvontamoodi = ''
    lopeta = False
    print('Bingontulostusohjelma')
    print('---------------------\n')
        
    while lopeta == False:
        
        tulosta_tila(lappujen_maara, arvontamoodi)
        print('1 Tulosta lappu')
        print('2 Valinnat')
        print('3 Lopeta')
        syote = input()
        syote = syote.strip()
        
        loop1 = False
        loop2 = False
        
        if syote == '1':
            loop1 = True
        elif syote == '2':
            loop2 = True
        elif syote == '3':
            lopeta = True
        else:
            print()
            
            
        while loop1 == True:
            kerrat = 0
            while kerrat < lappujen_maara:
                
                lappu = bingolappu()
                lappu.arvo_numerot(arvontamoodi)
                
                print('')
                lappu.tulosta()
                print('')
                
                kerrat += 1
            loop1 = False
        
        
            
        while loop2 == True:
            syote = '0'
            print('\n---------------------------')
            tulosta_tila(lappujen_maara, arvontamoodi)
            
            print('1 Valitse ruudukoiden maara')
            print('2 Valitse arvontamoodi')
            print('3 Takaisin')
            syote = input()
            
            if syote == '1':
                lappujen_maara = int(input('Ruudukoiden maara:'))
            if syote == '2':
                arvontamoodi = input('Arvontamoodi:[\'tavallinen\']/[\'sarakkeet\']')
            if syote == '3':
                loop2 = False
        
main()
            
            
        