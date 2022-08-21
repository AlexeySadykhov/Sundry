import os
from PIL import Image

try:
    in_files = os.listdir(input('Enter directory with images you want to unite:'))
except FileNotFoundError:
    print('No such directory.')
    exit(1)

images = list(filter(lambda x: x.endswith('.jpg') or x.endswith('.jpeg') or x.endswith('.png'), in_files))
if not images:
    print('No images found.')
    exit(1)

im_first = Image.open(images[0]).convert('RGB')

arr = []
for i in range(1, len(images)):
    arr.append(Image.open(images[i]).convert('RGB'))

out_file = input('Enter output file location:')
if os.path.isfile(out_file):
    ans = input('%s file exists. Do you want to replace it? (y/n)' % out_file)
    if ans == 'n':
        exit(0)

im_first.save(out_file, save_all=True, append_images=arr)
print('Done')
