import random

def tlacsachovnicu(sachovnica):             #tato funkcia je na vytlacenie sachonvici
    velkost = len(sachovnica)-1
    for i in range(len(sachovnica)):
        if i == 0:                      
            print(" ",end=" ")          
        if i == velkost:
            print(" ",end=" ")          
        else:    
            print(i%10,end=" ")             #najprv som vypisoval cisla od 0 do 'n' s odsekom
    print("")    
    for i in range(len(sachovnica)):
        if i == velkost:
            print("",end=" ")             
        else:    
            print(i%10,end=" ")
        for j in range(len(sachovnica)):    #potom som vypsoval sachovnicu
            print(sachovnica[i][j],end=" ")
        print("")
    print("\n")
    
def gensachovnicu(velkost):                 #tato funkcia je na vygenerovanie sachovnici
    stred = (velkost-1)/2
    stred = int(stred)
    hra = []
    for i in range (velkost+1):
        pom = []
        for j in range (velkost+1):         #najprv som vytvoril jednu praznu sachovnicu
            pom.append(' ')                 #ktora najprv bude obsahovat iba medzery
        hra.append(pom)


    for i in range (velkost):               #potom som vyplnil sachovnicu podla velkosti
        hra[i][stred] = 'D'                 #napjrv som vyplnil stredny stlpec a aj vedlajsie 
        hra[i][stred-1] = '*'               #toto som robil preto aby som potom mal niektore riadky na koniec hotove
        hra[i][stred+1] = '*'                
        
    for i in range (velkost):
        if (i == 0 or i == velkost-1):
            hra[i][stred] = '*'             
            hra[i][stred-1] = '*'           #tuto som vyplnil horny a dolny riadok
            hra[i][stred+1] = '*'
            
        if (i == stred):
            for k in range (velkost):       #tuto stredny
                hra[i][k] = 'D'
                
            hra[stred][stred]='X'
            hra[i][0] = '*'
            hra[i][velkost-1] = '*'
            
        if (i == stred-1 or i == stred+1):
            for k in range (velkost):      #a tuto riadky vedla stredneho
                hra[i][k] = '*'
            hra[i][stred] = 'D'         
     
        
    return hra    

def jeden_hrac(hra,velkost):              #tato funkcia je na symulovanie hry pre jedneho hraca
    stred = (velkost-1)/2
    stred = int(stred)
    hra[0][stred+1]= 'A'
    x = 0
    y = stred+1
    predX = 0
    predY = stred
    pom = 0
    tlacsachovnicu(hra)
    while(1):
        inp = 'a'
        #inp = input("Chcete pokracovat? a/n: ")
        if (inp == 'n'):
            tlacsachovnicu(hra)
            break
        else:
            hod = random.randint(1, 6)
            print("Hod kouckou bolo: ",hod ,"\n")
            konec = 0
            #hod = input("kolko: ")                        #najprv som deklaroval vsetky dolezite premenne
            #hod = int(hod)
            zaciatokX = x
            zaciatokY = y
            zaciatokPredX = predX
            zaciatokPredY = predY
            for i in range (hod):                          #najprv hrac hodi s kockou a potom bude behat jeden cyklus ktory bude behat tolko krat kolko hrac hodil
                pomX = x                                   #v jednom cykle hrac urobi jeden krok
                pomY = y
                hra[predX][predY] = 'A'
                if (x == 0 and y == stred or konec == 1):    # tento if statement je nato aby som kotroloval ze ci hrac nie je v dome
                    konec = 1                                # ked ano tak dalej bude pohnut v dome
                    x = x+1
                    if (hra[x][y] == 'X'):             
                        x = zaciatokX
                        y = zaciatokY
                        hra[predX][predY] = '*'      
                        predX = zaciatokPredX                #ked hrac je v dome tak premenna 'konec' bude mat hodnotu 1
                        predY = zaciatokPredY                #podla toho viem na konci ze hrac uz je v dome a mozem ukoncit hru
                        hra[x][y]= 'A'
                        konec = 0
                        for m in range(stred):
                            if (m == 0):
                                continue
                            hra[m][stred] = 'D'
                        break
                    hra[predX][predY] = '*'                 #na sachovnicy hrac krokovat tak ze budem hladat znamieko '*' okolo hraca (hore,dole,doprava,dolava) 
                elif (hra[x][y+1] == '*'):                  #co vzdy bude iba jeden lebo predchadzajucu poziciu hraca nebudom kontrolovat
                    y = y+1
                    hra[predX][predY] = '*'
                elif (hra[x][y-1] == '*'):
                    y = y-1
                    hra[predX][predY] = '*'
                elif (hra[x+1][y] == '*'):
                    x = x+1
                    hra[predX][predY] = '*'
                elif (hra[x-1][y] == '*'):
                    x = x-1
                    hra[predX][predY] = '*'
                predX = pomX
                predY = pomY
                hra[predX][predY] = '*'           
                hra[x][y] = 'A'                             #potom ked som rozhodol ze kam dalej a vypocital som poziciu tak vymenim si znamienko na tom pozicii na 'A'
                                                            #a znamienko na predchadzjucom si vymenim na '*'
            m = 1
            if (y == stred and x < stred):
                for m in range(stred):
                    if (m == x and y == stred or m == 0):   #tato cast je nato aby dom vyzeral ako ma na konci
                        continue
                    hra[m][stred] = 'D'
                
            tlacsachovnicu(hra)
            #print ("x =",x," y =",y)
            if (konec == 1):                                #tuto kontrolujem premennu 'konec' ked sa rovna 1 tak hra je ukoncena
                print("Hra je ukoncena !!!")
                return hra

    
            
