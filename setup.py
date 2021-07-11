#-------IMPORTS---------
import os
import os.path
from PIL import Image

#Displaying the name
print("Image Manipulator\n\n")

#Taking the directory
print("If image is in desktop's image folder then give input as:")
print("\Desktop\image\\")
dir=input("Enter the directory:\n")
path=os.path.expanduser('~')+dir

#Checking if path exists
if os.path.isdir(path):
    data=list()  #Creating a list for keeping items in that folder
    for image in os.listdir(path):
        data.append(image)
else:
    print("\nNo Such Directory!!")
    print("Thank you!")
    quit()


#Reading the image name
image_name=input("\nEnter the image name(photo.jpg,img.png):")

#Asking what is to be done
print("\nTasks Done:")
print("1.Rotate \n2.Resize \n3.Resize and Rotate \n4.B&W \n5.Change extension")
task=input("What would you like to do?:")
try:  #Error handling for task input
    task=int(task)
    if task==1:
        degree=int(input("\nHow many degrees you want to rotate? :"))

    elif task==2:
        width=int(input("\nEnter the width:"))
        height=int(input("Enter the height:"))

    elif task==3:
        degree=int(input("\nHow many degrees you want to rotate?:"))
        width=int(input("Enter the width:"))
        height=int(input("Enter the height:"))

    elif task==5:
        new_ext=input("\nEnter the extension(.jpg, .png, .jpeg etc):")
except:
    print("\nPlease enter an integer value.")
    print("Thank you!")
    quit()


#Doing the task if image is found in the directory
if image_name in data:
        if(task==1):  #Rotate
            img=Image.open(path+image_name)
            img.rotate(degree).save(path+image_name.split('.')[0]+"_rotated."+image_name.split('.')[1])
            print("\n\nRotated Successfully")
            img.close()

        elif(task==2): #Resize
            img=Image.open(path+image_name)
            img.resize((width,height)).save(path+image_name.split('.')[0]+"_resized."+image_name.split('.')[1])
            print("\n\nResized Successfully")
            img.close()

        elif(task==3): #Rotate and Resize
            img=Image.open(path+image_name)
            img.resize((width,height)).rotate(degree).save(path+image_name.split('.')[0]+"_new."+image_name.split('.')[1])
            print("\n\nResized and Rotated Successfully")
            img.close()

        elif(task==4): #B&W
            img=Image.open(path+image_name)
            img.convert('L').save(path+image_name.split('.')[0]+"_b&w."+image_name.split('.')[1])
            print("\n\nB&W Successful")
            img.close()

        elif(task==5): #Changing extension
            try:  #Error handling if extension cannot be changed
                img=Image.open(path+image_name)
                img.save(path+image_name.split('.')[0]+"_new"+new_ext)
                img.close()
                print("\n\nExtension Changed Successfully")
            except:
                print("\nCannot change extension")
                quit()

#If image not found in the directory
else:
    print("\n!!!Image Not Found!!!")

print("Thank you!")
