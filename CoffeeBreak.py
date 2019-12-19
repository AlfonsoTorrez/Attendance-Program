'''
    Program Name: Coffee Break
    Contributors: Alfonso Torres, Jaime Velazquez, Brittany Arnold
    Course: CST 205
    Github Repo: https://github.com/AlfonsoTorrez/CoffeeBreakTeam6
    Objective: Coffee Break is a team based project for the course CST 205 - Multimedia Design
            & Programming. The program was created to increase a user/customer base at a
            designated location.
'''
from PIL import Image
import glob
import numpy as np
import cv2
import pickle
import time
from email.headerregistry import Address
from email.message import EmailMessage
import smtplib

#Getting image directory and opening images
img_arr = glob.glob("faces/*.png")

#Getting the path of Haar Cascade file
casc_class = 'haarcascade_frontalface_default.xml'
#Loading the cascade file
face_cascade = cv2.CascadeClassifier(casc_class)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#Creating an array of images
image = [Image] * len(img_arr)
faces = [] #IN TEST DATA
labels = [] #Creating a new list

#need to use pip install
#create our LBPH face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()


def store_dict(dict):
    with open('file.txt', 'wb') as handle:
        pickle.dump(dict, handle)

def read_dict():
    with open('file.txt', 'rb') as handle:
        dict = pickle.loads(handle.read())
    
    return dict;

#Reading in my dictionary
my_info = read_dict()

# Gmail details
email_address = "coffeebreak205@gmail.com"
email_password = "givemecoffee!"


def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg


#Turning on the video to see who comes and goes
def begin_broadcast():
    num = 1
    timeout = time.time() + 60*1 #seconds the test takes
    while time.time() < timeout:
        face_stuff = []
        
        my_video = cv2.VideoCapture(0)
        #Person walking up
        while(len(face_stuff)==0 and time.time() < timeout):
            ret, frame = my_video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_stuff = face_cascade.detectMultiScale(gray, 1.3, 5)
        print("Face Detected")
        time.sleep(5)
        face_stuff = []
        #Take picture once person is close
        while(len(face_stuff)==0 and time.time() < timeout):
            ret, frame = my_video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_stuff = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if(len(face_stuff)>0):
            cv2.imwrite("test_data/test"+str(num)+".jpg",frame)
            print("*****FACE FOUND!*****")
            num = num + 1
            time.sleep(10)
    
    my_video.release()
    cv2.destroyAllWindows()

print("*****PROGRAM DONE!*****")


#Gathering data from video feed and save pictures
def gather_data(id,iterator):
    num = (100*iterator)-100
    if face_cascade.empty( ):
        print('WARNING: Cascade did not load')
    

    #Starting to gather the data
    my_video = cv2.VideoCapture(0)

    while (num<100*iterator):
        num = num + 1
        ret, frame = my_video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        face_cords = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if(len(face_cords)!=0):
            cv2.imshow("Gathering Data", frame)
            cv2.moveWindow("Gathering Data", 0,0)
            cv2.waitKey(1)
            cv2.destroyAllWindows()#NEW STUFF
            (x,y,w,h) = face_cords[0]
            if(num<10):
                gray = cv2.resize(gray[y:y+w, x:x+h], dsize=(250,250), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite("faces/"+str(id)+"_0"+str(num)+".png",gray)
            else:
                gray = cv2.resize(gray[y:y+w, x:x+h], dsize=(250,250), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite("faces/"+str(id)+"_"+str(num)+".png",gray)
        else:#NEW STUFF
            num = num - 1

    my_video.release()
    cv2.destroyAllWindows()



#Getting face from test images
def get_face(my_image):
    
    if face_cascade.empty():
        print('WARNING: Cascade did not load')

    my_image = cv2.resize(my_image, dsize=(353,200), interpolation=cv2.INTER_CUBIC)
    g = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

    face_cords = face_cascade.detectMultiScale(g, 1.3, 5)

    (x,y,w,h) = face_cords[0]

    g = g[y:y+w, x:x+h]

    return g

def predict(test_img):
    #Making copy
    img = test_img.copy()
    
    #detecting face on the image
    face = get_face(img)
    
    #predict the image using our face recognizer
    face = cv2.resize(face, dsize=(250,250), interpolation=cv2.INTER_CUBIC)
    label, confidence = face_recognizer.predict(face)
    
#    print("Name: "+my_info[label][0])
#    print("Confidence: "+str(confidence))
    return label

def count_visitors(arr):
    test_dic = {}
    for x in arr:
        img = cv2.imread(x)
        label=predict(img)
        
        if(label in test_dic):
            test_dic[label] = test_dic[label]+1
        else:
            test_dic[label] = 1
    
    #max(mydict.items(), key=lambda k: k[1])
    least = min(test_dic.keys(), key=(lambda k: test_dic[k]))
    mail = my_info[least][1]
    
    email = (Address(display_name='Coffee Break', username=mail.split("@")[0], domain=mail.split("@")[1]))
    return email #Least visited email


#***** MAIN CODE *****************************************************


print("What what would you like to do:")
print("Enter 0 to gather data")
print("Enter 1 to test program")
print("Enter 2 to delete user information")
answer = int(input("Enter your selection here: "))
print("")

#Gathering data
if(answer==0):
    id = int(input("Enter user ID # : "))
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    
    if(id in my_info):
        my_info[id][2] = my_info[id][2] + 1
    else:
        my_info[int(id)] = [name,email,1]
    
    gather_data(id,my_info[int(id)][2])
    store_dict(my_info)
    print("Info has been gathered thank you!")
    print("Program ended")

#Testing your program
elif(answer==1):
    #Opening all my pictures
    for i in range(len(img_arr)):
        temp=cv2.imread(img_arr[i])
        temp=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
        faces.append(temp)
        labels.append(int(img_arr[i][6:10]))
    #Testing Data
    face_recognizer.train(faces, np.array(labels))

    #Populating my dictionary
    my_info = read_dict()
    begin_broadcast()
    test_arr = glob.glob("test_data/*.jpg")


    #Predicting an image
    print("Predicting face.....")
    print(" ")
    email = count_visitors(test_arr)
    body = "Hello, it seems that you haven't been coming to our break room all that much. How can we change that?"
    msg = create_email_message(email_address,email,"Coffee Break",body)
    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(email_address, email_password)
        smtp_server.send_message(msg)

    print('Email sent successfully')
#Deleting user information
elif(answer==2):
    x = True
    while x :
        #print(my_info)
        print("READ PLEASE: Make sure you delete the data corresponding to the ID you removed!")
        key = int(input("Enter the user ID that you would like to delete: "))
        print("")
        if(key in my_info):
            print(my_info[key][0]+"'s information has been deleted")
            del my_info[key]
            store_dict(my_info)
            print("")
        else:
            print("ERROR: ID does not exist")
            print("")
        print("Would you like to continue?")
        print("Enter 0 to exit")
        print("Enter any key to continue")
        choice = input("Enter your selection here: ")
        print("")
        if(choice=="0"):
            x = False