def dve_hrace(hra):                                         #tato funkcia je na simulovanie hru pre dve hrace
    velkost = len(hra)-1                                    #funguje to takmer tak isto ako pre jednemu
    stred = (velkost-1)/2
    stred = int(stred)
    ax = 0
    ay = stred+1
    predAX = 0                                              #najprv som deklaroval vsetky premenne
    predAY = stred                                        
    bx = velkost-1
    by = stred-1
    predBX = velkost-1
    predBY = stred
    panakA = (velkost-3)/2
    panakB = (velkost-3)/2
    hra[ax][ay]= 'A'
    hra[bx][by]= 'B'
    tlacsachovnicu(hra)
    AvD = []
    BvD = []
    while(1):
#A-----------------------------------------------------------------------------
        pomA = 0
        pomB = 0
        inp = 'a'
        #inp = input("Chcete pokracovat, hrac A? a/n: ")
        if (inp == 'n'):
            print("Hra bola ukoncena !!!")
            tlacsachovnicu(hra)
            break
        else:
            hod = random.randint(1, 6)                                  #najprv ide prvy hrac (hrac A)
            print("Hod kouckou bolo pre hraca A: ",hod ,"\n")           #najprv hrac hodi s kockou a potom bude behat jeden cyklus ktory bude behat tolko krat kolko hrac hodil
            konec = 0                                                   #v jednom cykle hrac urobi jeden krok
            #hod = 1
            zaciatokX = ax
            zaciatokY = ay
            zaciatokPredAX = predAX
            zaciatokPredAY = predAY
            for i in range (hod):    
                pomAX = ax
                pomAY = ay
                hra[predAX][predAY] = 'A'
                if (ax == 0 and ay == stred or pomA == 1):             # tento if statement je nato aby som kotroloval ze ci hrac nie je v dome
                    pomA = 1                                           # ked ano tak dalej bude pohnut v dome
                    ax = ax+1
                    if (hra[ax][ay] == 'X'):
                        ax = zaciatokX                                 #ked hrac je v dome tak premenna 'pomA' bude mat hodnotu 1
                        ay = zaciatokY                                 #podla toho viem na konci ze hrac uz je v dome a mozem ukoncit hru
                        hra[predAX][predAY] = '*'                      
                        predAX = zaciatokPredAX
                        predAY = zaciatokPredAY
                        hra[ax][ay]= 'A'
                        pomA = 0                                      
                        for m in range(stred):
                            if (m == 0):
                                continue
                            hra[m][stred] = 'D'    
                        break
                    hra[predAX][predAY] = '*'
                elif (hra[ax][ay+1] == '*' ):                          #na sachovnicy hrac krokovat tak ze budem hladat znamieko '*' okolo hraca (hore,dole,doprava,dolava)
                    ay = ay+1                                          #co vzdy bude iba jeden lebo predchadzajucu poziciu hraca nebudom kontrolovat
                    hra[predAX][predAY] = '*'              
                    pomoc = 1
                elif (hra[ax][ay-1] == '*' ):
                    ay = ay-1
                    hra[predAX][predAY] = '*'
                    pomoc = 1
                elif (hra[ax+1][ay] == '*' ):
                    ax = ax+1
                    hra[predAX][predAY] = '*'
                    pomoc =1
                elif (hra[ax-1][ay] == '*' ):
                    ax = ax-1
                    hra[predAX][predAY] = '*'
                    pomoc = 1
                predAX = pomAX
                predAY = pomAY
                hra[predAX][predAY] = '*'
                hra[ax][ay] = 'A'                                     #potom ked som rozhodol ze kam dalej a vypocital som poziciu tak vymenim si znamienko na tom pozicii na 'A'
                                                                      #a znamienko na predchadzjucom si vymenim na '*'
            m = 1 
            o = 0
            if (ay == stred and ax < stred): 
                for m in range(stred):
                    if m == 0:
                        continue
                    hra[m][stred] = 'D'
                
            #print ("x =",x," y =",y)

            if (pomA == 1):                                        #tuto som ulozol do retazci tia A panaky ktore uz so v dome
               AvD.append([ax,ay])
               ax = 0
               ay = stred+1
               predAX = 0
               predAY = stred
               hra[0][stred+1]= 'A'
               pomA = 0 
            for g in range(len(AvD)):                                         
                hra[AvD[g][0]][AvD[g][1]] = 'A'
                #print("AvD: ",AvD[g][0],AvD[g][1])
            tlacsachovnicu(hra)

            pocetAvD = 0
            for pocet in range(stred):                             # tuto som spocital vsetky panaky ktre su v dome a ked su rovne k (n-3)/2 tak hrac A vyhral
                if pocet == 0:                                     # ked vsetky pankay uz su v dome tak premenym si hodnotu premennej 'konec' na 1 co znamena
                    continue                                       # ze vyhral hrac A
                if (hra[pocet][stred] == 'A'):
                    pocetAvD = pocetAvD+1
                if (pocetAvD == panakA):                           
                    konec = 1
            
            if (konec == 1):                                       #tuto kontrolujem premennu 'konec' ked sa rovna 1 tak hra je ukoncena
                print("Hra je ukoncena !!! Vyhral hrac A !!!")
                return hra
            
