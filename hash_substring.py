#Andrejs Vasiljevs 12 grupa 221RDB441

def read_input():
   
    inp = input()
    
    if "I" in inp:
        
        pattern = input()
        text = input()   
    elif "F" in inp:
        
        with open ( "./tests/06" ) as file:   
            
            pattern = file.readline()
            text = file.readline()  
            
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    patlen = len( pattern )
    texlen = len( text )
    hp = ht = 0
    rez = 1
    arr = []
    B = 13
    Q = 256
    
    for i in range ( patlen ):
        
        ht = ( ht * B + ord( text[i] )) % Q
        hp = ( hp * B + ord( pattern[i] )) % Q        

    for i in range( patlen - 1):
        
        rez = ( rez * B ) % Q
        
    for i in range( texlen - patlen + 1 ):
        
        if ht == hp:
            
            for j in range( patlen ):
                
                if pattern[j] != text[i + j]:
                    
                    break
            else:
                
                arr.append( i )
        if i < texlen - patlen:
            
            ht = ( B * ( ht - ord( text[i] ) * rez ) + ord( text[i + patlen] )) % Q
            
    return arr    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
