import os

file_name = 'docker_stats_.log'
some_file_name = 'wc_counter.md'

os.system('tail docker_stats_.log > docker_stats_tail.txt')

os.system('wc -l docker_stats_.log > wc_counter.md')
some_count = open(some_file_name, 'r')
wc_count_file = some_count.split(" ")
print wc_counter
some_count.close()

# file_name_tail = 'docker_stats_tail.txt'
# my_array = []

# with open(file_name_tail) as f:
# 	for el in f:
# 		my_array.append(el)
# f = open(file_name_tail, 'r')
# lines = f.readlines()
# my_array = lines.split('\n')

# counter = 0
# length = len(my_array)

# for el in my_array:
# 	if 'CONTAINER' in el:
# 		counter += 1
# 		my_array.remove(el)

# for el in my_array:
# 	print el

# print "some edit: " + str(counter)
