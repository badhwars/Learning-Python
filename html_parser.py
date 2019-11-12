from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):


    def handle_comment(self,data):
     print("Encountered commenrt",data)
     pos =self.getpos()
     print("\tAt line", pos[0], "position", pos[1])
    
    def handle_starttag(self,tag,attrs):
        

    def handle_endtag(self , tag, attrs):
    



def main():
    parser= MyHTMLParser()
    f=open("samplehtml.html")
    if f.mode=='r':
        contents = f.read()
        parser.feed(contents)


main()

