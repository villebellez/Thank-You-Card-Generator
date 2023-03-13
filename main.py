print("""
 ______  __ __   ____  ____   __  _      __ __   ___   __ __         __   ____  ____   ___   _____
|      ||  |  | /    ||    \ |  |/ ]    |  |  | /   \ |  |  |       /  ] /    ||    \ |   \ / ___/
|      ||  |  ||  o  ||  _  ||  ' /     |  |  ||     ||  |  |      /  / |  o  ||  D  )|    (   \_ 
|_|  |_||  _  ||     ||  |  ||    \     |  ~  ||  O  ||  |  |     /  /  |     ||    / |  D  \__  |
  |  |  |  |  ||  _  ||  |  ||     \    |___, ||     ||  :  |    /   \_ |  _  ||    \ |     /  \ |
  |  |  |  |  ||  |  ||  |  ||  .  |    |     ||     ||     |    \     ||  |  ||  .  \|     \    |
  |__|  |__|__||__|__||__|__||__|\_|    |____/  \___/  \__,_|     \____||__|__||__|\_||_____|\___|
  A   G E N E R A T O R   F O R   P A R E N T S   W H O   J U S T   D O N T   H A V E   T I M E 
  """)

print("Do you hate having to write thank you notes after every single one of your children's birthdays? Same!\n"
      "It's repetitive and tedious, and many of us just don't have time for it. Thankfully, there's a way to make this process a bit easier.\n")

print("This will be the generic letter that we are sending:\n\n"
      "\"Dear [name],\n\n"
      "Thank you so much for attending [child's name]'s birthday party and for your generous gift! [child's name] is going to absolutely love it. "
      "We hope you had a great time and that we'll see you at the next one!\n\n"
      "Love,\n"
      "The [family name]'s\" \n")

print("So let's start filling it out!")

childs_name= input("First, what is your child's first name? ")
family_name = input("What is your family's last name? ")
filepath = input("What is the filepath of your list of recipients? ") # For Testing: Input/Names/recipients.txt

recipients = open(filepath, 'r')
contents = recipients.readlines()
i = 0

for recipient in contents:
      name = contents[i]
      name = name.strip()
      replacements = {"[child's name]": childs_name, "[family name]": family_name, "[name]": name}
      with open('Input/Letters/starting_letter.txt', 'r') as infile, open('Output/ReadyToSend/' + name + '.txt', 'w') as outfile:
            for line in infile:
                  for source, target in replacements.items():
                        line = line.replace(source, target)
                  outfile.write(line)
      i += 1



