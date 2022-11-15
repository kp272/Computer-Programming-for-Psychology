# Dialog box exercises

### Use the PsychoPy help page on guis to customize your "exp_info" dialog box: psychopy.gui

1. Edit the dictionary "exp_info" so you have a variable called "session", with "1" preset as the session number.
```
exp_info = {    'subject_nr':0, 
                'age':0, 
                'handedness':('right','left','ambi'), 
                'gender':('male', 'female', 'other', 'prefer not to say'), 
                'session': 1}                   # I also noticed that using "[1]" instead of "1" sets it up so that it doesn't allow the subject to 
                                                # change the session number.
```
2. Edit the "gender" variable in "exp_info" so the subject can write in whatever they want into an empty box, instead of the drop-down list
```
exp_info = {    'subject_nr':0, 
                'age':0, 
                'handedness':('right','left','ambi'), 
                'gender':(), 
                'session': 1}
```

### Using DlgFromDict:

1. Customize my_dlg so that you have a title for your dialog box: "subject info".
```
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info")
```
2. Set the variable "session" as fixed. What happens?
Answer 2. This creates the dialog box so that the subject doesn't have the choice to change the "session" that is set as "1". 
```
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])
```
3. Set the order of the variables as session, subject_nr, age, gender, handedness.
```
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'], order = ['session', 'subject_nr', 'age', 'gender', 'handedness')
```
4. Once you have done all of the above, don't show "my_dlg" right away. Tell your experiment to print "All variables have been created! Now ready to show the dialog box!". Then, show the dialog box.
```
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
print("All variables have been created! Now ready to show the dialog box!")
exp_info = {    'subject_nr':0, 
                'age':0, 
                'handedness':('right','left','ambi'), 
                'gender':(), 
                'session': 1
                }
print(exp_info)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(   dictionary=exp_info, 
                            title = "subject info", 
                            fixed = ['session'], 
                            order = ['session', 'subject_nr', 'age', 'gender', 'handedness'])

#get date and time
#-create a unique filename for the data
```

5. Fill in the following pseudocode with the real code you have learned so far:

```
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
print("All variables have been created! Now ready to show the dialog box!")
exp_info = {    'subject_nr':0, 
                'age':0, 
                'handedness':('right','left','ambi'), 
                'gender':(), 
                'session': 1
                }
print(exp_info)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(   dictionary=exp_info, 
                            title = "subject info", 
                            fixed = ['session'], 
                            order = ['session', 'subject_nr', 'age', 'gender', 'handedness'])

#get date and time
date = datetime.now()

exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename =  str(exp_info['subject_nr']) + '-' + exp_info['date'] + '.csv'
print(filename)

main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)
```

# Monitor and window exercises

### Look at the psychopy help page on "window" to help solve the exercises:

1. How does changing "units" affect how you define your window size?
For the units, we can define it's ‘height’ (of the window), ‘norm’, ‘deg’, ‘cm’, ‘pix’. 
- changing units to height doesn't affect how we define the window size, because PsychoPy automatically scales it to the window size, given that we have the ratio of the screen dimensions. 
- changing units to norm means that we have to adjust or scale the units based on the dimensions of ou window. e.g. on a 1024x768 window the size=(0.75,1) will be square. 
- when dealigng with 'deg', 'cm' and 'pix', its not so simple. 
    - 'cm' requires : information about the screen width in cm and size in pixels
    - 'deg' requires : information about the screen width in cm and pixels and the viewing distance in cm
    - 'pix' requires : information about the size of the screen (not window) in pixels, although this can often be deduce from the operating system if
      it has been set correctly there.
    
2. How does changing colorSpace affect how you define the color of your window? Can you define colors by name?

There are three colour spaces: RGB, DKL and LMS. And for all three, we use a "[ #, #, #]" format to define a colour. However, colour can also be specified by a name (e.g. ‘DarkSalmon’) or by a hexadecimal string (e.g. ‘#00FF00’).Because there are three colour spaces, depending on which colour space you use, there are different ways that we can get the desired colour by manipulating the "[ #, #, #]" format. 
Ex: 
  for the RGB and the LMS format, the numbers range from (-1) to (1) --> [-1, 0.6, 0.5]
  for the DKL format, the numbers range from 0-360 for the elevation and azimuth, and for the third number, it ranges from (-1) and (1)--> [55, 95, 0.6]

3. Fill in the following pseudocode with the real code you have learned so far:
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=35.89, distance=60) 
mon.setSizePix([1440,900])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(1200,500), color=[0.6, 0.7, 0.8], units = "height", fullscr = True)

```

# Stimulus exercises

### Check the psychopy help page on "ImageStim" to help you solve these exercises:

1. Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?
```
import numpy as np
from psychopy import core, gui, visual, event, monitors
import json
import os
from datetime import datetime

pics = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg','face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

mon = monitors.Monitor('myMonitor', width=35.89, distance=60) 
mon.setSizePix([1440,900])
mon.save()
win = visual.Window(monitor=mon, size=(1440,900), color=[0.6, 0.7, 0.8], units = "height", fullscr = True)

main_dir = os.getcwd()
image_dir = os.path.join(main_dir, 'images')

fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))
nTrials = 10

for thisTrial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[thisTrial])
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()
```
2. Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error method.
```
import numpy as np
from psychopy import core, gui, visual, event, monitors
import json
import os
from datetime import datetime

pics = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg','face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
main_dir = os.getcwd()
image_dir = os.path.join(main_dir, 'images')

mon = monitors.Monitor('myMonitor', width=35.89, distance=60) 
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]
win = visual.Window(monitor=mon, size=(1440,900), color=[0.6, 0.7, 0.8], units = "height", fullscr = True)

horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1]
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1]

fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))
nTrials = 10

for thisTrial in range(nTrials):
    my_image.image = os.path.join(image_dir, pics[thisTrial])
    my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()
```
3. Create a fixation cross stimulus (hint:text stimulus).

I have been doing the questions with the fixation cross, so I have just copy and pasted my entire code again.
```
import numpy as np
from psychopy import core, gui, visual, event, monitors
import json
import os
from datetime import datetime

pics = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg','face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
main_dir = os.getcwd()
image_dir = os.path.join(main_dir, 'images')

mon = monitors.Monitor('myMonitor', width=35.89, distance=60) 
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]
win = visual.Window(monitor=mon, size=(1440,900), color=[0.6, 0.7, 0.8], units = "height", fullscr = True)

horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1]
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1]

fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))
nTrials = 10

for thisTrial in range(nTrials):
    my_image.image = os.path.join(image_dir, pics[thisTrial])
    my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()
```
4. Fill in the following pseudocode with the real code you have learned so far:
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
start_message = "Welcome to the experiment"
my_textStart = visual.TextStim(win, text=start_message)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block"
my_textBlock = visual.TextStim(win, text=block_msg)
end_trial_msg = "End of Trial"


#-define stimuli using psychopy functions
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))


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
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        
        
        #-draw image
        my_image.image = os.path.join(image_dir, pics[thisTrial])
        my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        
        #-draw end trial text
        my_textEnd.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
```
