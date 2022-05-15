dh_arthur = float(input(''))
dh_luiz = float(input(''))
dh_pedro = float(input(''))
horas = float(input(''))
d_arthur = dh_arthur * horas
d_luiz = dh_luiz * horas
d_pedro = dh_pedro * horas
dmaximo_al = ((d_arthur + d_luiz) + abs(d_arthur - d_luiz)) / 2
dmaximo_ap = ((d_arthur + d_pedro) + abs(d_arthur - d_pedro)) / 2
dmaximo_total = ((dmaximo_al + dmaximo_ap) + abs(dmaximo_ap - dmaximo_al)) / 2
print(int(dmaximo_total))
