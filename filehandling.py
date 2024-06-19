try:
    with open('my_file.txt', 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 98765\n")
        print("File 'my_file.txt' created and initial content written successfully.")

except FileNotFoundError:
    print("Error: File not found or path is incorrect.")
except PermissionError:
    print("Error: Permission denied to create file.")
finally:
    print("File creation process completed.\n")

try:
    with open('my_file.txt', 'r') as file:
        file_contents = file.read()
        print(f"Contents of 'my_file.txt':\n{file_contents}")

except FileNotFoundError:
    print("Error: File 'my_file.txt' not found or path is incorrect.")
except PermissionError:
    print("Error: Permission denied to read file.")
finally:
    print("File reading process completed.\n")


try:
    with open('my_file.txt', 'a') as file:
        file.write("\nAppending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
        print("Three lines appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: File 'my_file.txt' not found or path is incorrect.")
except PermissionError:
    print("Error: Permission denied to append to file.")
finally:
    print("File appending process completed.")

try:
    with open('non_existent_file.txt', 'r') as file:
        file_contents = file.read()
        print(file_contents)

except FileNotFoundError:
    print("Error: File 'non_existent_file.txt' not found or path is incorrect.")
except PermissionError:
    print("Error: Permission denied to read file.")
finally:
    print("Error handling example completed.")
