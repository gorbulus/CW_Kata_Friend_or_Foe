# Friend or Foe

CodeWars Kata.

7 Kyu:

* Python 3

William Ponton
1.20.19
7 kyu

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Note: keep the original order of the names in the output.

## Sorting Names

Names that do not have exactly 4 charaters are added to the "FOE" list.
Names that  have exactly 4 charaters are added to the "FRIEND" list.

```python
# friend_or_foe(list, list, list)
def friend_or_foe(name_list, friend_list, foe_list):
  for name in name_list:
    if len(name) > 4 or len(name) < 4:
      foe_list.append(name)
    else:
      friend_list.append(name)
```

As you can see the algorithm checks each name in name_list to see the length.
Next, the name is appended to either the foe_list or friend_list depending on the length.

## Results

If the name has exactly 4 characters, it is a FRIEND~!

Output it displayed to the user:

```python
# console_output(list, list, list)
def console_output(name_list, friend_list, foe_list):
  return print("Howdy.  \n" +
                "If a name has 4 letters or less, the person is my friend.\n" +
                "If a name has 5 or more letters, the person is my foe.\n\n" +
               "Total list of names: {}\n".format(name_list) +
               "List of FRIENDS: {}\n".format(friend_list) +
               "List of FOES: {}\n".format(foe_list))
```