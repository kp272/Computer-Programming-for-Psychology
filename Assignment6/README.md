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
2. Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error method.
3. Create a fixation cross stimulus (hint:text stimulus).
4. Fill in the following pseudocode with the real code you have learned so far:
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions (images, fixation cross)

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
    #-present block start message
    #-randomize order of trials here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial
        
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
```
