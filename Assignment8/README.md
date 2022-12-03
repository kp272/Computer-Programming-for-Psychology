# PsychoPy keypress exercises

1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial. Come up with a solution so that only a single response is recorded from event.getKeys (e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in level6.

```

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
