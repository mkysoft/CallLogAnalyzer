#CallLogAnalyzer v0.5
#mkysoft@gmail.com
import appuifw
import logs
import time
#operatör ön kodlarım
mysbk = ['50', '55']
txtfile = open('e:\\Python\\CallLogAnalyzerMy.txt','r')
mysbkist = txtfile.readlines()
txtfile.close()
txtfile = open('e:\\Python\\CallLogAnalyzerDgr.txt','r')
dgrist = txtfile.readlines()
txtfile.close()
#fatura günüm
myftrdy = 23
clllgs = logs.calls(mode='out')
myht = 0
dgr = 0
for line in clllgs:
    bas = len(line['number']) - 10
    num = line['number'][bas:bas+10]
    if bas < 1:
        sbk = '00'
    else:     
        sbk = line['number'][bas:bas + 2]
    sure = int(line['duration'])
    if (sbk in mysbk and num not in mysbkist) or sbk in dgrist:
        myht=myht+sure
    else:    
        dgr = dgr + sure
msg='Konuşma Süreleri\n'
msg=msg+'-------------------------\n'
msg=msg+'Şbk içi: %d dak %d sn\nŞbk dışı: %d dak %d sn' % (myht/60, myht % 60, dgr/60, dgr % 60)
appuifw.note(msg.decode('u8'), 'info')