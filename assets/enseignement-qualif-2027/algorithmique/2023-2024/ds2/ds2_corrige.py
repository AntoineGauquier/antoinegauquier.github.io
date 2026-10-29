#!/usr/bin/env python3

class Polynome:
    def __init__(self, coeff = []):
        if coeff == [0]:
            coeff = []
        self._degre = len(coeff) - 1
        self._coeff = coeff

    def __getitem__(self, x):
        if(self._degre == -1):
            return 0
        return self._coeff[x]

    def __call__(self, x):
        value = 0
        for coeff in reversed(self._coeff):
            value *= x
            value += coeff
        return value

    def __str__(self):
        if self._degre == -1:
            return "0"

        l = []
        first = True
        for i in reversed(range(0, self._degre + 1)):
            if self[i] != 0:
                if first:
                    first = False
                    if self[i]<0:
                        l.append("-")
                else:
                    l.append("+" if self[i]>0 else "-")
                if i==0:
                    monomial = ""
                elif i==1:
                    monomial = "X"
                else:
                    monomial = "X^" + str(i)

                if abs(self[i])==1 and i!=0:
                    l.append(monomial)
                else:
                    l.append(str(abs(self[i])) + monomial)

        return " ".join(l)

    def __add__(self, other):
        coeff = [0 for i in range(0, max(self._degre, other._degre) + 1)]
        for i in range(0, len(coeff)):
            if(i<=self._degre):
                coeff[i] += self[i]
            if(i<=other._degre):
                coeff[i] += other[i]
        return Polynome(coeff)

    def __sub__(self, other):
        coeff = [0 for i in range(0, max(self._degre, other._degre) + 1)]
        for i in range(0, len(coeff)):
            if(i<=self._degre):
                coeff[i] += self[i]
            if(i<=other._degre):
                coeff[i] -= other[i]
        return Polynome(coeff)

    def __mul__(self, other):
        coeff = [0 for i in range(0, self._degre + other._degre + 1)]
        for i in range(0, self._degre+1):
            for j in range(0, other._degre+1):
                coeff[i+j] += \
                  self[i] * other[j]
        return Polynome(coeff)

    def algok(p, q):
        degre = max(p._degre, q._degre)
        m = -(-degre // 2)
        if(m==0):
            return Polynome([p[0]*q[0]])
        else:
            p1 = Polynome(p[0:m])
            p2 = Polynome(p[m:])
            q1 = Polynome(q[0:m])
            q2 = Polynome(q[m:])
            r1  = Polynome.algok(p1, q1)
            r2  = Polynome.algok(p2, q2)
            r12 = Polynome.algok(p1+p2,q1+q2) - r1 - r2
            coeff = [0 for i in range(0, p._degre + q._degre + 1)]
            for i in range(0, r1._degre+1):
                coeff[i] += r1[i]
            for i in range(0, r12._degre+1):
                coeff[i+m] += r12[i]
            for i in range(0, r2._degre+1):
                coeff[i+2*m] += r2[i]
            return Polynome(coeff)

P = Polynome([1,-2,1])
#print(P)
Q = Polynome([1,0,1,1])
#print(Q)
R = P-Q
S = P*Q
#print(S(42))
#print(R)

#P=Polynome([1,1])
#Q=Polynome([1,1])

print(P*Q)
print(Polynome.algok(P,Q))
