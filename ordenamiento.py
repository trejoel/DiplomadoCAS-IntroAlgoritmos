import random

def create_random_vector(size, low=0.0, high=1.0):
    A=[]
    for i in range(size):
        A.append(random.randint(low,high))
    return A

def ordenamientoBurbula(A):
    B=[]
    return B

if __name__ == "__main__":
    size = 10
    # Generate a random vector of size 5 with values between 0 and 1
    A = create_random_vector(size,1,100)
    
    print(f"Vector aleatorio sin ordenar {size}:")
    print(A)