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

poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = - 13;
evaluate_poly(poly, x)

