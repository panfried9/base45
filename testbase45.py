import base45


a = base45.base45()

teststring = "Hello!!My Name is @#$%^&*()_+\":I'm Python & Perl type of Guy in -+\'"
out = a.decode(a.encode(teststring))

print("IN :" + teststring )
print("OUT:" + out )  

