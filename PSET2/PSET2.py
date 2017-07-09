#PS2.a
#Start time:1.31 PM (25/06/17)
#End time: 2:49 PM (25/06/2017)
def evaluate_poly(poly, x):
    sum = 0;
    poly_length = len(poly)
    for i in range (0, poly_length):       
        sum = sum + (poly[i] * (x ** i))
    print('Original Polynomial: ', end='');
    for i in range (poly_length-1, -1, -1):
        print (poly[i], 'x^', i, ' + ', sep='', end='') 
    print ("\nResult:", sum)
#PS2.b
#Start time: 3:22 PM (25/06/17)
#End time: 3:52 PM (25/06/17)
def compute_deriv(poly):
    new_poly = []
    poly_length = len(poly)
    for i in range (poly_length - 1, -1, -1):
        new_poly += (poly[i] * i, )
    del new_poly[-1]
    new_poly.reverse()
    new_poly_length = len(new_poly)
    print('Derivatived Polynomial: ', end='');
    for i in range (new_poly_length - 1, -1, -1):
        print (new_poly[i], 'x^', i, ' + ', sep='', end='')
    print ("\nDone")


poly = (-13.39, 0.0, 17.5, 3.0, 1.0) 
x = - 13;
evaluate_poly(poly, x)
compute_deriv(poly)
##Copyright Joeslie 2016
