import json
user=input("singup or login:")
name=input("enter your name:")
if user=="singup":
    password=input("enter the password:")
    re_password=input("enter the password:")
    dob=input("enter DOB :")
    gender=input("your gender:")
    print("your ac has been created")
    deta={"user":user,"name":name,"password":password,"password2":re_password,"dob":dob,"gender":gender} 
    with open (name+".json","w")as f:
        b=json.dump(deta,f,indent=2) 
else:
    print("login") 
    a=open(name+".json","r")
    b=a.read()
    c=json.loads(b)
    if name==c["name"]:
        password=input("enter your paasword")
        if password==c["password"]:
            print("login successfull")
        else:
            print("password is  wrong")
    else:
        print("your name is wrong")

# import json
# a={"name":"poonam",
#    "age":16}
# b= json.dumps(a)
# print(b)