import os
import os.path


def batch_rename(directory):
    print("Leave Paramter 2 field blank if your filename doesn't need two parameters")
    param1 = input('Enter Parameter 1 eg. Friends  : ')
    param2 = input('Enter Parameter 2 eg. Season number  : ')
    name = ' '.join((param1, 'S' + param2.zfill(2))) if param2 != '' else param1 + ' '
    param3 = int(input('Enter parameter 3 e.g. starting episode  : '))
    extension = input('Enter file extension e.g. mkv,mp4,avi : ')
    for filename in os.listdir(directory):
        old_name = os.path.join(directory, filename)
        new_name = os.path.join(directory, ''.join((name, 'E' + str(param3).zfill(2), '.' + extension)))
        os.rename(old_name, new_name)
        param3 += 1
    print('Done')


print('Hit return at location input if this python script and files that are to be renamed are in the same folder.')
print(r'Accepted Formats are D:\Season 1 or D:/Season 1 or D://Season 1  ')
location = input(r'Input location:')
batch_rename('./') if location == '' else batch_rename(location)
