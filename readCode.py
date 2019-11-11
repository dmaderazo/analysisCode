import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n','--N',type = int)
parser.add_argument('-nc','--num_class', type = int)
args = parser.parse_args()

num_class = args.num_class
N = args.N

num_intersections = pow(2,num_class)


#generate list of possible intersections
int_list = [None]*num_intersections

for i in range(num_intersections):
	int_list[i] = bin(i)[2:].zfill(num_class)[::-1]

int_list.reverse()

bin_num = bin(N-1)[2:].zfill(num_intersections)[::-1]
print bin_num
num_include = bin_num.count('1')

sets = [None]*num_include

# import pdb; pdb.set_trace()

index = [pos for pos, char in enumerate(bin_num) if char == "1"]

# these are the intersections in coded form
final_ints = list(int_list[i] for i in index)

# human readable ints for grep in 2^K bit code

human_ints = [bin(num_intersections-1-int(j,2))[2:].zfill(num_class) 
	for j in final_ints]


print human_ints

# go from human inits to classifier form
# string rotate first
rotate_combs = [x[::-1] for x in human_ints]
print rotate_combs
# now bit flip and add commas
class_form = [','.join('1' if i == '0' else '0' for i in j) for j in rotate_combs]
print class_form

grep_str = '|'.join(class_form)
print grep_str
# for j in range(len(bin_num)):
# 	if bin_num[j] == '1':
# 		sets[j] = int_list[j]
# 		flip_num =  num_intersections-1-int(sets[j],2) 
# 		print flip_num



# def f_numToSets(N,num_class):
# 	num_intersections = pow(2,num_class)


# 	#generate list of possible intersections
# 	int_list = [None]*num_intersections

# 	for i in range(num_intersections):
# 		int_list[i] = bin(i)[2:].zfill(num_class)[::-1]

# 	import pdb; pdb.set_trace()

# 	bin_num = bin(N-1).zfill(num_intersections)[::-1]
# 	print bin_num
# 	num_include = bin_num.count('0')

# 	sets = [None]*num_include

# 	for j in range(len(bin_num)):
# 		if bin_num[j] == '0':
# 			print int_list[j]

