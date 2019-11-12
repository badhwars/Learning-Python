def main():
    f=open("textfile.txt","w+")


    for i in range(10):
        f.write("this is a line"  + str(i) + "\r\n")

    f.close()

main()