class myClass():
    def method1(self):
        print("my class Method 1")
    
    def method2(self, somestring):
        print("my class method2" + somestring)
    

def main():

    c= myClass()
    c.method1()
    c.method2("This is a string")

    print("test")

main()