# Developer Journal

This is my intro to my project where i decided to go for a sort of user management system to focus on trying to showcase
the best that i could of the requirements from the brief for the project in a simple but (in my hopes) effective manner
with little to no bugs and having a full proof system that cant be given any invalid inputs and such.




# The Process of Completion

I started with brain storming what i was going to do and how i would structure my files and ended with the result i have now
and i had also created a flowchart diagram so that i could better visualise what i was going to do and once i was set on it, i
dived in.

i started with completing the regex checks/formatting first to get it out of the way as alot of the use for the program needs to
have checks in place for the name, email, password to make sure that it can run correctly. I looked through the material on moodle
aswell as finding a document with a table of all the different parts of regex so that i could better understand what i was doing.

Then i moved onto the classes as that was going to be the biggest bulk of my code and the hardest for me to code, i would go back
and forth from the lecture materials to try make a better and solid code aswell as turning to youtube and other sources to help teach
me more about how to use the classes better. I did struggle at the beginning with writing the classes as it was somewhat confusing how
their structure worked and then also how the subclasses worked. However in the end I got it all done and was happy with the end result 
where i feel as i have so far to this point fully implemented classes(OOP), REGEX and in this case File I/O. I had used a great portion
writing to a csv file within my class system to make sure that i could read, write etc all within each seperate class which had their own
permissions/roles to be able to do these things(seperate menu options).

Once i finished making all the classes and cross checking to make sure that i did have everything completed with out any workarounds i
moved on to doing the Testing portion of the brief before fully tieing together my code in the 'Project_Main_Code' file. In here i made 
sure to cover all the grounds i could think of, this being: Testing the Name, Email and Passords so that they actually are assuring my
regex works, then moved onto testing my class system where i checked what users can do depending on their role aswell as if a subclass
truly is a sublcass. Finally just to make sure that my code will work as expected later i tested the menu that was apart of each of the
classes with respective options, this consisted of testing if a user with the incorrect role not being able to use an option that a user
of a higher role can use and then making sure that non existant options are non existant. This means i was able to cover: REGEX testing, 
class/permission testing aswell as string testing.

Now that the entire back bone of the project has been completed and that im happy with the current state of the project i finally moved
onto combining together everything to make a working terminal app(i wanted to try a gui but it wasnt covered on material and was difficult).
This started with creating my main function which would then chain and lead into other functions as the code was slowly worked through, and
due to the structure that i have made my classes and regex where seperate libraries that i imported to allow me not to clutter my main file
and this played a large role in finishing that main file as lots of the options and usage sections are chained off into the other files libraries
of classes and regex formatting, but that made it overall more organised and cleaner to read. The main code itself was one of the most
straightforward part of the entire project in my opinion since it was lots of if statements which ran through the class library which already
had their respective functions in place which i just had to call upon. i only had to make the first two filler options which had been for fun 
and i used cowsay and random to print a random animal and then i went out and found a joke library which i used for another option.




# Specifics

If we look at specifics ill start with the testing file which corresponds to material found in lecture 8 which focused on File testing using 
primarily pytest for the that lecture but like i stated i had to use a different method as it wasnt working for me at the time. In the lecture
we can find that unit testing was shown and taught which is what i showcased in my code. Then if we move onto the REGEX file it links back to 
workshop 8 where we first started to implement it into code, but now as i have showed in my project code i have expanded to use more functions
of regex to better specify and limit what is valid and invalid as input. Moving onto pretty much the last important file to talk about is my 
'User_Levels' file which contains parts from lecture 9 With OOP(Object Orientated Programming), aswell as lecture 8 with File I/O with the use
of reading and writing a file while also appending data onto the current file without intruding on whats already existing.

This means i was able to cover the: Regular Expressions, Testing, Libraries, File I/O and Object Orientated Programming elements from the 
project brief.