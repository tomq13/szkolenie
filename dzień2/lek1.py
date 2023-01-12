import functools
import heapq

heap = []
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 5)
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 4)
# print(heapq.nsmallest(3, heap))
# print(heap)


# def push(*args, **kwargs):
#     return heapq.heappush(heap, *args, **kwargs)


push = functools.partial(heapq.heappush, heap)
smallest = functools.partial(heapq.nsmallest, iterable=heap)
lambda_push = lambda x: heapq.heappush(heap, x)

push(1)
push(3)
push(5)
push(4)
push(2)
print(smallest(3))
print(heap)
