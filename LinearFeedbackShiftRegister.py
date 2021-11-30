
# 4-bit
state=0b1001
result=0
for i in range(20):
	print(f"{state:04b} - {state:02d}")
	newbit = (state ^ (state >> 1)) & 1
	state = (state >> 1) | (newbit << 3)
	result = (result << 1) | newbit

print(f"{result:20b}")

spread=dict()
for i in range(256):
	spread[i]=0

dicespread=dict()
for i in range(7):
	dicespread[i]=0

state=(1<<127)|1 # 1...126x0...1 or just a large number
state=(5938495598)
for j in range(1000000):
	result=0
	for i in range(8):
		# print(state & 1, end="")
		newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
		state = (state >> 1) | (newbit << 127)
		result = (result << 1) | newbit
	# print(f" - {result}")
	spread[result]+=1
	dicespread[result%6+1]+=1

for key, val in spread.items():
	print(f"{key}: {val} - {val%6+1}") 

print(f"Min: {min(spread.values())} Max: {max(spread.values())}")

for key, val in dicespread.items():
	print(f"{key}: {val} - {val%6+1}")