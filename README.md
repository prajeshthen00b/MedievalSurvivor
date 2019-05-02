# Medieval Survivor
A simple text-based, turn-based combat game written in python 3. The player is allocated a random 'hero' of predefined stats and is pitted against another hero (the CPU). 
The hero whose HP (Health) touches or drops below 0 FIRST loses the match. If both heroes have a positive health by the end of 5 rounds, the match is rendered a stalemate. 
The CPU makes it decisions based on randomized tosses via numpy.random.randint(x,y).
The heroes and their attributes (HP, Name, damage, Special Attack) have been defined on an excel sheet (MS.xlsx). Using pandas.read_excel functionality, MS.xslx is read and crawled for data. 
This is done instead of say, a dictionary, so as to handle charcaters and edit their attributes a whole lot more efficiently and conveniently. 
