#default parameter

#def user_info(first_name, last_name, age =None): you can declare last parameter as default 
#but cannot declare first and second parameter as default

def user_info(first_name, last_name, age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
    
user_info("varun","sharma","35")
