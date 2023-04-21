# "Sherlock" version 0.0.1
import functions

print("""Welcome in Sherlock game!
          
                            .--:::::--. 
                           '           '       
                          ''           ''       
                      ---'''```````````'''---      
                      -----____________------          
          
     .:::. ||   || ||```` ||''\  ||      =====  :::::: ||  //
    ||     ||   || ||     ||  || ||     [[   ]] ||     || //
     ====: ||===|| ||===  ||==// ||     [[   ]] ||     ||//
        || ||   || ||     ||':.  ||     [[   ]] ||     ||''::
    '::::' ||   || ||.... ||  || ||____  =====  :::::: ||  || 

Create your own detective and solve puzzles that fate will put in front of you.
Gain experience and develop your skills.
Find missing Marietta.
""")

detective_name = input('Give your detective name: \n')


print(f"\nHi {detective_name}! \nJoanna Mark, a plump blonde with green eyes came tonight to your house asking for \
a help. Her daughter Marietta left home the previous day and hasn't returned. All Joanna knows is that \
she was supposed to meet with her friend Andrew in an abandoned metal factory. You promised to find Marietta and \
therefore went to the meeting place. \n \n In a dark room you noticed a piece of paper lying on an old desk. You \
cautiously walked up to it. On the document was written: \"first P. of USA\".\n")

print("It crossed your mind that this might be about the President of United States. But... \n\n# Who was the first \
president of USA?")

print("""a. John Adams
b. Thomas Jefferson
c. George Washington""")

functions.response_pattern_1('c', 10)


print("""Ok. Let's focus on the task. 
So the first President of USA was G. Washington...
After turning the piece of paper around you noticed blood. You looked around. A strange, dusty image on the wall \
caught your eye.\n""")

temporary_answer = input("Do you walk up to it? Type y or n: \n")

if temporary_answer == 'y':
    print("""Painting shows a man holding his head with both hands. His eyes are goggled and his mouth is wide open. \n\
You think that it is probably Edward Munch's painting, called \"The Scream\". \n For what reason this man holds his\
head like that?""")
    print("""a. He is in crisis
b. He is afraid of something
c. He suffers""")
    functions.response_pattern_1('c', 15)

if temporary_answer == 'n':
    print("""Your phone rang.\n x-\-/-x-\-/-x-\-/-x-x-\-/-x \n The inspector orders you return to the headquarters \
immediately. He has an important announcement for you. What are you doing?""")
    print("""a. You humbly return
b. You tell him that you are on an important mission
c. You turn off the phone.
    """)
    functions.response_pattern_2('b', 'c', 'a')








