import ctypes

class DynamicArray:

    def _make_array(self, c):
        """Return a new array with capacity `c`."""
        return (c * ctypes.py_object)()
	
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                    
        self._capacity = 1
        self._array = self._make_array(self._capacity) 
        
    def __len__(self):
        """Return the number of element strored in the array."""
        return self._n
    
    def is_empty(self):
        return self._n == 0

    def __str__(self):
        if self.is_empty(): return '[]'
        string = '['
        for i in range(self._n):
            string = '{}{}, '.format(string, self[i]) if i < self._n - 1 else '{}{}'.format(string, self[i]) 
        string = '{}]'.format(string)
        return string

    def __getitem__(self, k):
        """Return the element at index `k`."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._array[k]
    
    def __setitem__(self, k, e):
        """Set index `k` equal to `e`."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        self._array[k] = e
        
    def append(self, e):
        """Add element `e` at the end of the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = e
        self._n += 1
        
    def _resize(self, c):
        """Resize internal array to capacity `c`."""
        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self[i]
        self._capacity = c
        self._array = B

    def remove(self, k):
        obj_to_remove = self[k]
        for i in range(k, self._n-1):
            self[i] = self[i+1] 
        self[self._n-1] = None
        self._n -= 1
        return obj_to_remove

    def pop(self):
        """Return and remove the object on top of the list.
        If the number of object in the list is smaller then 
        a quarter of the the capacity, the array is resized.
        """
        obj = self[self._n-1]
        self.remove(self._n-1)
        if self._n <= self._capacity / 4:
            self._resize(self._capacity // 2)
        return obj

    def find(self, obj):
        """Return the index of `obj` if `obj` is in the list else `None`"""
        for k in range(self._n):
            if self[k] == obj:
                return k
        return None

    def insert(self, obj, k): 
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        self.append(None)
        for i in range(self._n-1, k, -1):
            self[i] = self[i-1]
        self[k] = obj 

if __name__ == '__main__':
    x = DynamicArray()
    for i in range(5): x.append(i)
    print(x)

    print(x.find(4))
    x.insert(9, 2)
    print(x)

    for i in range(6, 2, -1):
        print(i)
    