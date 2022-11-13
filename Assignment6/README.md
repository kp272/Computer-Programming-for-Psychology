# Dialog box exercises

### Use the PsychoPy help page on guis to customize your "exp_info" dialog box: psychopy.gui

1. Edit the dictionary "exp_info" so you have a variable called "session", with "1" preset as the session number.
2. Edit the "gender" variable in "exp_info" so the subject can write in whatever they want into an empty box, instead of the drop-down list

### Using DlgFromDict:

1. Customize my_dlg so that you have a title for your dialog box: "subject info".
2. Set the variable "session" as fixed. What happens?
3. Set the order of the variables as session, subject_nr, age, gender, handedness.
4. Once you have done all of the above, don't show "my_dlg" right away. Tell your experiment to print "All variables have been created! Now ready to show the dialog box!". Then, show the dialog box.
5. Fill in the following pseudocode with the real code you have learned so far:

```
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data
```

# Monitor and window exercises

### Look at the psychopy help page on "window" to help solve the exercises:

1. How does changing "units" affect how you define your window size?
2. How does changing colorSpace affect how you define the color of your window? Can you define colors by name?
3. Fill in the following pseudocode with the real code you have learned so far:
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
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
