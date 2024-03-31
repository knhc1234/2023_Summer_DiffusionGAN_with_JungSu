import h5py
import numpy as np
from PIL import Image
from sklearn.preprocessing import MinMaxScaler
def convert(path):
    hdf = h5py.File(path,'r')
    X = np.array(hdf['mri'][:,:,0])

    min_max_scaler = MinMaxScaler()

    # 바탕 선 제거용 코드
    trans = X.reshape(-1, 1)
    array = min_max_scaler.fit_transform(trans)
    result = array.reshape(X.shape)
    # ---------------------------------------------

    img = Image.fromarray(result.astype('uint8'), 'L')
    #img = img.resize((256,256))
    img.save("ct.png", "PNG")
    img.show()

if __name__ == '__main__':
    for i in range(60):
        if i<10:
            i = '0{}'.format(i)
        convert('./train/train_0{}.h5'.format(i,i))
        break