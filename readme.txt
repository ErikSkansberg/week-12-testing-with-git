rintOutput: copy this function from your Week 10B lab. Here's an example of using this function:
>>> PrintOutput("Hello World")
OUTPUT Hello World
LoadFile is a function that takes in a string (a filename) and then returns a list. The list is the contents of the file, where each element is a list of data from the file. Here's an example of using this function. The input file had four lines of text.
>>> lines = LoadFile("test.txt")
>>> print("OUTPUT", lines)
OUTPUT ["Hello there", "I am a test file", "please load me in and print me out", "Thanks"]
UpdateString is a function that takes in two strings and an index integer (no return). The function should print a string that is the first string modified to replace the character at the index provided with the second string. (Remember that strings are immutable, i.e., some_string[5] = 'a' will give you an error.) Here's an example of using this function:
>>> UpdateString("Hello World", "a", 3)
OUTPUT Helao World
FindWordCount is a function that takes in a list and a string. The function then returns the number of occurances of the string in the list. Here's an example of using this function:
>>> a = LoadFile("alice.txt")
>>> PrintOutput(str(FindWordCount(a, "Alice")))
OUTPUT 403
ScoreFinder is a function that takes in two lists and a string. The first list is a list of strings (player names), the second list is a list of floats (player scores), and the string is a name (player to find). If the player to find exists in the list of player names, then print the name of that player along with their associated score (which is in the second list at the same index). If the player to find does not exist in the list of player names, print player not found. Here are two examples of using this function:
>>> players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
>>> scores = [5, 8, 10, 6, 10, 4]
>>> ScoreFinder(players, scores, "jill") % NOTE: upper and lowercase should both work
OUTPUT Jill got a score of 6
>>> ScoreFinder(players, scores, "Manuel")
OUTPUT player not found
Union takes in two lists and returns a single list that is the union of the two lists (i.e., return all values of the lists A and B with no duplicates). Here's an example of using this function:
>>> players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
>>> print("OUTPUT", Union(scores, players2))
OUTPUT [5, 8, 10, 6, 4, "Melvin", "Martian", "Baka", "Xai", "Cody"]
Intersection takes in two lists and returns a single list that is the intersection of the two lists (i.e., return all values of the lists A and B that are in both A and B). Here's an example of using this function:
print("OUTPUT", Intersection(players, players2))
>>> OUTPUT ["Cody", "Xai"]
NotIn takes in two lists and returns a single list that is all values in the first list that are NOT in the second list. Here's an example of using this function:
>>> print("OUTPUT", NotIn(players2, players))
OUTPUT ["Melvin", "Martian", "Baka"]