



            
a = [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]

def get_second_element(sublist):
    return sublist[1]

a_sorted = sorted(a, key=get_second_element)

print(a_sorted)



