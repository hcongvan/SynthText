import cv2
import os
import h5py
import scipy.io
# for (dir, names, files) in os.walk('/data2/synth90k/bg_img/'):
#     for f in files:
#         imgfile = os.path.join(dir,f)
#         img = cv2.imread(imgfile)
#         if img is None:
#             os.remove(imgfile)
#         else:
#             print(img.shape)
data = {}
# with h5py.File('/data2/synth90k/repoVN/SynthText/model_trained/model_dcnf-fcsp_NYUD2.mat','r') as f:
# # with h5py.File('/data2/synth90k/repoVN/SynthText/model_trained/NYU_ResNet-UpProj.mat','r') as f:
#     for i in f.keys():
#         data[i] = f[i][...]
#     print("TEST")
# scipy.io.savemat('/data2/synth90k/repoVN/SynthText/model_trained/model_dcnf-fcsp_NYUD2_1.mat', data)

mat = scipy.io.loadmat('/data2/synth90k/repoVN/SynthText/model_trained/NYU_ResNet-UpProj.mat')
print("TEST")
