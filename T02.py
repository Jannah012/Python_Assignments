file_name=input('Input the filename:')
d={'py':'python','docx':'word document','pdf':'portable document format','ppt':'powerpoint'}
ext=file_name.split('.')[-1]
if ext in d:
    description=d[ext]
    print('The extension of the file is:', description)
else:
    print('Unknown extension')