#B------------------------------------------------------------------------------
        pomB = 0
        inp = 'a'
        #inp = input("Chcete pokracovat, hrac B? a/n: ")                           #a potom ide druhy hrac
        if (inp == 'n'):
            print("Hra bola ukoncena !!!")                                         #druhy hrac pohibuje tak isto ako prvy len tu pracujem s inymi poziciami
            tlacsachovnicu(hra)
            break
        else:
            hod = random.randint(1, 6)
            print("Hod bolo pre hraca B: ",hod ,"\n")
            konec = 0
            #hod = 1
            zaciatokBX = bx
            zaciatokBY = by
            zaciatokPredBX = predBX
            zaciatokPredBY = predBY
            for i in range (hod):    
                pomBX = bx
                pomBY = by
                hra[predBX][predBY] = 'B'
                if (bx == velkost-1 and by == stred or pomB == 1):
                    pomB = 1
                    bx = bx-1
                    if (hra[bx][by] == 'X'):
                        bx = zaciatokBX
                        by = zaciatokBY
                        hra[predBX][predBY] = '*'
                        predBX = zaciatokPredBX
                        predBY = zaciatokPredBY
                        hra[bx][by]= 'B'
                        pomB = 0
                        m = stred+1
                        for m in range(stred):
                            #print("M: ",m)
                            if (velkost-2-m == stred):
                                continue
                            hra[velkost-2-m][stred] = 'D'
                            
                        break
                    hra[predBX][predBY] = '*'  
                elif (hra[bx-1][by] == '*'):
                    bx = bx-1
                    hra[predBX][predBY] = '*'
                    pomoc = 1
                elif (hra[bx][by+1] == '*'):
                    by = by+1
                    hra[predBX][predBY] = '*'
                    pomoc = 1
                elif (hra[bx][by-1] == '*' ):
                    by = by-1
                    hra[predBX][predBY] = '*'
                    pomoc = 1
                elif (hra[bx+1][by] == '*' ):
                    bx = bx+1
                    hra[predBX][predBY] = '*'
                    pomoc = 1
                predBX = pomBX
                predBY = pomBY
                hra[predBX][predBY] = '*'
                hra[bx][by] = 'B'
    
            m = stred+1
            o = 0
            if (by == stred and bx > stred and bx < velkost-1):
                for m in range(stred):
                    #print("M: ",m)
                    if (velkost-2-m == stred):
                        continue
                    hra[velkost-2-m][stred] = 'D'
                
            #print ("x =",x," y =",y)

            if (pomB == 1):
               BvD.append([bx,by])
               bx = velkost-1
               by = stred-1
               predBX = velkost-1
               predBY = stred
               hra[velkost-1][stred-1]= 'B'
               pomB = 0 
            for g in range(len(BvD)):
                hra[BvD[g][0]][BvD[g][1]] = 'B'
                #print("BvD: ",BvD[g][0],BvD[g][1])
            tlacsachovnicu(hra)

            pocetBvD = 0
            for pocet in range(stred):
                if pocet == 0:
                    continue
                if (hra[velkost-1-pocet][stred] == 'B'):
                    pocetBvD = pocetBvD+1
                if (pocetBvD == panakB):
                    konec = 2
            
            if (konec == 2):
                print("Hra je ukoncena !!! Vyhral hrac B !!!")
                return hra

            
def hra_clovece():                             #tato funkcia je hlavna funkcia 
    n = input("Aka velka ma byt sachovnica? ")                  
    clovece = gensachovnicu(int(n))

    tlacsachovnicu(clovece)
    #print(clovece[9][3],"___")

    typ = input("Aku hru chcete hrat? Hra pre jeden 'j', pre dvoch 'd': ")
    if (typ == 'j'):
        jeden_hrac(clovece,int(n))
    else:
        print(typ)
        dve_hrace(clovece)

hra_clovece()
