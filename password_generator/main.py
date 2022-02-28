# Random password generator
# Creator: JackBroow

import random

# No need to change this section
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[]{}#()*;+_-"

# If you don't want any of the features in your password you can't delete it in the line below
together = lower + upper + NUMBER + Symbol
# Set the length to whatever you want (default: 9).
length = 9
# DO NOT TOUCH!
password = "".join(random.sample(together,length))
# Irrelevant code, you can change it if you want.
print("Generated password: ",password)
