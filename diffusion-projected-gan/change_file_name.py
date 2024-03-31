import os
count = 0

for i in range(0,60):
    if i < 10:
        dir_path = '.\\CTData\\Train\\0000{}'.format(i)
    else:
        dir_path = '.\\CTData\\Train\\000{}'.format(i)
    file_names = os.listdir(dir_path)

    for name in file_names:
        src = os.path.join(dir_path, name)
        result_path = '.\\CTData2\\Train\\'
        if count < 10:
            dst = str('img0000000{}').format(count) + '.png'
            result_path = result_path + '00000'
            dst = os.path.join(result_path, dst)
        elif count < 100:
            dst = str('img000000{}').format(count) + '.png'
            result_path = result_path + '00000'
            dst = os.path.join(result_path, dst)
        elif count < 1000:
            dst = str('img00000{}').format(count) + '.png'
            result_path = result_path + '00000'
            dst = os.path.join(result_path, dst)
        else:
            dst = str('img0000{}').format(count) + '.png'
            result_path = result_path + '00001'
            dst = os.path.join(result_path, dst)
        os.rename(src, dst)
        count += 1