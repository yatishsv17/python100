with open("./Documentation/backend_web_development.txt") as file:
    contents = file.read()
    print(contents)
    # Return all lines in the file as a list where each line is an item in the list object
    print("-----")
    # file.seek(0)  # Reset file pointer to beginning
    print(file.readlines())