'''
CodeWars_Kata_Friend_or_Foe.py
William Ponton
1.20.19
7 kyu

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Note: keep the original order of the names in the output.

'''
# Import modules
from console_output import console_output as co
from friend_or_foe import friend_or_foe as fo

# Main function
def main():
  # Local collections
  name_list = ["Aggy", "Kenny", "Mark", "Carson", 
               "Stacie", "Jazz", "Kyle", "Whitney", "Milly",
               "Wayne", "Debbi", "Amanda", "Eric", "Masn", "Mindy",
               "KC"]  
  friend_list = []
  foe_list = []
  # Program execution
  fo.friend_or_foe(name_list, friend_list, foe_list)
  # Output
  co.console_output(name_list, friend_list, foe_list)

# Control Initiating Event
if __name__ == "__main__":
  main()