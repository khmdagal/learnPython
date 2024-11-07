
# All variables declared inside a function are scoped 
# within that function. One good example is below here
# inside function can access variables of the outer function
# But the outer function can not access those declared in inside function 
# like 'animal_inside_2level' can not be access inside the outer function

# ============ 
# Lexical scope in Python is a way to manage variable accessibility based on where they are defined in the code

# ============
def outer_1level_fun():
    animal_outer_1level = 'Secretary Bird'
    # print(animal_inside_2level) this line will return error
    def inside_2level_func():
        animal_inside_2level = 'Cat'
        print("from second level",animal_outer_1level)
        def inside_3level_func():
            print("from third level accessed 1 and 2 level variables", animal_outer_1level,animal_inside_2level)
        inside_3level_func()
    inside_2level_func()
outer_1level_fun()


        