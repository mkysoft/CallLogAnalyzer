#CallLogAnalyzer v0.2
#mkysoft@gmail.com
import appuifw
import logs
import time
#operatör ön kodlarım
mysbk = ['50', '55']
#fatura günüm
myftrdy = 23
clllgs = logs.calls(mode='out')
myht = 0
dgr = 0
for line in clllgs:
    bas = len(line['number']) - 11
    if bas < 1:
        sbk = '53'
    else:     
        sbk = line['number'][bas:bas + 2]
    sure = int(line['duration'])   
    if sbk not in mysbk:
        dgr = dgr + sure
    else:
        myht = myht + sure
msg='Konuşma Süreleri\nŞbk içi: %d dak %d sn\nŞbk dışı: %d dak %d sn' % (myht/60, myht % 60, dgr/60, dgr % 60)
appuifw.note(msg.decode('u8'), 'info')
