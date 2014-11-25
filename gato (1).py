# coding: utf8
    
def GetTablero():
    global a
    template1= ('  '+str(a[0])+' │  '+str(a[1])+' │  '+str(a[2])+'  │  '+str(a[9])+' │ '+str(a[10])+' │ '+str(a[11])+'  │  '+str(a[18])+' │ '+str(a[19])+' │ '+str(a[20])+'\n────┼────┼──── │ ────┼────┼──── │ ────┼────┼────\n''  '+str(a[3])+' │  '+str(a[4])+' │  '+str(a[5])+'  │  '+str(a[12])+' │ '+str(a[13])+' │ '+str(a[14])+'  │  '+str(a[21])+' │ '+str(a[22])+' │ '+str(a[23])+'\n────┼────┼──── │ ────┼────┼──── │ ────┼────┼────\n''  '+str(a[6])+' │  '+str(a[7])+' │  '+str(a[8])+'  │  '+str(a[15])+' │ '+str(a[16])+' │ '+str(a[17])+'  │  '+str(a[24])+' │ '+str(a[25])+' │ '+str(a[26]))
    template2= (' '+str(a[27])+' │ '+str(a[28])+' │ '+str(a[29])+'  │  '+str(a[36])+' │ '+str(a[37])+' │ '+str(a[38])+'  │  '+str(a[45])+' │ '+str(a[46])+' │ '+str(a[47])+'\n────┼────┼──── │ ────┼────┼──── │ ────┼────┼────\n'' '+str(a[30])+' │ '+str(a[31])+' │ '+str(a[32])+'  │  '+str(a[39])+' │ '+str(a[40])+' │ '+str(a[41])+'  │  '+str(a[48])+' │ '+str(a[49])+' │ '+str(a[50])+'\n────┼────┼──── │ ────┼────┼──── │ ────┼────┼────\n'' '+str(a[33])+' │ '+str(a[34])+' │ '+str(a[35])+'  │  '+str(a[42])+' │ '+str(a[43])+' │ '+str(a[44])+'  │  '+str(a[51])+' │ '+str(a[52])+' │ '+str(a[53]))
    template3= (' '+str(a[54])+' │ '+str(a[55])+' │ '+str(a[56])+'  │  '+str(a[63])+' │ '+str(a[64])+' │ '+str(a[65])+'  │  '+str(a[72])+' │ '+str(a[73])+' │ '+str(a[74])+'\n────┼────┼──── │ ────┼────┼──── │ ────┼────┼────\n'' '+str(a[57])+' │ '+str(a[58])+' │ '+str(a[59])+'  │  '+str(a[66])+' │ '+str(a[67])+' │ '+str(a[68])+'  │  '+str(a[75])+' │ '+str(a[76])+' │ '+str(a[77])+'\n────┼────┼──── │ ────┼────┼──── │ ────┼────┼────\n'' '+str(a[60])+' │ '+str(a[61])+' │ '+str(a[62])+'  │  '+str(a[69])+' │ '+str(a[70])+' │ '+str(a[71])+'  │  '+str(a[78])+' │ '+str(a[79])+' │ '+str(a[80]))
    tablero=(template1+"\n───────────────┼────────────────┼───────────────\n"+template2+"\n───────────────┼────────────────┼───────────────\n"+template3)
    return tablero

