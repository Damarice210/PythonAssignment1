# Read the input file and write to the output file
with open("input.txt", "r") as input_file:
    content = input_file.read()

# Modify the content (e.g., make it uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as output_file:
    output_file.write(modified_content)

print("File has been processed and saved as 'output.txt'.")
