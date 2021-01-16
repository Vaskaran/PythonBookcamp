def count_words(input_file):
    """
    This function counts approximate number
    of words in a text file.
    """
    try:
        with open(input_file,"r") as file_object:
            file_content = file_object.read()

    except FileNotFoundError as e:
        print(f"The file {input_file} is not found.")
        print(f"Error details:{e}")
    else:
        separate_words = file_content.split()
        #word_count = len(separate_words)
        # Alternative solution
        word_count = 0
        for word in separate_words:
            word_count += 1
        print("The content of the file:")
        print("-" * 20)
        print(file_content)
        print("-" * 20)
        print(f" The file has {word_count} words (approx).")


count_words('C:\\TestData\\sample_text_file.txt')
