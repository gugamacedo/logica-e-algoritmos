def leia_dinheiro(valor):
    ok = False
    while ok == False:
        val = str(input(valor)).replace(',', '.').replace(' ', '')
        if val.isalpha() == False and val != '':
            ok = True
            return float(val)