def JuegoContinua():
    global a, final
    if (t1== 'XXXXXXXXX') and (t2== ' X X X X X X X X X') and (t3== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t4== ' X X X X X X X X X') and (t5== ' X X X X X X X X X') and (t6== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t7== ' X X X X X X X X X') and (t8== ' X X X X X X X X X') and (t9== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t1== 'XXXXXXXXX') and (t4== ' X X X X X X X X X') and (t7== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t2== ' X X X X X X X X X') and (t5== ' X X X X X X X X X') and (t8== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t3== ' X X X X X X X X X') and (t6== ' X X X X X X X X X') and (t9== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t1== 'XXXXXXXXX') and (t5== ' X X X X X X X X X') and (t9== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t3== ' X X X X X X X X X') and (t5== ' X X X X X X X X X') and (t7== ' X X X X X X X X X'):
        final='X'
        return False
    elif (t1== 'OOOOOOOOO') and (t2== ' O O O O O O O O O') and (t3==' O O O O O O O O O'):
        final='O'
        return False
    elif (t4== ' O O O O O O O O O') and (t5== ' O O O O O O O O O') and (t6== ' O O O O O O O O O'):
        final='O'
        return False
    elif (t7== ' O O O O O O O O O') and (t8== ' O O O O O O O O O') and (t9== ' O O O O O O O O O'):
        final='O'
        return False
    elif (t1== 'OOOOOOOOO') and (t4== ' O O O O O O O O O') and (t7== ' O O O O O O O O O'):
        final='O'
        return False
    elif (t2== ' O O O O O O O O O') and (t5== ' O O O O O O O O O') and (t8== ' O O O O O O O O O'):
        final='O'
        return False
    elif (t3== ' O O O O O O O O O') and (t6== ' O O O O O O O O O') and (t9== ' O O O O O O O O O'):
        final='O'
        return False
    elif (t1== 'OOOOOOOOO') and (t5== ' O O O O O O O O O') and (t9== ' O O O O O O O O O'):
        final='O'
        return False
    elif (t3== ' O O O O O O O O O') and (t5== ' O O O O O O O O O') and (t7== ' O O O O O O O O O'):
        final='O'
        return False
    elif a[0]!='1' and a[1]!='2' and a[2]!='3' and a[3]!='4' and a[4]!='5' and a[5]!='6' and a[6]!='7' and a[7]!='8' and a[8]!='9' and a[9]!='10' and a[10]!='11' and a[11]!='12' and a[12]!='13' and a[13]!='14' and a[14]!='15' and a[15]!='16' and a[16]!='17' and a[17]!='18' and a[18]!='19' and a[19]!='20' and a[20]!='21' and a[21]!='22' and a[22]!='23' and a[23]!='24' and a[24]!='25' and a[25]!='26' and a[26]!='27' and a[27]!='28' and a[28]!='29' and a[29]!='30' and a[30]!='31' and a[31]!='32' and a[32]!='33' and a[33]!='34' and a[34]!='35' and a[35]!='36' and a[36]!='37' and a[37]!='38' and a[38]!='39' and a[39]!='40' and a[40]!='41' and a[41]!='42' and a[42]!='43' and a[43]!='44' and a[44]!='45' and a[45]!='46' and a[46]!='47' and a[47]!='48' and a[48]!='49' and a[49]!='50' and a[50]!='51' and a[51]!='52' and a[52]!='53' and a[53]!='54' and a[54]!='55' and a[55]!='56' and a[56]!='57' and a[57]!='58' and a[58]!='59' and a[59]!='60' and a[60]!='61' and a[61]!='62' and a[62]!='63' and a[63]!='64' and a[64]!='65' and a[65]!='66' and a[66]!='67' and a[67]!='68' and a[68]!='69' and a[69]!='70' and a[70]!='71' and a[71]!='72' and a[72]!='73' and a[73]!='74' and a[74]!='75' and a[75]!='76' and a[76]!='77' and a[77]!='78' and a[78]!='79' and a[79]!='80' and a[80]!='81':
        final='A'
        return False
    else:
        return True
    
