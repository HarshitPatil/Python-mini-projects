#importing modules
import os

#making a function to rename files
def rename(path):
    #Using enumerate inbuilt function to get index and value through for loop iteration.
    for idx, file in enumerate(os.listdir(path)):
        
        #checking for all the image formats and renaming it.
        if file.endswith('.jpg') or file.endswith('.img') or file.endswith('.png'):
            new = 'image'+ str(idx) + '.' + file.split('.')[1]
        
        #checking for video formats and renaming it.
        elif file.endswith('.mp4'):
            new = 'Video' + str(idx) + '.' + file.split('.')[1]

        #checking for all sound/music formats.
        elif file.endswith('.mp3') or file.endswith('.ogg') or file.endswith('.wav'):
            new = 'Sound' + str(idx) + '.' + file.split('.')[1]
            # spliting the file name from '.' and after splitting these gives us a list of
            # filename and file type eg. old_song.mp3 will be ['old_song', 'mp3'] and 
            # to get second value in list we use [1] after file.split('.') but '.' is missing.
            # so we add '.' seprately in cocatination
            # at last the cocatination is '<new_filename>' + str(idx) + '.' + file.split('.')[1]
            # This is same with every new variable in each if/else statement.

        #remaning all file types all are renamed as unknown.
        else:
            new = 'unknown' + str(idx) + '.' + file.split('.')[1]
        
        os.rename(path+file, path+new)

if __name__ == '__main__':
    path = 'C:\\Users\\<user_name>\\Pictures\\images\\'
    rename(path)
     
