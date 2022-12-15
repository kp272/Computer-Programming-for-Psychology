My name is Kasti Patel. This file is the README file where I have explained my experiment and what it does in details.


The name of my Final Project File where my code is "FinalProject.py" --> See file [FinalProject.py](https://github.com/kp272/Computer-Programming-for-Psychology/blob/main/FINAL%20Project/FinalProject.py)


There are 2 blocks of 18 trials each. 

Each trial has a single word in a single coloured ink.

I used the colours 'red', 'green', and 'blue'. 

Each block has 

    - 6 "control" trials where the word and colour were irrelevant (ex: word "dog" in colour blue), 
    - 6 "congruent" trials where the word and colour match (ex: word "red" in red), 
    - 6 "incongruent" trials where the word and colour don't match (ex: word "red" in blue).
    
The subject should press letters ('r', 'g', or 'b') to indicate the ink colour, not the word of the colour. (ex: for word "red" in blue, they have to pick blue) 

This experiment records 

    - trials             (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
    - blocks             (1, 2)
    - words              ('dog','cat','house','bottle','blanket','pan' for trials 1-6) and ('red','green','blue' for trials 7-18 )
    - ink colours        (red, green, blue)
    - responses          ('r', 'g', 'b')
    - accuracy          (Correct, Incorrect)
    - reaction time     (seconds)

I saveed these into a csv output file

Words remained on the screen until the response was collected

each block looks something like this and I randmized this:

control (6 trials)

    - dog in red
    - cat in red
    - house in green 
    - bottle in green
    - blanket in blue
    - pan in blue

conguent (6 trials)

    - red in red
    - red in red
    - green in green 
    - green in green
    - blue in blue
    - blue in blue

in congruent (6 trials)

    - red in green
    - red in blue
    - green in red 
    - green in blue
    - blue in red
    - blue in green

I used this picture as a refrence to design my experiment. The only difference is that instead of having 3 trials I doubled this picture so that there are 2 blocks with 3 trials each. 
See file [Image_used_as_reference_to_design_experiment.jpg](https://github.com/kp272/Computer-Programming-for-Psychology/blob/main/FINAL%20Project/Image_used_as_reference_to_design_experiment.jpg)



# This was my output for the experiment in Psychopy. This corresponds with my excel file

```
## Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Final Project Images/stroop.py ##
2022-12-15 12:00:18.226 python[70309:17595947] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
[('dog', 'green', 'neutral'), ('cat', 'red', 'neutral'), ('house', 'blue', 'neutral'), ('bottle', 'red', 'neutral'), ('blanket', 'blue', 'neutral'), ('pan', 'green', 'neutral'), ('red', 'red', 'congruent'), ('green', 'green', 'congruent'), ('blue', 'blue', 'congruent'), ('green', 'green', 'congruent'), ('blue', 'blue', 'congruent'), ('red', 'red', 'congruent'), ('green', 'red', 'incongruent'), ('blue', 'green', 'incongruent'), ('red', 'blue', 'incongruent'), ('blue', 'green', 'incongruent'), ('red', 'blue', 'incongruent'), ('green', 'red', 'incongruent'), ('dog', 'green', 'neutral'), ('cat', 'red', 'neutral'), ('house', 'blue', 'neutral'), ('bottle', 'red', 'neutral'), ('blanket', 'blue', 'neutral'), ('pan', 'green', 'neutral'), ('red', 'red', 'congruent'), ('green', 'green', 'congruent'), ('blue', 'blue', 'congruent'), ('green', 'green', 'congruent'), ('blue', 'blue', 'congruent'), ('red', 'red', 'congruent'), ('green', 'red', 'incongruent'), ('blue', 'green', 'incongruent'), ('red', 'blue', 'incongruent'), ('blue', 'green', 'incongruent'), ('red', 'blue', 'incongruent'), ('green', 'red', 'incongruent')]
Block: 1 ,Trial: 1 ,Condition: incongruent , Word: red , Ink Colour: blue , Accuracy: Correct , Subject response: ['b'] , RT: 0.08828045218251646
Block: 1 ,Trial: 2 ,Condition: incongruent , Word: green , Ink Colour: red , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.1096919639967382
Block: 1 ,Trial: 3 ,Condition: incongruent , Word: green , Ink Colour: red , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.15579667896963656
Block: 1 ,Trial: 4 ,Condition: incongruent , Word: red , Ink Colour: blue , Accuracy: Incorrect , Subject response: ['r'] , RT: 0.231375846080482
Block: 1 ,Trial: 5 ,Condition: neutral , Word: bottle , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.20448558614589274
Block: 1 ,Trial: 6 ,Condition: incongruent , Word: blue , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.08886517211794853
Block: 1 ,Trial: 7 ,Condition: neutral , Word: pan , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.10032018995843828
Block: 1 ,Trial: 8 ,Condition: incongruent , Word: blue , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.14445307315327227
Block: 1 ,Trial: 9 ,Condition: congruent , Word: green , Ink Colour: green , Accuracy: Incorrect , Subject response: ['r'] , RT: 0.09611782501451671
Block: 1 ,Trial: 10 ,Condition: neutral , Word: bottle , Ink Colour: red , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.3150246050208807
Block: 1 ,Trial: 11 ,Condition: neutral , Word: blanket , Ink Colour: blue , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.7822596600744873
Block: 1 ,Trial: 12 ,Condition: neutral , Word: cat , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.3016694800462574
Block: 1 ,Trial: 13 ,Condition: congruent , Word: red , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.23242834582924843
Block: 1 ,Trial: 14 ,Condition: incongruent , Word: red , Ink Colour: blue , Accuracy: Incorrect , Subject response: ['r'] , RT: 0.019036937970668077
Block: 1 ,Trial: 15 ,Condition: congruent , Word: blue , Ink Colour: blue , Accuracy: Incorrect , Subject response: ['r'] , RT: 0.06292455899529159
Block: 1 ,Trial: 16 ,Condition: neutral , Word: house , Ink Colour: blue , Accuracy: Correct , Subject response: ['b'] , RT: 0.03893645713105798
Block: 1 ,Trial: 17 ,Condition: neutral , Word: dog , Ink Colour: green , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.1213109630625695
Block: 1 ,Trial: 18 ,Condition: congruent , Word: green , Ink Colour: green , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.06287272297777236
Block: 2 ,Trial: 1 ,Condition: congruent , Word: blue , Ink Colour: blue , Accuracy: Correct , Subject response: ['b'] , RT: 0.0566298789344728
Block: 2 ,Trial: 2 ,Condition: congruent , Word: green , Ink Colour: green , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.104902109131217
Block: 2 ,Trial: 3 ,Condition: congruent , Word: red , Ink Colour: red , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.2561368199530989
Block: 2 ,Trial: 4 ,Condition: incongruent , Word: green , Ink Colour: red , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.06385736400261521
Block: 2 ,Trial: 5 ,Condition: neutral , Word: cat , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.09589438885450363
Block: 2 ,Trial: 6 ,Condition: incongruent , Word: green , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.04768990003503859
Block: 2 ,Trial: 7 ,Condition: incongruent , Word: blue , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.07359656202606857
Block: 2 ,Trial: 8 ,Condition: neutral , Word: pan , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.04988549998961389
Block: 2 ,Trial: 9 ,Condition: neutral , Word: bottle , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.1348974988795817
Block: 2 ,Trial: 10 ,Condition: congruent , Word: blue , Ink Colour: blue , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.024351546075195074
Block: 2 ,Trial: 11 ,Condition: incongruent , Word: green , Ink Colour: red , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.2411328600719571
Block: 2 ,Trial: 12 ,Condition: congruent , Word: green , Ink Colour: green , Accuracy: Incorrect , Subject response: ['r'] , RT: 0.3162639159709215
Block: 2 ,Trial: 13 ,Condition: congruent , Word: blue , Ink Colour: blue , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.19126208685338497
Block: 2 ,Trial: 14 ,Condition: neutral , Word: cat , Ink Colour: red , Accuracy: Correct , Subject response: ['r'] , RT: 0.010769709944725037
Block: 2 ,Trial: 15 ,Condition: incongruent , Word: blue , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.06509767100214958
Block: 2 ,Trial: 16 ,Condition: incongruent , Word: blue , Ink Colour: green , Accuracy: Correct , Subject response: ['g'] , RT: 0.09948110394179821
Block: 2 ,Trial: 17 ,Condition: incongruent , Word: green , Ink Colour: red , Accuracy: Incorrect , Subject response: ['b'] , RT: 0.1763313750270754
Block: 2 ,Trial: 18 ,Condition: congruent , Word: red , Ink Colour: red , Accuracy: Incorrect , Subject response: ['g'] , RT: 0.29744198895059526
################ Experiment ended with exit code 0 [pid:70309] #################
```
