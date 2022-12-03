# PsychoPy keypress exercises

1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial. Come up with a solution so that only a single response is recorded from event.getKeys (e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in level6.

```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event, monitors

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os
from datetime import datetime



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


#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
print("All variables have been created! Now ready to show the dialog box!")
exp_info = {'subject_nr': 0, 'age': 0, 'handedness':('right','left','ambi'), 'gender':(), 'session': 1}
print(exp_info)
print("All variables have been created! Now ready to show the dialog box!")
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = "subject info", fixed = ['session'], order = ['session', 'subject_nr', 'age', 'gender', 'handedness'])

#get date and time
date = datetime.now()
exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename =  str(exp_info['subject_nr']) + '-' + exp_info['date'] + '.csv'
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 2
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
cats = ['faces'] * 10
imgs = ['im1.png', 'im2.png', 'im3.png', 'im4.png', 'im5.png', 'im6.png', 'im7.png', 'im8.png', 'im9.png', 'im10.png']

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200];
stimDur = 1;
stimOri = [10];
stimLoc = [50,150]

#-start message text (check "CREATION OF WINDOW AND STIMULI" for a repeat of this)
startMessage = "Welcome to the experiment. Press any key to begin"

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
mon = monitors.Monitor('myMonitor', width=35.89, distance=60) 
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix() # --> these 3 were for the alternation of stimuli n 4 quadrants
thisWidth = thisSize[0]
thisHeight = thisSize[1]
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1]
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1]
CorrectResponse = [True, True, True, True, True, True, True, True, True, True]

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(1440,900), color=[0.6, 0.7, 0.8], units = "height", fullscr = True)

#-define experiment start text unsing psychopy functions
start_message = "Welcome to the experiment"
my_textStart = visual.TextStim(win, text=start_message)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block"
my_textBlock = visual.TextStim(win, text=block_msg)
end_trial_msg = "End of Trial"
my_textEnd = visual.TextStim(win, text=end_trial_msg)


#-define stimuli using psychopy functions
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))

#-create response time clock
block_timer = core.Clock()
trial_timer = core.Clock()
# wait_timer = core.Clock()
# clock_wait_timer = core.CountdownTimer()
stimulus_timer = core.Clock()
response_timer = core.Clock()

#-make mouse pointer invisible


#=====================
#START EXPERIMENT
#=====================
#-present start message text
my_textStart.draw()
win.flip()

#-allow participant to begin experiment with button press
my_textBlock.draw()
win.flip()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    #-present block start message
    print('Welcome to block' + str(thisBlock+1))
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    block_timer.reset()
    block_timer_start = block_timer.getTime()
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
        trial_timer_start = trial_timer.getTime()
        #-empty keypresses
        count = -1
        
        
        #=====================
        #START TRIAL
        #=====================   
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1: 
        #-draw fixation
            fix_text.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        stimulus_timer.reset()
        response_timer.reset()
        startTime = stimulus_timer.getTime()
        while stimulus_timer.getTime() <= 2:
        #-draw image
            my_image.image = os.path.join(image_dir, pics[thisTrial])
            my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
            my_image.draw()
            fix_text.draw()
        #-flip window
            win.flip()
        #-collect subject response for that trial
            key = event.waitKeys(maxWait = (response_timer.getTime() <= 2), timeStamped = response_timer)
            if key:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    print(key)
                    
        #-wait time (stimulus duration)
        endTime = stimulus_timer.getTime()
        
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw stimulus
        #-...
        
        #-collect subject response time for that trial
        print("The test took {} sec." .format(endTime - startTime)) 
        
        #-collect accuracy for that trial
        #if key[0] == 'left':
            #if horizMult[thisTrial] == -1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        # if key[0] == 'right':
            #if horizMult[thisTrial] == 1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        
        #-draw end trial text
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1:
            my_textEnd.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        trial_end_time = trial_timer.getTime()
    
    block_end_time = block_timer.getTime()    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()

#-quit experiment
```
This was my output (I also double checked this by pressing the keys multiple times in each trial, but it only recorded the first time I pressed it):
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Assignment7.py ######
2022-12-03 15:48:51.156 python[86736:10778855] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
15-3-12-2022
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
The test took 2.0425316349137574 sec.
Trial2
[['right', 0.19952150504104793]]
The test took 2.3974182209931314 sec.
Welcome to block2
Trial1
[['left', 0.40868456079624593]]
The test took 2.437658107141033 sec.
Trial2
[['right', 1.1735229259356856]]
The test took 2.191165911965072 sec.
################ Experiment ended with exit code 0 [pid:86736] #################

```
2. Statement placement in your script is very important when collecting responses and refreshing keypresses. What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? What happens if you unindent the "if keys:" line?

# Psychtoolbox keypress exercises
1. Notice how "for key in keys:" in the kb examples of level6 are not indented within the stimulus presentation while loop. What happens if you indent this line? How is this different from event.getKeys?

2. Try out the kb keypress functions using core.wait instead of a CountdownTimer. What happens?

3. Use your favorite search engine to interpret epoch time from key.tDown. Add a bit of code using datetime or ctime modules to print epoch time into a readable format.

# Recording data exercises

1. Instead of collecting key name, subject RT, subject accuracy, and correct responses in lists, create a dictionary containing those variables. Then, during response collection, append the data to the dictionary instead of filling lists.

2. Keep in mind that you can pre-define dictionaries or lists for the whole experiment (in which case you have to use [block][trial] indexing to collect responses) or you can do it block-by-block (in which case you can use [trial] indexing). Create your lists (or dictionary, if you prefer) within the block loop and switch to [trial] indexing.

# Save csv exercises

1. Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you created above) as a .csv file.

# Save JSON exercises

1. Add JSON filesaving to your experiment script.

# Read JSON exercises

1. Create a short "read and analysis" script that loads a saved JSON file, performs rudimentary analyses on the data, and prints the means.

2. Change your "read and analysis" script so that RTs for inaccurate responses are removed from analysis.

3. Change your "read and analysis" script so that any trials without a response (0 value) are removed from analysis.
