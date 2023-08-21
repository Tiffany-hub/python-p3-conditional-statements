dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."

elif dog == "thirsty":
    owner = "Refilling water bowl."
    
elif dog == "playful":
    owner = "PLaying tug-of-war."
 
elif dog == "cuddly":
    owner = "Snuggling."
    
else:
    owner = "Reading newspaper." 
    
print(owner)

def control_flow(value):
    if value:
        #if the value is truthy 
        print("yep!")
        
    else:
        #if the value is falsy
        print("nope!") 
        
control_flow(False)    
control_flow(None)  
control_flow(True)
control_flow("")
control_flow(0)
control_flow("5")
control_flow("0")                       

age = 1

if age < 2:
    is_baby = 'baby'
    
else:
    is_baby = 'not a baby'   
    
print(is_baby)   

def divide(num1, num2):
    try:
        quotient = num1/num2
        print (quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
divide(10, 2)  
divide(9, 13)  

dog = "cuddly"

dict_map = {
    "hunry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "PLaying tug-of-war.",
    "cuddly": "Snuggling.",
}            

owner = dict_map.get(dog, "Reading newspaper.")
print(owner)          