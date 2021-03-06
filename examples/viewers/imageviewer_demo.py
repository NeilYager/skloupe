"""
================
ImageViewer demo
================

Basic use of ImageViewer for viewing images.

"""
from skimage import data
from skloupe.viewers import ImageViewer

image = data.camera()

view = ImageViewer(image)
view.show()

