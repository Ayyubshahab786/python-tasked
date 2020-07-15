with open("first task.py","a") as first_data:
    first_data.write("\nthis is a first text")
with open("first task.py","r") as second:
    content_read = second.read()
print(content_read)