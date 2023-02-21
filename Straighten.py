# - - - - - - - IMPORTS - - - - - - -
import numpy as np
import cv2

from matplotlib import pyplot as plt

# - - - - - - - FINALS - - - - - - -

# - - - - - - - METHODS - - - - - - -
def in_bounds(val, min_val, max_val):
	if val >= min_val and val < max_val:
		return True
	return False

def circle(image, x, y, val=1):
	max_x = len(image)
	max_y = len(image[0])
	
	if in_bounds(x-2, 0, max_x) and in_bounds(y, 0, max_y):
		image[x-2, y] = val
	
	if in_bounds(x-1, 0, max_x):
		if in_bounds(y-1, 0, max_y):
			image[x-1, y-1] = val
		if in_bounds(y, 0, max_y):
			image[x-1, y] = val
		if in_bounds(y+1, 0, max_y):
			image[x-1, y+1] = val
                
	if in_bounds(x, 0, max_x):
		if in_bounds(y-2, 0, max_y):
			image[x, y-2] = val
		if in_bounds(y-1, 0, max_y):
			image[x, y-1] = val
		if in_bounds(y, 0, max_y):
			image[x, y] = val
		if in_bounds(y+1, 0, max_y):
			image[x, y+1] = val
		if in_bounds(y+2, 0, max_y):
			image[x, y+2] = val
	
	if in_bounds(x+1, 0, max_x):
		if in_bounds(y-1, 0, max_y):
			image[x+1, y-1] = val
		if in_bounds(y, 0, max_y):
			image[x+1, y] = val
		if in_bounds(y+1, 0, max_y):
			image[x+1, y+1] = val
	
	if in_bounds(x+2, 0, max_x) and in_bounds(y, 0, max_y):
		image[x+2, y] = val

	return image
	

def make_vol(x, y, z, out):
	print("Making volume")
	vol = np.zeros([x, y, z, 3])
	cx, cy = 5, 10
	cx1, cy1 = x, y
	cx2, cy2 = int(x/2), int(y/2)
	cx3, cy3 = int(x/2), y
	for i in range(z):
		img = vol[:,:,i, 2]
		img += (i/z)
		vol[:,:,i, 2] = img
		img = vol[:,:,i, 0]

		img = circle(img, cx, cy)
		img = circle(img, cx1, cy1, 0.25)
		img = circle(img, cx2, cy2, 0.5)
		img = circle(img, cx3, cy3, 0.75)

		cx += 2
		cy += 3
		cx1 -= 1
		cy1 -= 2
		cx3 += 1
		cy3 -= 2
		
		vol[:,:,i, 0] = img
		img = vol[:,:,i,:]
		plt.imshow(img)
		plt.savefig(f"{out}/in/{i}.png")
	return vol

def save_vol_slice(img, out, n):
	_, _, z, _ = np.array(img).shape

	for i in range(z):
		slice = img[:, :, i, :]
		plt.imshow(slice)
		plt.savefig(f"{out}/out/{n}{i}.png")


def slice(vol, out):
	print("Slicing")
	print("Test X")
	test = np.array(vol)
	for i in range(0, 100, 1):
		x = np.arange(i)
		y = np.arange(i)
		slice_notation = np.index_exp[x, y, :, :]
		slice_notation_g = np.index_exp[x, y, :, 1]
		try:
			img = vol[slice_notation]
			plt.imshow(img)
			plt.savefig(f"{out}/out/x{i}.png")
			test[slice_notation_g] = 1
		except Exception:
			pass

	save_vol_slice(test, out, "tx")
	print("Test Y")
	test = np.array(vol)

	for i in range(0, 100, 1):
		x = np.arange(i) + 40
		y = np.arange(i)
		slice_notation = np.index_exp[x, :, y, :]
		slice_notation_g = np.index_exp[x, :, y, 1]
		try:
			img = vol[slice_notation]
			plt.imshow(img)
			plt.savefig(f"{out}/out/y{i}.png")
			test[slice_notation_g] = 1
		except Exception:
			pass

	save_vol_slice(test, out, "ty")
	print("Test Z")
	test = np.array(vol)

	for i in range(0, 100, 1):
		x = np.arange(i)
		y = np.arange(i)
		slice_notation = np.index_exp[:, x, y, :]
		slice_notation_g = np.index_exp[:, x, y, 1]
		try:
			img = vol[slice_notation]
			plt.imshow(img)
			plt.savefig(f"{out}/out/z{i}.png")
			test[slice_notation_g] = 1
		except Exception:
			pass

	save_vol_slice(test, out, "tz")
	print("Completed Slices")

# - - - - - - - MAIN - - - - - - -
def main():
	volume_path = "/mnt/ssd/Repos/Utilities/vol"
	vol = make_vol(100,100,30, volume_path)
	slice(vol, volume_path)

# - - - - - - - RUN - - - - - - -
if __name__ == "__main__":
	main()