def permute(data, i, length, output_file):
    if i == length:
        output_file.write(''.join(data) + '\n')
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length, output_file)
            data[i], data[j] = data[j], data[i]  # backtrack
            
# ask user to enter a list of characters
characters = input("Enter a list of characters: ")

# ask the user the location where the file will be stored
location = input("Enter the location where the file will be stored: ")

# ask the user the name of the file
filename = input("Enter the name of the file (with .txt extension): ")

# if in the location such a file exist alert the user and ask him for another name
filepath = location + '/' + filename
try:
    with open(filepath, 'x') as f:
        permute(list(characters), 0, len(characters), f)
except FileExistsError:
    print("File already exists. Please choose another name.")
# if in the location such a file exist alert the user and ask him for another name