def IntentarTirada(casilla):
    global x,a,t1,t2,t3,t4,t5,t6,t7,t8,t9
    if casilla>81 or casilla<1:
        return('La tirada debe de estar entre 1 y 81')
    elif a[casilla-1]=='X' or a[casilla-1]=='O' or a[casilla-1]==' X' or a[casilla-1]==' O':
        return ('La casilla ya esta ocupada')
    else:
        if x%2==0:
            if casilla>9:
                a[casilla-1]=' X'
            else:
                a[casilla-1]='X'
        else:
            if casilla>9:
                a[casilla-1]=' O'
            else:
                a[casilla-1]='O'
                
        t1=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
        t2=a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]
        t3=a[18]+a[19]+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
        t4=a[27]+a[28]+a[29]+a[30]+a[31]+a[32]+a[33]+a[34]+a[35]
        t5=a[36]+a[37]+a[38]+a[39]+a[40]+a[41]+a[42]+a[43]+a[44]
        t6=a[45]+a[46]+a[47]+a[48]+a[49]+a[50]+a[51]+a[52]+a[53]
        t7=a[54]+a[55]+a[56]+a[57]+a[58]+a[59]+a[60]+a[61]+a[62]
        t8=a[63]+a[64]+a[65]+a[66]+a[67]+a[68]+a[69]+a[70]+a[71]
        t9=a[72]+a[73]+a[74]+a[75]+a[76]+a[77]+a[78]+a[79]+a[80]
        
        x+=1
        msge=''
        if (t1!= 'XXXXXXXXX')and((a[0]+a[1]+a[2]=='XXX')or (a[3]+a[4]+a[5]=='XXX')or(a[6]+a[7]+a[8]=='XXX') or (a[0]+a[3]+a[6]=='XXX')or(a[1]+a[4]+a[7]=='XXX')or(a[2]+a[5]+a[8]=='XXX')or(a[0]+a[4]+a[8]=='XXX')or(a[2]+a[4]+a[6]=='XXX')):
            a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]='X','X','X','X','X','X','X','X','X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif (t1!= 'OOOOOOOOO')and((a[0]+a[1]+a[2]=='OOO')or(a[3]+a[4]+a[5]=='OOO')or(a[6]+a[7]+a[8]=='OOO')or(a[0]+a[3]+a[6]=='OOO')or(a[1]+a[4]+a[7]=='OOO')or(a[2]+a[5]+a[8]=='OOO')or(a[0]+a[4]+a[8]=='OOO')or(a[2]+a[4]+a[6]=='OOO')):
            a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]='O','O','O','O','O','O','O','O','O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t1!= 'XXXXXXXXX')and(a[0]!='1' and a[1]!='2' and a[2]!='3' and a[3]!='4' and a[4]!='5' and a[5]!='6' and a[6]!='7' and a[7]!='8' and a[8]!='9'):
            a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]='1','2','3','4','5','6','7','8','9'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t2!= ' X X X X X X X X X')and((a[9]+a[10]+a[11]==' X X X')or (a[12]+a[13]+a[14]==' X X X')or(a[15]+a[16]+a[17]==' X X X') or (a[9]+a[12]+a[15]==' X X X')or(a[10]+a[13]+a[16]==' X X X')or(a[11]+a[14]+a[17]==' X X X')or(a[9]+a[13]+a[17]==' X X X')or(a[11]+a[13]+a[15]==' X X X')):
            a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17]=' X',' X',' X',' X',' X',' X',' X',' X', ' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif(t2!= ' O O O O O O O O O')and ((a[9]+a[10]+a[11]==' O O O')or(a[12]+a[13]+a[14]==' O O O')or(a[15]+a[16]+a[17]==' O O O')or(a[9]+a[12]+a[15]==' O O O')or(a[10]+a[13]+a[16]==' O O O')or(a[11]+a[14]+a[17]==' O O O')or(a[9]+a[13]+a[17]==' O O O')or(a[11]+a[13]+a[15]==' O O O')):
            a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17]=' O',' O',' O',' O',' O',' O',' O',' O', ' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t2!= ' X X X X X X X X X')and(a[9]!='10' and a[10]!='11' and a[11]!='12' and a[12]!='13' and a[13]!='14' and a[14]!='15' and a[15]!='16' and a[16]!='17' and a[17]!='18'):
            a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17]='10','11','12','13','14','15','16','17','18'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t3!= ' X X X X X X X X X')and((a[18]+a[19]+a[20]==' X X X')or (a[21]+a[22]+a[23]==' X X X')or(a[24]+a[25]+a[26]==' X X X') or (a[18]+a[21]+a[24]==' X X X')or(a[19]+a[22]+a[25]==' X X X')or(a[20]+a[23]+a[26]==' X X X')or(a[18]+a[22]+a[26]==' X X X')or(a[20]+a[22]+a[24]==' X X X')):
            a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif (t3!= ' O O O O O O O O O')and((a[18]+a[19]+a[20]==' O O O')or(a[21]+a[22]+a[23]==' O O O')or(a[24]+a[25]+a[26]==' O O O')or(a[18]+a[21]+a[24]==' O O O')or(a[19]+a[22]+a[25]==' O O O')or(a[20]+a[23]+a[26]==' O O O')or(a[18]+a[22]+a[26]==' O O O')or(a[20]+a[22]+a[24]==' O O O')):
            a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t3!= ' X X X X X X X X X')and(a[18]!='19' and a[19]!='20' and a[20]!='21' and a[21]!='22' and a[22]!='23' and a[23]!='24' and a[24]!='25' and a[25]!='26' and a[26]!='27'):
            a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26]='19','20','21','22','23','24','25','26','27'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t4!= ' X X X X X X X X X')and ((a[27]+a[28]+a[29]==' X X X')or (a[30]+a[31]+a[32]==' X X X')or(a[33]+a[34]+a[35]==' X X X') or (a[27]+a[30]+a[33]==' X X X')or(a[28]+a[31]+a[34]==' X X X')or(a[29]+a[32]+a[35]==' X X X')or(a[27]+a[31]+a[35]==' X X X')or(a[29]+a[31]+a[33]==' X X X')):
            a[27],a[28],a[29],a[30],a[31],a[32],a[33],a[34],a[35]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif (t4!= ' O O O O O O O O O')and ((a[27]+a[28]+a[29]==' O O O')or(a[30]+a[31]+a[32]==' O O O')or(a[33]+a[34]+a[35]==' O O O')or(a[27]+a[30]+a[33]==' O O O')or(a[28]+a[31]+a[34]==' O O O')or(a[29]+a[32]+a[35]==' O O O')or(a[27]+a[31]+a[35]==' O O O')or(a[29]+a[31]+a[33]==' O O O')):
            a[27],a[28],a[29],a[30],a[31],a[32],a[33],a[34],a[35]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t4!= ' X X X X X X X X X')and(a[27]!='28' and a[28]!='29' and a[29]!='30' and a[30]!='31' and a[31]!='32' and a[32]!='33' and a[33]!='34' and a[34]!='35' and a[35]!='36'):
            a[27],a[28],a[29],a[30],a[31],a[32],a[33],a[34],a[35]='28','29','30','31','32','33','34','35','36'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t5!= ' X X X X X X X X X')and  ((a[36]+a[37]+a[38]==' X X X')or (a[39]+a[40]+a[41]==' X X X')or(a[42]+a[43]+a[44]==' X X X') or (a[36]+a[39]+a[42]==' X X X')or(a[37]+a[40]+a[43]==' X X X')or(a[38]+a[41]+a[44]==' X X X')or(a[36]+a[40]+a[44]==' X X X')or(a[38]+a[40]+a[42]==' X X X')):
            a[36],a[37],a[38],a[39],a[40],a[41],a[42],a[43],a[44]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif(t5!= ' O O O O O O O O O')and ((a[36]+a[37]+a[38]==' O O O')or(a[39]+a[40]+a[41]==' O O O')or(a[42]+a[43]+a[44]==' O O O')or(a[36]+a[39]+a[42]==' O O O')or(a[37]+a[40]+a[43]==' O O O')or(a[38]+a[41]+a[44]=='O O O')or(a[36]+a[40]+a[44]==' O O O')or(a[38]+a[40]+a[42]==' O O O')):
            a[36],a[37],a[38],a[39],a[40],a[41],a[42],a[43],a[44]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t5!= ' X X X X X X X X X')and(a[36]!='37' and a[37]!='38' and a[38]!='39' and a[39]!='40' and a[40]!='41' and a[41]!='42' and a[42]!='43' and a[43]!='44' and a[44]!='45'):
            a[36],a[37],a[38],a[39],a[40],a[41],a[42],a[43],a[44]='37','38','39','40','41','42','43','44','45'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t6!= ' X X X X X X X X X')and((a[45]+a[46]+a[47]==' X X X')or (a[48]+a[49]+a[50]==' X X X')or(a[51]+a[52]+a[53]==' X X X') or (a[45]+a[48]+a[51]==' X X X')or(a[46]+a[49]+a[52]==' X X X')or(a[47]+a[50]+a[53]==' X X X')or(a[45]+a[49]+a[53]==' X X X')or(a[47]+a[49]+a[51]==' X X X')):
            a[45],a[46],a[47],a[48],a[49],a[50],a[51],a[52],a[53]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif(t6!= ' O O O O O O O O O')and ((a[45]+a[46]+a[47]==' O O O')or(a[48]+a[49]+a[50]==' O O O')or(a[51]+a[52]+a[53]==' O O O')or(a[45]+a[48]+a[51]==' O O O')or(a[46]+a[49]+a[52]==' O O O')or(a[47]+a[50]+a[53]==' O O O')or(a[45]+a[49]+a[53]==' O O O')or(a[47]+a[49]+a[51]==' O O O')):
            a[45],a[46],a[47],a[48],a[49],a[50],a[51],a[52],a[53]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t6!= ' X X X X X X X X X')and(a[45]!='46' and a[46]!='47' and a[47]!='48' and a[48]!='49' and a[49]!='50' and a[50]!='51' and a[51]!='52' and a[52]!='53' and a[53]!='54'):
            a[45],a[46],a[47],a[48],a[49],a[50],a[51],a[52],a[53]='46','47','48','49','50','51','52','53','54'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t7!= ' X X X X X X X X X')and((a[54]+a[55]+a[56]==' X X X')or (a[57]+a[58]+a[59]==' X X X')or(a[60]+a[61]+a[62]==' X X X') or (a[54]+a[57]+a[60]==' X X X')or(a[55]+a[58]+a[61]==' X X X')or(a[56]+a[59]+a[62]==' X X X')or(a[54]+a[58]+a[62]==' X X X')or(a[56]+a[58]+a[60]==' X X X')):
            a[54],a[55],a[56],a[57],a[58],a[59],a[60],a[61],a[62]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif(t7!= ' O O O O O O O O O')and((a[54]+a[55]+a[56]==' O O O')or(a[57]+a[58]+a[59]==' O O O')or(a[60]+a[61]+a[62]==' O O O')or(a[54]+a[57]+a[60]==' O O O')or(a[55]+a[58]+a[61]==' O O O')or(a[56]+a[59]+a[62]==' O O O')or(a[54]+a[58]+a[62]==' O O O')or(a[56]+a[58]+a[60]==' O O O')):
            a[54],a[55],a[56],a[57],a[58],a[59],a[60],a[61],a[62]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t7!= ' X X X X X X X X X')and(a[54]!='55' and a[55]!='56' and a[56]!='57' and a[57]!='58' and a[58]!='59' and a[59]!='60' and a[60]!='61' and a[61]!='62' and a[62]!='63'):
            a[54],a[55],a[56],a[57],a[58],a[59],a[60],a[61],a[62]='55','56','57','58','59','60','61','62','63'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t8!= ' X X X X X X X X X')and ((a[63]+a[64]+a[65]==' X X X')or (a[66]+a[67]+a[68]==' X X X')or(a[69]+a[70]+a[71]==' X X X') or (a[63]+a[66]+a[69]==' X X X')or(a[64]+a[67]+a[70]==' X X X')or(a[65]+a[68]+a[71]==' X X X')or(a[63]+a[67]+a[71]==' X X X')or(a[65]+a[67]+a[69]==' X X X')):
            a[63],a[64],a[65],a[66],a[67],a[68],a[69],a[70],a[71]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif(t8!= ' O O O O O O O O O')and ((a[63]+a[64]+a[65]==' O O O')or(a[66]+a[67]+a[68]==' O O O')or(a[69]+a[70]+a[71]==' O O O')or(a[63]+a[66]+a[69]==' O O O')or(a[64]+a[67]+a[70]==' O O O')or(a[65]+a[68]+a[71]==' O O O')or(a[63]+a[67]+a[71]==' O O O')or(a[65]+a[67]+a[69]==' O O O')):
            a[63],a[64],a[65],a[66],a[67],a[68],a[69],a[70],a[71]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t8!= ' X X X X X X X X X')and(a[63]!='64' and a[64]!='65' and a[65]!='66' and a[66]!='67' and a[67]!='68' and a[68]!='69' and a[69]!='70' and a[70]!='71' and a[71]!='72'):
            a[63],a[64],a[65],a[66],a[67],a[68],a[69],a[70],a[71]='64','65','66','67','68','69','70','71','72'
            msge= ("Juego empatado, comienza de nuevo. :(")
        if (t9!= ' X X X X X X X X X')and ((a[72]+a[73]+a[74]==' X X X')or (a[75]+a[76]+a[77]==' X X X')or(a[78]+a[79]+a[80]==' X X X') or (a[72]+a[75]+a[78]==' X X X')or(a[73]+a[76]+a[79]==' X X X')or(a[74]+a[77]+a[80]==' X X X')or(a[72]+a[76]+a[80]==' X X X')or(a[74]+a[76]+a[78]==' X X X')):
            a[72],a[73],a[74],a[75],a[76],a[77],a[78],a[79],a[80]=' X',' X',' X',' X',' X',' X',' X',' X',' X'
            msge= ("Felicidades X has ganado esa casilla. weeee")
        elif(t9!= ' O O O O O O O O O')and ((a[72]+a[73]+a[74]==' O O O')or(a[75]+a[76]+a[77]==' O O O')or(a[78]+a[79]+a[80]==' O O O')or(a[72]+a[75]+a[78]==' O O O')or(a[73]+a[76]+a[79]==' O O O')or(a[74]+a[77]+a[80]==' O O O')or(a[72]+a[76]+a[80]==' O O O')or(a[74]+a[76]+a[78]==' O O O')):
            a[72],a[73],a[74],a[75],a[76],a[77],a[78],a[79],a[80]=' O',' O',' O',' O',' O',' O',' O',' O',' O'
            msge= ("Felicidades O has ganado esa casilla. weeee")
        elif (t9!= ' X X X X X X X X X')and(a[72]!='73' and a[73]!='74' and a[74]!='75' and a[75]!='76' and a[76]!='77' and a[77]!='78' and a[78]!='79' and a[79]!='80' and a[80]!='81'):
            a[72],a[73],a[74],a[75],a[76],a[77],a[78],a[79],a[80]='73','74','75','76','77','78','79','80','81'
            msge= ("Juego empatado, comienza de nuevo. :(")
    return (msge)
    
def IniciaJuego():
    global x,casilla,a,msg,t1,t2,t3,t4,t5,t6,t7,t8,t9
    x=0
    casilla=0
    msg = ""
    final=""
    a=[]
    d=0
    t1,t2,t3,t4,t5,t6,t7,t8,t9='','','','','','','','',''
    for d in range(1,82):
        y=str(d)
        a.append(y)
    return x, casilla, msg, a,t1,t2,t3,t4,t5,t6,t7,t8,t9

if __name__ == '__main__':
    global casilla,msg
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)
    if final=='A':
        print ('El juego esta empatado. :(')
    else:
        print ('Felicidades '+final+', ganaste el juego :D!')
