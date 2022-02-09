# RepoSJX5
**Python Tkinter Project for course from NIELIT,Kolkata**
---
### *Project work for course at NIELIT, Kolkata*
### *Project work done by : Bishal Biswas (Student ID : 1920-5201-40-02-002)* 
### *Course Name: CC Python with Linux (80 hours) - (Course ID: 1920-5201-40-02)*

**_Project Target: Development of an app/UI using Tkinter and Python(2.7.x specifically) that has the capacity to interact with user on the
frontend and files in the rearend. App must have capacity to take in input, process if possible and then store the changes in files.
App must also be able to import data directly from files and bring it to the front for the user to see and administer changes._**

---
#### **Startup point: _windowControl.py_**
 > **only execute this file to start the app**
---    
#### **Test User: Username and password tags created as a default and not to be replaced**
  * username - def_usr1
  * password - Usr1pass57
  NB: Username once created is not replacable
  
#### **Super User: Username and password tags hardcoded to the code for getting access to the Maintenance section of the app**
this section can be used to add new platform details or change platform names. 
Note- no access is given to the SuperUser to change or modify any individual user's informations.
* username(Main ID) - masterC659
* password - plcc982#F

---    
**File Descriptions:**
1. windowControl.py - front end of app; contains app call and window size fix
2. AppElements.py - class and member methods for generating widget elements into the app window
3. WindowScreens.py - class and member methods for navigating between various operations of app and handling respective screens
4. ValidationChecks.py - class and member methods for validation checks of entries and updating entries into files
5. FileManagement.py - class and member methods for reading from and writing to files
6. Tickets.py - class and member methods to generate tickets pertaining to fixed rules
7. userInfo.txt - contain information of username and its linked password
8. UserDetails.txt - contain name, address and other additional information linked to a username
9. infoDB.txt - contain information of various destinations

---
***Caution: never remove the files of type .txt --- infoDB.txt, userInfo.txt, UserDetails.txt
These files are a very integral part of the UI and is important for the operation of the UI. Removing or Renaming these files 
could and will generate fatal errors and may stop the UI completely from even a small operation.***

*Future Ideas:*
1. view/hide passwords (all hidden at moment)
2. passwords editable for the super user
3. ability to change usernames by request
4. additional screen in maintenance section to change the rates of tickets
5. more power to the SuperUser to restrict/reallow a particular user on specific grounds 
6. provide Administrator handler 
7. securing and encripting data of the .txt files that contain vital informations
8. addition of timetable section 
9. formatting by using images and framing appUI window for proper display
10. highlighting of active/inactive entry modules in app
               
*Future Bugfixes:*
1. changes to the treatment of Registered ID of user
2. changes to the treatment of Phone number of user
3. changes to the Address entry section so that the whole address is visible and make the entry a wrapable text
4. ability to book return ticket in the same slot as the normal booking
5. addition of formatting to the booked ticket
6. removing spurious responses from message boxes

---
&copy;[Bishal Biswas(@WolfDev8675)](https://github.com/WolfDev8675)
_(b.biswas_94587@ieee.org)_
