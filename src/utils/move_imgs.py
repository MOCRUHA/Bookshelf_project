#move images from storage dir to work dir

import os


def move_img(src, dst):
	#list all images
	imlist = os.listdir(src)

	#rename and move one image at a time to the dst dir
	num=0
	for image in imlist:
		src_path = os.path.join(src, f'{image}')
		dst_path = os.path.join(dst, f'bc_{num}.jpg')
		os.rename(src_path, dst_path)
		num+=1




