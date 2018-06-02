import PIL
from PIL import Image
import argparse
import glob


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
args = vars(ap.parse_args())


# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# extract our unique image ID (i.e. the filename)
	image_name = imagePath[imagePath.rfind("/") + 1:]
	img = Image.open(imagePath)
	img = img.resize((800, 350), PIL.Image.ANTIALIAS)
	img.save('resized_img/'+image_name)

print 'Done ;)'
