# will remove files older than n days.
import os
import time


def delete_old_files():
    print('\n')
    days_to_keep = 7
    path = os.getcwd()  # folder of the script file
    # path = r"C:\Test"
    extension = '.xlsx'

    now = time.time()
    time_fence = now - days_to_keep * 86400

    file_list = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            file_list.append(os.path.join(r, file))

    for f in file_list:
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < time_fence and f.endswith(extension):
            os.remove(f)
            print(f'file: {f} was deleted')
    print('\nScript finished the job!')


delete_old_files()
