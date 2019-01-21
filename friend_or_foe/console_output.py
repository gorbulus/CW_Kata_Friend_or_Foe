# console_output(list, list, list)
def console_output(name_list, friend_list, foe_list):
  return print("Howdy.  \n" +
                "If a name has 4 letters or less, the person is my friend.\n" +
                "If a name has 5 or more letters, the person is my foe.\n\n" +
               "Total list of names: {}\n".format(name_list) +
               "List of FRIENDS: {}\n".format(friend_list) +
               "List of FOES: {}\n".format(foe_list))