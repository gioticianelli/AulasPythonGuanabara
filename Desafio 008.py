dis_metro = float(input('Digite uma distância em metros: '))
print('A distancia de {} metros, correspode a'.format(dis_metro))

km = dis_metro / 1000
hm = dis_metro / 100
dam = dis_metro / 10
dm = dis_metro * 10
cm = dis_metro * 100
mm = dis_metro * 1000

print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
