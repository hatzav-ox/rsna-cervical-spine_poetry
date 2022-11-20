import matplotlib.pyplot as plt
import nibabel as nib
from nibabel import Nifti1Image
import numpy as np


import streamlit as st

import time

"""
# Medical Images Exploration
"""


@st.cache
def load_nii_file(file_path: str) -> np.memmap:
    image_obj: Nifti1Image = nib.load(file_path)
    return image_obj.get_fdata()


image_path: str = "/Volumes/Data/HadavandsMininos/data/raw/segmentations/1.2.826.0.1.3680043.780.nii"

image_data: np.memmap = load_nii_file(file_path=image_path)

height, width, depth = image_data.shape


i: int = st.slider("Layer", 0, depth - 1, 100)

f"""
### Plotting layer {i}
"""
st.image(image_data[:, :, i], clamp=True)

bone_image = st.image(image_data[:, :, 0], clamp=True)

while True:
    for i in range(depth):
        time.sleep(0.1)
        bone_image.image(image_data[:, :, i], clamp=True, caption=f"Layer {i}")
