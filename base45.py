

class base45:
   
  ring = [ "0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"
         , "S","T","U","V","W","X","Y","Z"," ","$","%","*","+","-",".","/",":" ]
  revring = { "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15  
         , "G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30
         , "V":31,"W":32,"X":33,"Y":34,"Z":35," ":36,"$":37,"%":38,"*":39,"+":40,"-":41,".":42,"/":43,":":44 } 

  def __init(self):
    self.ring = ring

  def encode(self, instring):
    outchar = ""
    lenin = len(instring) 
    for i in range(0, lenin, 2):
       a = int.from_bytes(bytes( instring[i], 'us-ascii'),"little") 
       if i+1 < lenin: 
          b = int.from_bytes(bytes( instring[i+1], 'us-ascii'),"little")  
          ab = int( 256 * a + b ) 
          c = divmod( ab , (45*45) ) 
          de= divmod( c[1], 45)
          outchar  += self.ring[de[1]] + self.ring[de[0]] + self.ring[c[0]] 
       else: 
          de = divmod( a , 45 )   
          outchar  += self.ring[de[1]] + self.ring[de[0]]   
    return outchar

  def decode(self, instring): 
    outchar = "" 
    lenin = len(instring) 
    for i in range(0, lenin, 3):
        a = self.revring[ instring[i] ]
        if i+1 < lenin: 
          b = self.revring[ instring[i+1] ]
        else: 
          b = 0 
        if i+2 < lenin:
          c = self.revring[ instring[i+2] ]
        else: 
          c = 0 
        group = a  + b*45 + c *45 * 45 
        b = divmod( group, 256)
        outchar += chr( b[0]) +  chr(b[1]) 
    return outchar 
 
 
