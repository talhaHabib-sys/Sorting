##17b-048-cs B
## TALHA HABIB

import pandas as pn
d=pn.read_csv('data.csv')

import matplotlib.pyplot as p

import time as t 

def insertionSort(arr): 
  
     
    for i in range(1,len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

def partition(arr,l,h):
   i = ( l - 1 )
   x = arr[h]
   for j in range(l , h):
      if arr[j] <= x:
         
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[h] = arr[h],arr[i+1]
   return (i+1)

def quickSort(arr):
   
   h=len(arr)-1
   l=0
   size = h - l + 1
   stack = [0] * (size)
   
   top = -1
   
   top = top + 1
   stack[top] = l
   top = top + 1
   stack[top] = h
   
   while top >= 0:
      # Pop
      h = stack[top]
      top = top - 1
      l = stack[top]
      top = top - 1
    
      p = partition( arr, l, h )
      
      if p-1 > l:
         top = top + 1
         stack[top] = l
         top = top + 1
         stack[top] = p - 1
      
      if p+1 < h:
         top = top + 1
         stack[top] = p + 1
         top = top + 1
         stack[top] = h 
def mergeSort(a):  
      
    current_size = 1
      
     
    while current_size < len(a) - 1:  
          
        left = 0
         
        while left < len(a)-1:  
              
            
            mid = min((left + current_size - 1),(len(a)-1)) 
              
             
            right = ((2 * current_size + left - 1,  
                    len(a) - 1)[2 * current_size  
                        + left - 1 > len(a)-1])  
                              
             
            merge(a, left, mid, right)  
            left = left + current_size*2
              
        
        current_size = 2 * current_size  
  

def merge(a, l, m, r):  
    n1 = m - l + 1
    n2 = r - m  
    L = [0] * n1  
    R = [0] * n2  
    for i in range(0, n1):  
        L[i] = a[l + i]  
    for i in range(0, n2):  
        R[i] = a[m + i + 1]  
  
    i, j, k = 0, 0, l  
    while i < n1 and j < n2:  
        if L[i] > R[j]:  
            a[k] = R[j]  
            j += 1
        else:  
            a[k] = L[i]  
            i += 1
        k += 1
  
    while i < n1:  
        a[k] = L[i]  
        i += 1
        k += 1
  
    while j < n2:  
        a[k] = R[j]  
        j += 1
        k += 1 

        
    
           






print("WELCOME!")
print("1)open")
print("2)high")
print("3)low")
print("4)Close")
print("Enter your choice")
ina=int(input())
chunk=10000

iteration=int(len(d)/chunk)
if  ina==1:
    p.xlabel('n')
    n=[]
    n2=[]
    n3=[]
    p.ylabel('Time(s)')
    p.title('Comparision')
    op=list(d["Open"])
    a=0
    v1=[]
    v2=[]
    v3=[]
    for i in range(0,iteration):
         n.append(op[0:a+10000])
         a=a+10000
    

  
    for i in range(0,iteration):
        t1=t.time()             
        insertionSort(n[i])
        t2=t.time()
        v1.append(t2-t1)
        
   
    
        
    p.plot(['10000','20000','30000','40000','50000'],v1,'g',label='INSERTION')
    
    
    
    c=0  
    for i in range(0,iteration):
         n2.append(op[0:c+10000])
         c=c+10000
   
    for i in range(0,iteration):
        t3=t.time()
        mergeSort(n2[i])
        t4=t.time()
        
        v2.append(t4-t3)
        
       
    p.plot(['10000','20000','30000','40000','50000'],v2,'r',label='Merge')
    
    
    b=0
    for i in range(0,iteration):
         n3.append(op[0:b+10000])
         b=b+10000
    for i in range(0,iteration): 
        t5=t.time()
        quickSort(n3[i])
        t6=t.time()
        v3.append(t6-t5)

    p.plot(['10000','20000','30000','40000','50000'],v3,'y',label='QUICK')
    p.legend()
    p.savefig('graph1.png',dpi=100)
    p.show()
    print("Have a nice day !")
    
elif  ina==2:
    
    p.xlabel('n')
    n=[]
    n2=[]
    n3=[]
    p.ylabel('Time(s)')
    p.title('Comparision')
    op=list(d["High"])
    a=0
    v1=[]
    v2=[]
    v3=[]
    for i in range(0,iteration):
         n.append(op[0:a+10000])
         a=a+10000
    

  
    for i in range(0,iteration):
        t1=t.time()             
        insertionSort(n[i])
        t2=t.time()
        v1.append(t2-t1)
        
   
    
        
    p.plot(['10000','20000','30000','40000','50000'],v1,'g',label='INSERTION')
    
    
    
    c=0  
    for i in range(0,iteration):
         n2.append(op[0:c+10000])
         c=c+10000
   
    for i in range(0,iteration):
        t3=t.time()
        mergeSort(n2[i])
        t4=t.time()
        
        v2.append(t4-t3)
        
       
    p.plot(['10000','20000','30000','40000','50000'],v2,'r',label='Merge')
    
    
    b=0
    for i in range(0,iteration):
         n3.append(op[0:b+10000])
         b=b+10000
    for i in range(0,iteration): 
        t5=t.time()
        quickSort(n3[i])
        t6=t.time()
        v3.append(t6-t5)

    p.plot(['10000','20000','30000','40000','50000'],v3,'y',label='QUICK')
    p.legend()
    p.savefig('graph2.png',dpi=100)
    p.show()
    print("have a nice day!")
    
         
elif ina==3:
    n=[]
    n2=[]
    n3=[]
    p.xlabel('n')
    p.ylabel('Time(s)')
    p.title('Comparision')
    op=list(d["Low"])
    a=0
    v1=[]
    v2=[]
    v3=[]
    for i in range(0,iteration):
         n.append(op[0:a+10000])
         a=a+10000
    

  
    for i in range(0,iteration):
        t1=t.time()             
        insertionSort(n[i])
        t2=t.time()
        v1.append(t2-t1)
        
   
    
        
    p.plot(['10000','20000','30000','40000','50000'],v1,'g',label='INSERTION')
    
    
    
    c=0  
    for i in range(0,iteration):
         n2.append(op[0:c+10000])
         c=c+10000
   
    for i in range(0,iteration):
        t3=t.time()
        mergeSort(n2[i])
        t4=t.time()
        
        v2.append(t4-t3)
        
       
    p.plot(['10000','20000','30000','40000','50000'],v2,'r',label='Merge')
    
    
    b=0
    for i in range(0,iteration):
         n3.append(op[0:b+10000])
         b=b+10000
    for i in range(0,iteration): 
        t5=t.time()
        quickSort(n3[i])
        t6=t.time()
        v3.append(t6-t5)

    p.plot(['10000','20000','30000','40000','50000'],v3,'y',label='QUICK')
    p.legend()
    p.savefig('graph3.png',dpi=100)
    p.show()
    print("Have a nice day !")
    

elif ina==4:
    n=[]
    n2=[]
    n3=[]
    p.xlabel('n')
    p.ylabel('Time(s)')
    p.title('Comparision')
    op=list(d["Close"])
    a=0
    v1=[]
    v2=[]
    v3=[]
    for i in range(0,iteration):
         n.append(op[0:a+10000])
         a=a+10000
    

  
    for i in range(0,iteration):
        t1=t.time()             
        insertionSort(n[i])
        t2=t.time()
        v1.append(t2-t1)
        
   
    
        
    p.plot(['10000','20000','30000','40000','50000'],v1,'g',label='INSERTION')
    
    
    
    c=0  
    for i in range(0,iteration):
         n2.append(op[0:c+10000])
         c=c+10000
   
    for i in range(0,iteration):
        t3=t.time()
        mergeSort(n2[i])
        t4=t.time()
        
        v2.append(t4-t3)
        
       
    p.plot(['10000','20000','30000','40000','50000'],v2,'r',label='Merge')
    
    
    b=0
    for i in range(0,iteration):
         n3.append(op[0:b+10000])
         b=b+10000
    for i in range(0,iteration): 
        t5=t.time()
        quickSort(n3[i])
        t6=t.time()
        v3.append(t6-t5)

    p.plot(['10000','20000','30000','40000','50000'],v3,'y',label='QUICK')
    p.legend()
    p.savefig('graph4.png',dpi=100)
    p.show()
    print("have a nice day")
    
    
  

