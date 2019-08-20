x= ("sachin", "vishwakarma", "construal")
for i in x:
    print("his name is", i,)

def my_print (*team):
    for item in team:
        print("this team is comprised of", item)

my_print("sachin", "vishwakarma", "construality")