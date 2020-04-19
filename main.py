#a simple mad libs game that will prompt the user for some inputs and then put together a story

#possible problems - no way to check if the user is inputting the correct part of speech



holiday = input("Enter a Holiday: ")
emotion = input("Enter an emotion: ")
verb = input("Enter a verb: ")
family = input("Enter a family member: ")
noun = input("Enter a noun: ")
adj = input("Enter an adjective: ")

print("Today is %s and that makes me very %s. Today I will %s because of my %s. Every year, my %s used to get me a %s for %s and that memory is  %s." % (holiday, emotion, verb, family, family, noun, holiday, adj))
