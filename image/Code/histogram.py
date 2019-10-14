from skimage import data, exposure, img_as_float
from skimage import img_as_ubyte
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
image = img_as_ubyte(data.camera())

def histogram(image, nbins=256, source_range='image', normalize=False):
  image = tf.convert_to_tensor(image, dtype = tf.float32) # Change image to tensorflow
  with tf.Session() as sess:
      sh = sess.run(tf.shape(image))
  if len(sh) == 3 and sh[-1] < 4:
      warn("This might be a color image. The histogram will be "
            "computed on the flattened image. You can instead "
            "apply this function to each color channel.")

  with tf.Session() as sess:
    image = tf.reshape(image,[-1,1]) # 512**2 ==> (262144,)
  value_range = [0.0, 256.0] 
  new_values = image
  hist, bin_edges = np.histogram(image, bins=nbins, range=hist_range)  # nbins = 256
  bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.         # hist: 数量。 bin_centers: 刻度。
      #print(bin_centers)
  if normalize:
      hist = hist / np.sum(hist)
  return hist, bin_centers



