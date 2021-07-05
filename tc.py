def tc(mg):
    m = mg[0:9]
    g = []
    for x in str(m):
        g.append(int(x))
    s = (((g[0]+g[2]+g[4]+g[6]+g[8])*7)-(g[1]+g[3]+g[5]+g[7]))%10
    g.append(s)
    h = 0
    for x in g:
        h+= x
    h = h %10
    g.append(h)
    tot = ""
    for dd in g:
        tot += str(dd)
    if str(tot) == str(mg):
        return "T.C numarası Doğru"
    else:
        return "T.C numarası Yanlış"
print(tc(input("T.C numarası : ")))
input("Kapatmak için bir tuşa basınız...")
