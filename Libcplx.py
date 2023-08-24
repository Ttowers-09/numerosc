import math
def sumacplx (c1,c2):
    r = c1[0] + c2[0]
    i= c1[1] + c2[1]
    return (r,i)

def restacplx (c1,c2):
    r = c1[0] - c2[0]
    i= c1[1] - c2[1]
    return (r,i)

def multcplx (c1,c2):
    r = (c1[0]*c2[0]) + (-1*(c1[1]*c2[1]))
    i = (c1[0]*c2[1]) + (c1[1]*c2[0])
    return (r,i)

def divisioncplx (c1, c2):
    numr = (c1[0]*c2[0]) + (-1*(c1[1]*(-1*(c2[1]))))
    numi = (c1[0]*(-1*(c2[1])))+ (c1[1]*c2[0])
    den = (c2[0]**2) - (-1*(c2[1]**2))
    return (numr/den, numi/den)

def modulocplx (c1):
    modulo = (c1[0]**2 + c1[1]**2)**0.5
    return (modulo)
def conjugadocplx (c1):
    conj1 = c1[1]*-1

    return ((c1[0],conj1))


def cartpolarcplx(c1):
    ang = math.atan(c1[1]/c1[0])
    radio =  ((c1[0]**2)+(c1[1]**2))**0.5
    return (radio, ang)

def fasecplx (c1):
    division =  c1[1] / c1[0]
    fase = math.atan(division)
    return (fase)

if __name__ == '__main__':
    print (sumacplx ((3,2),(-5,5.2)))
    print(multcplx((3, 2), (-5, 5.2)))
    print(restacplx((3, 2), (-5, 5.2)))
    print (divisioncplx ((-4,5),(8,-2)))
    print(modulocplx ((3,2)))
    print(conjugadocplx((3, 2)))
    print(cartpolarcplx ((-9,4)))
    print(fasecplx ((3,2)))
    print("-----")
