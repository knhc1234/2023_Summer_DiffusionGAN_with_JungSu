import nibabel as nib

# 1. Proxy 불러오기
proxy = nib.load('./train_000_adc.nii.gz')

# 2. Header 불러오기
header = proxy.header

# 3. 원하는 Header 불러오기 (내용이 문자열일 경우 숫자로 표현됨)
header_size = header['sizeof_hdr']


# 2. 전체 Image Array 불러오기
arr = proxy.get_fdata()

print(arr.shape)