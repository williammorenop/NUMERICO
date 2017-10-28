from PIL import Image
import random


file=open("pato.txt","w")
img = Image.open("pato.jpeg")
img = img.resize((200,67), Image.ANTIALIAS)
# img.draft('L')
img.convert(mode='L')
img.show()
px = img.load()
width,height = img.size
print(img.size)
pato=[];
for j in range(height):
    pato.append([])
    for i in range(width):
        # print(px[i,j],end=' ')
        # file.write(chr(px[i,j]))
        if( px[i,j] == (255,255,255) ):
            pato[-1].append('-')
            file.write('-');
        else:
            # 33-47
            c = chr(ord('!')+random.randrange(10))
            c='+'
            # c='.'
            file.write(c);
            pato[-1].append(c)
    file.write('\n')
    # print()
# print(pato)

file.close();
