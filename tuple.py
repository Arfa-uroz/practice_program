"""Given an integer,n, and  n space-separated integers as input, create a tuple ,t , of those n integers. 
Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported."""

if __name__ == '__main__':
    n = int(input())      #n number of elements in tuple
    integer_list = map(int, input().split())     #n spaced  integer elements in tuple
    t = tuple(integer_list)
    print(t)                  #converts the list into a tuple
    print(hash(t))                           #hash() encodes the given argument