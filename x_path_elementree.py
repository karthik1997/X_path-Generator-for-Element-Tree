from xml.etree import ElementTree as ET
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-x", "--xml", help = "Path to the XML",default='./test_xml/karthik.xml')
args = vars(ap.parse_args())
class XpathGenerator():
    #the function iteratively checks the root and child tags and returns the xpath for the same
    def __init__(self):
        #setting a variable for the repeated tag handling 
        #setting the counter for the notation
        self.temp=''
        self.c=2
    def getpath(self,root, tag=None, path=None):
        if tag is None or root.tag == tag:
            yield path
        for child in root:
            if child.tag==self.temp:
                child_path_set = f"{path}/{child.tag}{[self.c]}"
                self.c+=1
            else:
                child_path_set = f"{path}/{child.tag}"
            self.temp=child.tag
            for child_path in self.getpath(child, tag, path=child_path_set):
                yield child_path
XMLfile= ET.parse(args["xml"])
root=XMLfile.getroot()
XG=XpathGenerator()
for path in XG.getpath(root,path = '/'+root.tag):
    print(path)
