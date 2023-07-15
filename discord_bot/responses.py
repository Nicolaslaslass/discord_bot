import random

def handle_response(message):
    
    
    if message == 'hola':
        return 'Hola Ale, soy un robot' #meter def de cointoss
    if message == 'roll':
        return str(random.randint(1,6))
    


    
    