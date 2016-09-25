import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from skimage import data
from skimage.util.dtype import dtype_range
from skimage.util import img_as_ubyte, img_as_float
from skimage import exposure
from skimage.morphology import disk
from skimage.filters import rank
from skimage import io
import os
from scipy import misc
from skimage import data
from skimage import feature


def plot_img_and_hist(img, axes, bins=256):
    """Plot an image along with its histogram and cumulative histogram.

    """
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(img, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Display histogram
    ax_hist.hist(img.ravel(), bins=bins)
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')

    xmin, xmax = dtype_range[img.dtype.type]
    ax_hist.set_xlim(xmin, xmax)

    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(img, bins)
    ax_cdf.plot(bins, img_cdf, 'r')

    return ax_img, ax_hist, ax_cdf


# Load an example image
#filename = os.path.join(skimage.data_dir, 'lena_B.png')

img =(io.imread('lena_B.png', as_grey=True))

# Equalization
selem = disk(100)
img_eq = rank.equalize(img, selem=selem)

io.imsave('EqLocal.png', img_eq)
