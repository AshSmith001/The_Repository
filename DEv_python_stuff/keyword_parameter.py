#keyword parameter/argument
def display(str,int_x,float):
    print("The string is  ",str)
    print("The integer is  ",int_x)
    print("The float value is ",float)

display(str = 'Dev', float = 5.78, int_x = 4)

#variable length argument
def func(name,*fav_subject):
    print("\n",name," likes to read ",)
    for sub in fav_subject:
        print(sub,end = " ")
func("Goransh","A","B")
func("Smitha","C","D","E")
func("Nayan")
#default arguments
def display_2(name, course = "BTech"):
    print("name : " + name)
    print("Course : ", course)
display_2(course = "BCA",name = "Arav")
display_2(name = "Reyansh")
#lambda functions or anonymous functions

sum = lambda x,y:x+y
print("sum = ",sum(3,5))
#documentation for multi line
"""this is a documentation line"""
