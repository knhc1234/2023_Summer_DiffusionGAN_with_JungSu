from PIL import Image
from PIL import ImageDraw

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
        #if dict == 'b\'tabby_s_002228.png\'':
        print(di)
        for x in len(dict):
            if dict == 'tabby_s_002228.png':
                img = Image.open('tabby_s_002228.png')
                img
    return dict

print(unpickle('./cifar-10-batches-py/data_batch_1'))
