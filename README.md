# QLearning
## Implementation of Qlearning for solving Sun/Moon game.

### Explaining the game
- Consider we have 3 * 3 square (9 tiles) that 4 of tiles are sun :sunny: and 4 are moon :crescent_moon: and thus there is one blank tile. you should move the blank tile to read the goal position. That is as follows:
  <Blank> | :crescent_moon: | :sunny:
  --- | --- | --- 
  :crescent_moon: | :sunny: | :crescent_moon:
  :sunny: | :crescent_moon: | :sunny:
  
- and for example this is your first state:
  :sunny: | :sunny: | :sunny:
  --- | --- | ---
  :crescent_moon: | :sunny: | :crescent_moon:
  :sunny: | <Blank> | :sunny:
  
- Now This algorithm Shows the way to find your way through goal.

### Code explantion
- In this report we are going to see what happens when you run  `MAIN.PY `.
- `RL` is a class which is in `RL.PY` that is the main part of this project.
- Now we'll see what is in `RL`, when the constructor is called the code will call a function of another
- class named `HELP` in `HELP.PY` that will return all subsets of size `k` of a set which size in `n`.
- Elements of the returned List will be like : `[0, 0, 0, 1, 0, 1, 1, 1]  (for k = 4, n = 8)`
- which is also another list (1's mean that we have select that object and 0's vice versa).
- Now we have all permutations of suns and moons. (0 is a symbol for suns and 1 is for moon)
- All we have to is to build all permutations that is created by blank-space (that in my code is 2).
- Now we have all states of the game we can use it to build table of Q-Learning in `MakingTable` method.
- Through `MakingTable` we call a method named `Coding` that gives a permutation and return an integer,
- I will explain about this because the rest of `MakingTable` is straight-forward.
- In `Coding` I assign a unique integer built by prime numbers and indexes of 1's and 2.
- The reason of doing this was that I built a dictionary that plays the roll of table, because time complexity of access
- in it is O(1), so for the keys I wanted something unique so I built it :)))
- Finally in `Qlearn` method I implemented q-learning, `Episode` method makes the episodes
- and `Transition` method is clear (gets the code of an state and an action and returns the code of next state).
- `Print` is just for printing the table.

### A bit running!
- Now I want to show one of lines of output and explain about it.

  `s m m b m s s m s  | Right : 79.67 | Left : -1000 | Up : 97.81 | Down : 3.14 | State number: 228`
- The first part is the way that suns and moons are located in this state(the last part is state number).
- for example here we have:
  :sunny: | :crescent_moon: | :crescent_moon:
  --- | --- | ---
  <Blank> | :crescent_moon: | :sunny:
  :sunny: | :crescent_moon: | :sunny:
  
- Next parts are related to moving the blank space for example `Up : 97.81` means that if we move the blank tile to up we'rr rewarded by    `97.81` points. (obviously we choose the one move with max reward.)

