import my_library # imports the whole module.
print("Accessing some list elements:")
print(f"my_list[0]={my_library.my_list[0]}")
print(f"my_list[3]={my_library.my_list[3]}")

print("\nAccessing some dictionary elements:")
print(f"my_dictionary[1]={my_library.my_dictionary[1]}")
print(f"my_dictionary[2]={my_library.my_dictionary[2]}")

print("\nUsing the make_total_double function now.")
result = my_library.make_total_double(20, 30.5)
print(result)
