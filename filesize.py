import os


def get_size(start_path = '/Library'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                #print(fp)
                total_size += os.path.getsize(fp)
            except:
                pass
    return total_size


size = get_size()
print(size)
while size / 1024 > 0:
    size = size/1024
print(size)
