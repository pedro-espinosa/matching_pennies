# matching_pennies
[Too long to read: Run main.py]

This is a programme that enables participants to play a game of matching pennies against the computer. In this game, each player has a coin; on each round, each player decides which side of their coin to show. If both coins match, the participant gets a point (the 'even' player), if they don't match the computer gets a point (the 'odd' player).

When the programme starts, the experimenter inputs the subject's ID and specifies the computer's strategy:
- A. Random: Computer chooses face randomly with no bias.
- B. Bias towards heads
- C. Bias towards tails
- D. Switch from own previous decision
- E. Choose opposite of subject's previous decision
- F. Choose subject's previous decision
- G. Assign one of the previous 6 strategies randomly

Additionally, the programme automatically prints some results at the end of the game namely:
  - Final score
  - How often the subject switched their choice so that it was different from their choice in the previous round
  - How often the subject switched their choice so that it was different from the computer’s choice in the previous round.

Finally, the programme stores the subject's ID and their results in a csv file.




References
Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv,
J. (2019). PsychoPy2: experiments in behavior made easy. Behavior Research Methods. 10.3758/s13428-018-
01193-y
