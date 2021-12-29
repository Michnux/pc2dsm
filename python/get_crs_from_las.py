

import laspy




def main():

	# f = laspy.read('../work_dir/210323_Vol_6_Lidar.las')
	f = laspy.read('../work_dir/input.las')
	print(f.header.__dict__)
	scale = f.header.scale
	offset = f.header.offset
	mins = f.header.mins
	maxs = f.header.maxs


	print('scale', scale)
	print('offset', offset)

	print(f.header.vlrs)

	for i in range(len(f.header.vlrs)):

		print(i, '  ################')
		print(f.header.vlrs[i].__dict__)




if __name__ == "__main__":

	main()

