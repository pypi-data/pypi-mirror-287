import matplotlib.pyplot as plt
import nibabel as nib
from wmh_seg import wmh_seg
import numpy as np

nii = nib.load('/Users/jinghangli/Developer/wmh_seg/FLAIR.nii')
out = wmh_seg(nii)

slice = nii.get_fdata()[:,:,50]
out_2d = wmh_seg(slice)
plt.imshow(slice, cmap='gray')
plt.imshow(out_2d, cmap='gray', alpha=0.5)
plt.show()