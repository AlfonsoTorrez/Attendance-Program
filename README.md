# Coffee Break

## Dependencies

+ Pillow
+ Glob
+ Numpy
+ cv2
+ Pprint
+ Pickle
+ Smtplib

__Coffee Break__ is a team based project for the course CST 205 - Multimedia Design & Programming. The program was created to increase a user/customer base at a designated location. 

The example we are going to use is a break room with a coffee machine. Our mission is get more people to use the coffee machine. The way we will do that is to put a computer near the coffee machine to take video of the people who come and go. The program will then identify how many times an individual comes to get coffee. Out of all the people who go get coffee, we are seeking to target the people who get coffee the least amount of times. The people in question will be targeted by an email to let them know what kind of coffee would encourage them to go to the coffee machine more often. 

## Team Members 

+ Alfonso Torres
+ Jaime Velazquez
+ Brittany Arnold

## Built With

+ [Python](https://www.python.org/) - The programming language used for Coffee Break
+ [OpenCV Library](https://opencv.org/) - Open Source Computer Vision Library

## Getting Started

### Step 1
Gather employee data. For our program to accurately identify its users, an extensive data set of faces must first be aquired. Around 100 or so pictures is enough to attain a high success rate. To obtain these pictures, all that has to be done is to run the program and input 'gather data'. Once this is done, have the employee sit, and face the camera. Instruct the employee to move their head from side to side. This process should take around twenty to thirty seconds. At the end of the picture taking process, the program will prompt the employee for their Employee ID as well as their name, and email.
### Step 2
Setup a camera that's running our program in front of the office coffee machine! Throughout the day, a tally will be kept of the amount of times an employee visits the coffee machine. The employee with the highest amount of uses will be automatically sent an email a discount for their next coffee! The employee's with the least amount of visits will be sent a questionaire asking for which kind of coffee blends they would most like to have at the office. 

## Future Improvements

### Training data
Currently, our algorithm can only make accurate predictions based on a large training data set. We would like to reduce the amount of required training data. This would eliminate the need for every employee to take the initial 100 pictures. The initial few pictures that are taken when an employee is hired would suffice.

### Accuracy
The current face recognition algorithm that we're using could be improved upon. We would like to implement a feature where, when a person is not in the data set, the program will not return a positive match.

### Email Configuration
Currently, our company email is configured with strings that are public. Upon future improvements, we would like to abstract this information and hide it.
