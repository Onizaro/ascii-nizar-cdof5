from letters import alphabet 
text = input("tapez des lettres:")

for i in range(11):
    for letter in text:
        #if letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        print(alphabet[letter][i],end="")
    print("")
        