import colors
x = colors.color("/|\ ", 'RED')
y = colors.color('/ \ ', 'RED')
final = f'''
  _____   
 | /   |  
 |/    {colors.color('O', 'RED')}  
 |    {x}   
 |    {y}   
===         
'''

gibbet = '''
  _____   
 | /   |  
 |/      
 |       
 |       
===         
'''

stage_5 = '''
  _____   
 | /   |  
 |/    O  
 |    /|\   
 |    /    
===         
'''

stage_4 = '''
  _____   
 | /   |  
 |/    O  
 |    /|\   
 |      
===         
'''

stage_3 = '''
  _____   
 | /   |  
 |/    O  
 |    /|   
 |      
===         
'''
stage_2 = '''
  _____   
 | /   |  
 |/    O  
 |     |   
 |      
===         
'''

stage_1 = '''
  _____   
 | /   |  
 |/    O  
 |       
 |      
===         
'''

image_dict = {
    0: gibbet,
    1: stage_1,
    2: stage_2,
    3: stage_3,
    4: stage_4,
    5: stage_5,
    6: final
}