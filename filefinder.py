# import chardet

# def detect_encoding(file_path):
#     with open(file_path, 'rb') as file:
#         result = chardet.detect(file.read())
#     return result['encoding']

# file_encoding = detect_encoding('E:\\userform\\templates\\home.html')
# print(file_encoding)

# try:
#     with open('E:\\userform\\templates\\home.html', 'r', encoding=file_encoding) as file:
#         content = file.read()
# except UnicodeDecodeError as e:
#     print(f"Error reading HTML file: {e}")
#     # Handle the error as needed

# Read UTF-16 file content
# with open('E:\\userform\\templates\\home.html', 'r', encoding='utf-16') as file:
#     content_utf16 = file.read()

# # Write content to a new UTF-8 file
# with open('E:\\userform\\templates\\home_utf8.html', 'w', encoding='utf-8') as file:
#     file.write(content_utf16)