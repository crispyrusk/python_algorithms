

def set_of_subsets(num_elements):
  if (num_elements == 0):
    return [[]]
  prev = set_of_subsets(num_elements - 1)
  return prev + [[num_elements-1]+x for x in prev ]

if __name__ == "__main__":

    test_4 = set_of_subsets(4)
    print(test_4)
    print(len(test_4))
    print(2**4)
    
    
    test_5 = set_of_subsets(5)
    print(test_5)
    print(len(test_5))
    print(2**5)
	
    test_10 = set_of_subsets(10)
    print(test_10)
    print(len(test_10))
    print(2**10)
