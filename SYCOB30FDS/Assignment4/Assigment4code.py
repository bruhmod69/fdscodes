def accept(A):
    n=int(input("enter the size of the array"))
    for i in range (n):
        x=int(input("enter the element"))
        A.append(x)

def display(A):
    print("the array is")
    for i in range (len(A)):
        print(A[i])


def selection(A):
    n=len(A)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if(A[j]<A[min_index]):
                min_index=j
        temp=A[i]
        A[i]=A[min_index]
        A[min_index]=temp
    return A

def bubble(A):
    n=len(A)
    for count in range(n):
    
        for i in range(n-1):
            if(A[i]>A[i+1]):
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
    return A

def main():
    fds=[]
    accept(fds)
    display(fds)
    print("the sorted array is")
    print(selection(fds))
    print("the sorted array by bubble sort is \n", bubble(fds))

main()
