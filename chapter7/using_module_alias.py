import my_library as ml # imports the whole module.
print("Accessing a list element:")
print(f"my_list[0]={ml.my_list[0]}")

print("\nAccessing a dictionary element:")
print(f"my_dictionary[1]={ml.my_dictionary[1]}")

print("\nUsing the make_total_double function now.")
result = ml.make_total_double(20, 30.5)
print(result)
