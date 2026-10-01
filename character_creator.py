character_class = ["Fighter", "Wizard", "Rogue"]

print(character_class)
class_select = input("Which class would you like to select? ")

def class_selection(class_select):
  if class_select == "Fighter":
    print("You have chosen the Fighter class.")
  elif class_select == "Wizard":
    print("You have chosen the Wizard class.")
  elif class_select == "Rogue":
    print("You have chosen the Rogue class.")
class_selection(class_select)

average_adventurer_age = 18
storyteller_age = 56
character_name = input("What will your character's name be? ")
print(f"Hello {character_name} the {class_select}!")
character_age = input("Before we get started on your adventure, I'd like to know how old your character is: ")
character_age = int(character_age)
if character_age <= 17:
  print(f"Wow, you're only {character_age}? You sure you're ready to go on an adventure lil bro?")
elif character_age == 18:
  print("Straight out of high school, huh? I don't blame you, adventuring beats working the fields.")
elif character_age <= 30:
  print(f"It's about time you left your village on a wonderful quest. You're only {character_age - average_adventurer_age} years older than I was when I left for my great adventure.")
elif character_age <= 55:
  print(f"Wow. That's the age you chose? I hate to say it but you're only {storyteller_age - character_age} years younger than me, and I made a name for myself long ago princess. Well, I guess it could be worse for you.")
elif character_age == 56:
  print("Oh come on. You just chose that age because you know thats how old I am, didn't you? Real funny.")
elif character_age < 100:
  print(f"Holy Moly you're an old bastard. I mean, no shame in that I guess. After all, I'm not the one about to throw my life away... Not to throw any more shade your way, but you do realize that would make you {character_age - storyteller_age} years older than me, right? Just thought you should know.")
elif character_age >= 100:
  print(f"Okay, I'm just gonna stop you there. You and I both know that there isn't a damn soul out there adventuring at the age of {character_age}. In fact, for even suggesting such a thing, I think I'll just personally deal with your little adventurer myself.")
  print(f"Storyteller casts Fireball at 9th level. {character_name} the {class_select} has been burnt to a crisp.")

character_allies = input("One last thing before we go. Do you have any friends you'd like to bring along? Any pets? Maybe a former biology teacher you think would be fun to drag into a fantasy world to get ripped apart? ")
character_allies_list = character_allies.split()


