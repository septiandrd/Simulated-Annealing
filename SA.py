import random,math

def generateSolusi() :
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    solusi = [x1,x2]
    return solusi

def modify(x1,x2) :
    x1 += random.uniform(-1,1)
    x2 += random.uniform(-1,1)
    solusi = [x1, x2]
    return solusi

def hitungEnergi(x1,x2) :
    # energi = ( (4-(2.1*(x1**2))+((x1**4)/3)) * (x1**2) ) + (x1*x2) + ( (-4+4*(x2**2)) * (x2**2) )
    energi = (((2.1*(x1**2))+((x2**4)/3)) * (x1**2) ) + (-x1*x2) + ( (4*(x2**2)) * (x2**2) )
    return energi

if __name__ == '__main__':

    iterasi = 0
    maxIterasi = 500000
    t0 = 500000
    tmin = 1*10**-100
    # tmin = 0.001
    alpha = 0.995

    bestSolusi = generateSolusi()
    bestEnergi = hitungEnergi(bestSolusi[0],bestSolusi[1])

    while (t0>tmin and iterasi!=maxIterasi) :
        nextSolusi = generateSolusi()
        nextEnergi = hitungEnergi(nextSolusi[0],nextSolusi[1])
        dE = bestEnergi-nextEnergi
        if (dE>0) :
            bestSolusi = nextSolusi
            bestEnergi = nextEnergi
            print("Iterasi ke-",iterasi, ", suhu %.2f" % t0, "derajat")
            print("Solusi Terbaik : x1 = %.8f" % bestSolusi[0], " ; x2 = %.8f" % bestSolusi[1], " dengan hasil %.8f" % bestEnergi, "\n")
        else :
            p = random.random()
            pSolusiBaru = math.exp((bestEnergi-nextEnergi)/t0)

            if pSolusiBaru > p :
                bestSolusi = nextSolusi
                bestEnergi = nextEnergi

        t0 *= alpha
        iterasi += 1