def catalan(n=None):
    if n != None:
        if n == 0:
            return
        seznam = [1]
        yield 1
        for j in range(1, n):
            vsota = 0
            for i in range(j):
                vsota += seznam[i] * seznam[-i-1]
            seznam.append(vsota)
            yield vsota
    else:
        k = 1
        seznam = [1]
        yield 1
        while True:
            vsota = 0
            for i in range(k):
                vsota += seznam[i] * seznam[-i - 1]
            seznam.append(vsota)
            yield vsota
            k += 1

class Oseba:
    def __init__(self, ime):
        Oseba.ime = ime
        Oseba.meritve = []

    def dodaj_meritev(self, dan, teza):
        self.meritve.append((dan, teza))

    def teza_na_dan(self, dan):
        if len(self.meritve) == 0:
            return None
        if self.meritve[-1][0] < dan:
            return self.meritve[-1][1]
        if self.meritve[0][0] > dan:
            return self.meritve[0][1]
        tezaprej = 0
        danprej = 0
        tezapotem = 0
        danpotem = 0
        for (dan1, teza1) in self.meritve:
            if dan1 == dan:
                return teza1
            elif dan1 < dan:
                tezaprej = teza1
                danprej = dan1
            elif tezapotem == 0 and dan1 > dan:
                tezapotem = teza1
                danpotem = dan1
        teza2 = dan*((tezapotem - tezaprej)/(danpotem-danprej)) + danprej
        return teza2


def najrezji_prostovoljec(ime_datoteke, dan):
    seznam = preberi_podatke(ime_datoteke)
    pass

def preberi_podatke(ime_datoteke):
    with open(ime_datoteke, 'r') as f:
        prostovoljci = f.readlines()
    return prostovoljci

class Polinom:
    def __init__(self, slovar={}):
        self.slovar = slovar

    def __repr__(self):
        return str(self.slovar)

    def vrednost(self, točka):
        pass

class Utez:
    def __init__(self, masa):
        self.masa = masa

class Skripec:
    def __init__(self, nabor):
        self.sistem = nabor