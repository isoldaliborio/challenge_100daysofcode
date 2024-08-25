# paginator
# generator (yield)

"""
Implement a function create_paginator that takes two arguments: 
an array called items, 
and an integer called pageSize. 
The function should return a generator (yield) object that iterates through the elements in the array in pages of the specified size. 
Here, pages refer to the disjoint subarrays of array items of size equal to pageSize.
"""

from typing import Generator, List


def create_paginator(items: list, pageSize: int) -> Generator[List[int], None, None]:
    page = []
    count = 1
    
    for item in items:
        # add to page if count is less than page size
        if count <= pageSize:
            page.append(item)
        
        # last item in page
        if count == pageSize:
            yield page

            # reset page and counter, then go to next item with no counter increment
            page = []
            count = 1
            continue
        
        # increment counter if not last item
        count += 1


paginated = create_paginator(
    items=[1, 2, 3, 4, 5, 6, 7], 
    pageSize=2
)

for page in paginated:
    print(page)