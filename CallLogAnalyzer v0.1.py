#CallLogAnalyzer v0.1
#mkysoft@gmail.com
f = file(u"e:\\log-2009-11-23.csv", "r")
f.readline()
avea = 0
dgr = 0
for line in f:
    lst = []
    lst = line.split(',')
    if lst[2] == '"Voice call"' and lst[4] == '"Outgoing"':
        bas = len(lst[9]) - 11
        if bas < 1:
            sbk = '53'
        else:     
            sbk = lst[9][bas:bas + 2]
        sure = int(lst[6][1:len(lst[6])-1])
        #print sure   
        if sbk != '55' and sbk != '50':
            dgr = dgr + sure
        else:
            avea = avea + sure   
        #print sbk, lst[9]
print 'Þebeke içi %d, dýþý %d. Toplam %d' % (avea/60, dgr/60, (avea+dgr)/60)       
f.close()