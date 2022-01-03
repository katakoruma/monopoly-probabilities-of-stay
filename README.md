# monopoly-probabilities-of-stay

Solution to determine the probability of stay for each field in Monopoly.

To achieve this I have entered the transition probabilities from each of the 40 fields to any other in a 40 x 40 matrix (input files).
Movement possibilities result in each case from the triangular distribution when rolling the two dice, from some event and community cards (e.g. Go to jail) and from the double rule, according to which after rolling a double three times the player also has to go to jail.

The latter was not considered in the first matrix (Monopoly_without_double.xlsx). 
Also, there was no distinction between "In Jail" and "Just Visiting", where players are on the same field, but still in different circumstances.
In the second version (Monopoly_with_double.xlsx), the double rule is implemented, and prison stays are represented by the "Go to Jail" field, while the actual prison field stands for "Just Visiting".
