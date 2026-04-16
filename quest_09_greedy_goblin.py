# The // operator performs integer division (whole numbers).
# The % (modulo) operator finds the remainder that is left over.
gold_pieces = 27
friends = 4

each_gets = gold_pieces // friends
goblin_keeps = gold_pieces % friends

print(f"Each friend receives {each_gets} gold pieces.")
print(f"The greedy goblin keeps the remaining {goblin_keeps} gold pieces for himself!")