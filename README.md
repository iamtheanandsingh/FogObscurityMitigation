# Project Proposal
Project Title: - Fog Obscurity Mitigation
It can be used to identify the licence plate of vehicles, which may not be visible properly due to fog or other weather conditions. It enhances the visibility of the plate by restoring the licence plate to its original form for clarity in detection.
 
Aim: -The aim of this project is to detect the licence number of vehicles for parking system and similar usage, while on highways or roads if the speed of vehicle is over the speed limit it would send an alert to the authorities concerned, to prevent accidents. It also has improved visibility than the normal systems which are unable to identify the licence plates in unfavourable weather conditions such as fog, which further increases its usability and application. 
 
Application and Usefulness: -
1.       Parking management: The management of car entrances and exits.
2.       Road safety: This system is used to detect license plates exceeding a certain speed, coupling the plate reading system with road radar, crossing wildfires, etc.
3.       Theft Security: - Vehicle used for committing crimes.
4.       Better Quality of Image
5.       Enhanced object recognition

Abstract: -              
Step1: Detecting the object, that is captured in the frame
Step 2: Detecting the colour of the object.
Step 3: Detecting the speed of the object.
Step 4: Checking whether the object is over speeding or not.
Step 5: (IMPORTANT) Detecting the license number plate.
Step 5.1: Licence plate detection
In order to detect licences we will use YOLO( You Only Look One) deep learning object detection architecture based on convolution neural networks.
Step 5.2: Licence plate segmentation
Now we must segment our plate number. The input is the image of the plate, we will have to be able to extract the uncharacterized images. The result of this step, being used as input to the recognition phase, is of great importance. In a system of automatic reading of number plates.
Step 5.3: Licence plate recognition
The recognition phase is the last step in the development of the automatic license plate reader system. Thus, it closes all the processes passing by the acquisition of the image, followed by the location of the plate until the segmentation. The recognition must be made from the images characters obtained at the end of the segmentation phase. The learning model that will be used for this recognition must be able to read an image and to render the corresponding character.
Step 6: Enhancing the visibility of the detected number plate by reducing the weather obscuring.

Team Members: -
1.       Anand Singh (CSI-5A)
2.       Shivam Agarwal (CSI-5B)
3.       Abhishek Kumar Gupta (ECE-5A)
4.       Tejash Seth (CSI-3C)
 
 

