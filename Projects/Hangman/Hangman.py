import random

li_food = ["chicken", "banana", "fish", "pizza", "lemon", "bread", "jam", "cheese", "butter", "onion"]

a = random.choice(li_food)

li_1 = ""

turn = 9



while True:
    question = input("enter the word: ")
    li_1 += question
    if question not in a:
        turn -= 1
        print(f"your chance is {turn}")
        print("you chose wrong!")
    if turn == 8 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||                  
             ||                
             ||              
             ||               
             ||              
             ||     
        _____||_____""")
    if turn == 7 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||                
             ||              
             ||               
             ||              
             ||     
        _____||_____""")
    if turn == 6 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||                   
             ||                   
             ||              
             ||     
        _____||_____""")
    if turn == 5 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||               |
             ||               
             ||                
             ||     
        _____||_____""")
    if turn == 4 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|
             ||               
             ||              
             ||     
        _____||_____""")
    if turn == 3 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               
             ||             
             ||     
        _____||_____""")
    if turn == 2 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               |
             ||              
             ||     
        _____||_____""")
    if turn == 1 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               |
             ||              /
             ||     
        _____||_____""")
    if turn == 0:
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               |
             ||              / \\
             ||     
        _____||_____""")
        print("you lose")
        break
    counter = 0
    for i in a:
        if i in li_1:
            print(i, end=" ")
        else:
            print("_", end=" ")
            counter += 1
    if counter == 0:
        print("you win")
        break

