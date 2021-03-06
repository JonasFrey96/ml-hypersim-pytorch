from torchvision import transforms as tf
from torchvision.transforms import functional as F
import torch
import PIL
__all__ = ['Augmentation']

class Augmentation():
  def __init__(self, output_size=400, degrees = 10, flip_p = 0.5, jitter_bcsh=[0.3, 0.3, 0.3, 0.05]):
      
    # training transforms
    self._output_size = output_size
    self._crop = tf.RandomCrop( self._output_size  )
    self._rot = tf.RandomRotation(degrees = degrees, resample = PIL.Image.BILINEAR)
    self._flip_p = flip_p
    self._degrees = degrees
    
    self._jitter = tf.ColorJitter(
        brightness=jitter_bcsh[0],
        contrast=jitter_bcsh[1],
        saturation=jitter_bcsh[2],
        hue=jitter_bcsh[3])
    # val transforms 
    self._crop_center = tf.CenterCrop(self._output_size)
        
  def apply(self, img, label, only_crop=False):
    if not only_crop:
      # Color Jitter
      img = self._jitter(img)
      
      # Crop
      i, j, h, w = self._crop.get_params( img, (self._output_size, self._output_size) )
      img = F.crop(img, i, j, h, w)
      label = F.crop(label, i, j, h, w)
      
      # Rotate
      angle = self._rot.get_params( degrees = (self._degrees,self._degrees) )
      img = F.rotate(img, angle, resample=PIL.Image.BILINEAR , expand=False, center=None, fill=None)
      label = F.rotate(label, angle, resample=PIL.Image.NEAREST , expand=False, center=None, fill=None)
      
      # Flip
      if torch.rand(1) < self._flip_p:
        img = F.hflip(img)
        label = F.hflip(label)

    # Performes center crop 
    img = self._crop_center( img )
    label = self._crop_center( label )
    
    return img, label