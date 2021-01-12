FLOW = 8000558
TITLE = 'chromebook A-C214-{}/279-{}'#005 #726
FV_TITLE = 5
SV_TITLE = 726
for i in range(1,5):
    Ntitle = TITLE.format(str(FV_TITLE+i).zfill(3),str(SV_TITLE+i))
    Nflow = str(FLOW+i)
    print('正在輸入\nFLOW : {} | TITLE : {} ...\n'.format(Nflow,Ntitle))
