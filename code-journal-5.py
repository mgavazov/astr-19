import numpy as np 

def main():
	x = np.linspace(0.0, 2*np.pi, num=1000) #tabulate 0 and 2pi with 1000 entries
	sinx = np.sin(x)

	#organizing table
	print("  x   | sin(x)") 
	print("--------------")

	#loop that prints out 1000 values for x and sin(x)
	for i in range(1000):
		print(f"{x[i]:.3f} | {sinx[i]:.3f}")

if __name__ == '__main__':
	main()
