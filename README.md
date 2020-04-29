# Matching Pennies

(Too long to read: Run [main.py][main])

This is a psychopy programme that enables participants to play a game of matching pennies against the computer. In this game, each player has a coin; on each round, each player decides which side of their coin to show. If both coins match, the participant gets a point (the 'even' player), if they don't match the computer gets a point (the 'odd' player).

When the programme starts (by running [main.py][main]), the experimenter inputs the subject's ID and specifies the computer's strategy:
- a. Random: Computer chooses face randomly with no bias.
- b. Bias towards heads
- c. Bias towards tails
- d. Switch from own previous decision
- e. Choose opposite of subject's previous decision
- f. Choose subject's previous decision
- g. Assign one of the previous 6 strategies randomly

After this information is gathered the window is generated and the experiment is ready to start.

The window displays a welcome message explaining the rules of the game. Then, after pressing space bar, the instructions are displayed including the ability to quit by pressing 'Q'. Then, the game starts for un unlimited amount of rounds until the participant presses 'Q'. To set a limited number of rounds, open [main.py][main] and go to the following section:
```python
#%% Rounds Loop starts

while True:
#For a limited number of rounds you can uncomment and edit the following line of code (and comment the previous line):
#for x in range(1, 11):
```
Comment the while loop and uncomment the for loop like so:
```python
#%% Rounds Loop starts

#while True:
#For a limited number of rounds you can uncomment and edit the following line of code (and comment the previous line):
for x in range(1, 11):
```
Adjust the second number in the ```range(p, q)``` function so that q = desired number of rounds + 1

After each choice, the participant receives feedback by seeing an image of their coin, the computer's coin, a message indicating if they won or lost the round and the current score. The images that are displayed can be found [here][images] as jpg files.

Additionally, the programme automatically prints some results in the console at the end of the game, namely:
  - Subject ID
  - Rounds played
  - Final score
  - How often the subject switched their choice so that it was different from their choice in the previous round
  - How often the subject switched their choice so that it was different from the computer’s choice in the previous round.

These results and all relevant information from the session are stored in the object ```subject_data``` of class ```Data``` which is defined in the [strategy_functions][strategy] module. If you wish to implement data extraction, this object is a good place to start.

## Repository Structure

### Main script
To run the experiment, run [main.py][main]

### Stimuli module
Most stimuli are defined in [stimuli.py][stimuli] (text and images) although a few remain in [main.py][main] for simplicity (such as the text of final score screen and the text that is displayed in the console for the experimenter).

#### Images directory
The [images directory][images] contains the files of the images that are displayed for each possible outcome (as jpg files). It also includes the original images of the coins as png files and a directory with [supporting documents][supporting documents].

(You'll notice the images that get displayed are one for every possible outcome, rather than just having the programme use the two coin images. This is because I initially had a psychopy bug that made the location of objects on the screen a bit unpredictable, thus I sacrificed some flexibility for robustness. However all necessary documents are there if you want to create new stimuli).

### Functions module
Most functions are defined in [strategy_functions.py][strategy] and are tested when [strategy_functions.py][strategy] is run as ```__main__```



## Testing
Built-in tests of the functions are included in [strategy_functions.py][strategy] when the module is run as ```__main__```

A succesful run of the built-in tests returns no feedback. However if you have made modifications they may not be tailored to your new parameters.

## License
You can find license information [here][license]

### References

Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv,
J. (2019). PsychoPy2: experiments in behavior made easy. Behavior Research Methods. 10.3758/s13428-018-
01193-y


[main]: ../master/main.py
[stimuli]: ../master/stimuli.py
[strategy]: ../master/strategy_functions.py
[images]: ../master/images
[supporting documents]: images/supporting_docs
[license]: /LICENSE
