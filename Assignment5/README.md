# Experiment structure exercises

We want to find out how long it takes people to see faces in common objects. We will present 10 images, one image per trial, in a randomized order. Each image will appear for 1 second in the center of the screen, at a size of 200x200 pixels. Each trial will start with a 1-second fixation cross, and end with a "wait for next image" text. There will be 2 blocks of trials, with 10 trials each.

On the lines denoted with an asterix *, write in the correct python code:

```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
#-import file save functions
#-(import other functions as necessary: os...)



#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist


#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data


#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
cats = ['faces'] * 10
imgs = ['im1.png', 'im2.png', 'im3.png', 'im4.png', 'im5.png', 'im6.png', 'im7.png', 'im8.png', 'im9.png', 'im10.png']

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200];
stimDur = 1;
stimOri = [10];
stimLoc = [50,150]

#-start message text *
startMessage = "Welcome to the experiment. Press any key to begin"


#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
catimgs = list(zip(cats, imgs))
print(catimgs)


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is 
    #correct") *
corrResp = [];
corrResp = np.zeros(20);

#-create an empty list for participant responses (e.g., "on this trial, response was a 
    #X") *
partResp = [];
partResp = np.zeros(20);

#-create an empty list for response accuracy collection (e.g., "was participant 
    #correct?") *
respAccu = [];
respAccu = np.zeros(20);

#-create an empty list for response time collection *
respTime = [];
respTime = np.zeros(20);

#-create an empty list for recording the order of stimulus identities *
stimOrd_iden = [];
stimOrd_iden = np.zeros(20);

#-create an empty list for recording the order of stimulus properties *
stimOrd_prop = [];
stimOrd_prop = np.zeros(20);

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    print('Welcome to block' + str(thisBlock+1))
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        print('Trial' + str(thisTrial+1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
```
## Output after Experiment structure exercises
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignment5/Assignment5.py ######
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
Welcome to block2
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
################# Experiment ended with exit code 0 [pid:3799] #################
```

# Import exercises 
1. Fill in the "Import Modules" section of the experiment structure:
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os
print(os.getcwd())
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
data_dir = os.path.join(main_dir,'data')

if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

# if not os.path.isdir(data_dir):
    # raise Exception("Could not find the path!")
```
## Output after Import exercises
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignment5/Assignment5.py ######
2022-11-07 23:33:53.106 python[3850:156323] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
Welcome to block2
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
################# Experiment ended with exit code 0 [pid:3850] #################
```

# Directory exercises
3. Fill in the following sections of the experiment structure:
```
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
print(os.getcwd())
main_dir = os.getcwd()
print(main_dir)

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#-check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
# if not os.path.isdir(data_dir):
    # raise Exception("Could not find the path!")
```
## Output after Directory exercises Question #3
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignment5/Assignment5.py ######
2022-11-07 23:35:57.771 python[3877:157587] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignment5
/Users/kasti/Desktop/PSYCH 403/Assignment5
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
Welcome to block2
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
################# Experiment ended with exit code 0 [pid:3877] #################
```
1. Automate the creation of the list of images ("pics"). Do not write them all out manually.
```
#=====================
#PREPARE CONDITION LISTS
#=====================
# Automate the creation of the list of images ("pics"). Do not write them all out manually.
           # pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
           # 'face' + str(number) + .'jpg'
n = 0
pics = []
while n < 10:
    n = n + 1
    pics.append('face' + f'{n:02}' + '.jpg') 
print(pics)

#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))
if not pics == ims_in_dir:
    raise Exception("The image lists do not match up!")

#-create counterbalanced list of all conditions *
catimgs = list(zip(cats, imgs))
print(catimgs)

```
## Output after Directory exercises Question #1
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignment5/Assignment5.py ######
2022-11-07 23:37:28.071 python[3897:158390] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignment5
/Users/kasti/Desktop/PSYCH 403/Assignment5
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
Welcome to block2
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
################# Experiment ended with exit code 0 [pid:3897] #################
```
2. Automate the task of finding out whether each image (as listed in "pics") exists in the "images" directory. Use a for loop and if statements to print "cat1.jpg was found!", "cat2.jpg was found!"... etc. Raise an exception if an image does not exist.
```
#=====================
#PREPARE CONDITION LISTS
#=====================
# Automate the creation of the list of images ("pics"). Do not write them all out manually.
           # pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
           # 'face' + str(number) + .'jpg'
n = 0
pics = []
while n < 10:
    n = n + 1
    pics.append('face' + f'{n:02}' + '.jpg') 
print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
print(ims_in_dir)

#-check if files to be used during the experiment (e.g., images) exist
    # 1) One way to do this is to use the code:
            # if not pics == ims_in_dir:
            # raise Exception("The image lists do not match up!")
    # 2) Another way to do this:
        # Automate the task of finding out whether each image (as listed in "pics") exists in the "images" directory. 
        # Use a for loop and if statements to print "cat1.jpg was found!", "cat2.jpg was found!"... etc. 
        # Raise an exception if an image does not exist.

count = 0
for pic in pics:
    if pics == ims_in_dir:
        count = count + 1 
        pic = ims_in_dir
        print ('cat%i.jpg was found!' %count)
    else:
        raise Exception("The image lists do not match up!")

#-create counterbalanced list of all conditions *
catimgs = list(zip(cats, imgs))
print(catimgs)
```
## Output after Directory exercises Question #2
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignment5/Assignment5.py ######
2022-11-08 00:41:14.223 python[4454:192201] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignment5
/Users/kasti/Desktop/PSYCH 403/Assignment5
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
cat1.jpg was found!
cat2.jpg was found!
cat3.jpg was found!
cat4.jpg was found!
cat5.jpg was found!
cat6.jpg was found!
cat7.jpg was found!
cat8.jpg was found!
cat9.jpg was found!
cat10.jpg was found!
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
Welcome to block2
Trial1
Trial2
Trial3
Trial4
Trial5
Trial6
Trial7
Trial8
Trial9
Trial10
################# Experiment ended with exit code 0 [pid:4454] #################
```
