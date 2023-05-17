a = 0x51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4
b = 0x403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c

#XOR
c=a^b
print("Xor=",hex(c))
#зсув вправо
z=a>>1
print("Shift_right=",hex(z))
#зсув вліво
w=b<<1
print("Shift_left=",hex(w))
#OR
r=a|b
print("OR=",hex(r))
#AND
f=a&b
print("AND=",hex(f))

