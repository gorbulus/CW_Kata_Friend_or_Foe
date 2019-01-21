# friend_or_foe(list, list, list)
def friend_or_foe(name_list, friend_list, foe_list):
  for name in name_list:
    if len(name) > 4 or len(name) < 4:
      foe_list.append(name)
    else:
      friend_list.append(name)