#pip3 install pillow
from PIL import Image

n=int(input("enter the number of files : "+"\n"))

dire=input("Enter The Directory : ")

a1=input("enter the filename : "+"\n")

b1= Image.open(dire+"/"+a1)

b1=b1.convert('RGB')	

list1=[]

for i in range(n-1):
	a=input("enter the filename : "+"\n")
	b= Image.open(dire+"/"+a)
	b=b.convert('RGB')	
	im_list =list1.append(b)

confirm=input("Do You want to save this in the current Directory (y | n) : ")

if (confirm=="y") or (confirm=="Y"):
	name=input("Enter The filename to save the file (filename must be end with .pdf) : ")	
	path=dire+"/"+name

elif(confirm=="n") or (confirm=="N"):
	path=input("Enter The path with the file name to save (file name must be end with .pdf) : ")

else:
	print("Choose 'y' or 'n'\n")

pdf1_filename = path

b1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=list1)