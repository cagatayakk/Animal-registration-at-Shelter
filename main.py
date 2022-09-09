def register():
    print("""
   Enter the animal you want to register and its name. Press q to exit
   Please Attention to comma usage! 
   Example : dog,Ruby   or   cat,Kitty\n""")
    while True:
        register = input("   register :").lower()
        if register == "q":
            break
        with open ("shelter.txt" , "a" , encoding="utf-8") as r:
            r.write(register)
            r.write("\n")

def adopt():
    print(""" 
    Please choice a one option of the bottom  : 
    1 : Adopt  the "oldest" animal (based on arrival or addition time)
    2 : Adopt a cat 
    3 : Adopt a dog
    q : Exit   \n""")
    print()
    def remove_func():
        print('    {} adopted.'.format(remove.replace("\n"," ")))       
        with open("shelter.txt", "w", encoding="utf-8") as f:
            for i in list_shelter:
                if i != remove:
                    f.write(i)
            
    while True:
        choice=input("    choice : ")
        if choice == "q":
            break
                                    
        with open ("shelter.txt" , "r" , encoding="utf-8") as s:
            list_shelter = s.readlines()
            if choice == "1":
                remove=list_shelter[0]
                remove_func()

            for remove in list_shelter:
                index=remove.find(",")
                sliceAnimal = remove[:index]
                if choice == "2" and "cat" in sliceAnimal:
                    remove_func()
                    break
                if choice == "3" and "dog" in sliceAnimal:
                    remove_func()
                    break

register()

adopt()
