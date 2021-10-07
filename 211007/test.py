import mmap
import time
import numpy as np

mm = mmap.mmap(-1, 0x100000, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0)
arr = np.ndarray((0x100000), np.uint8, mm)

t_st = time.time()
li = arr
t_en = time.time()
t_map = t_en - t_st
print("4M mapping time :", t_map)

t_st = time.time()
li = arr.copy()
t_en = time.time()
t_copy = t_en - t_st
print("4M copying time :", t_copy)

print("mapping is {} time faster than copying".format(t_copy // t_map))

mm.close()
