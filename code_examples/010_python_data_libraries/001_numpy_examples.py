import numpy as np

# -------------------------------------------------------------
# SECTION 1: ARRAY CREATION
# -------------------------------------------------------------
print("=" * 50)
print("SECTION 1: ARRAY CREATION")
print("=" * 50)

# np.array() — create an array from a list or nested list
arr = np.array([1, 2, 3, 4, 5])
print("\nnp.array()")
print(arr)                          # [1 2 3 4 5]

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix)                       # 2D array

# np.zeros() — array filled with 0.0
print("\nnp.zeros()")
print(np.zeros(4))                  # [0. 0. 0. 0.]
print(np.zeros((3, 2)))             # 3x2 array of 0.0

# np.ones() — array filled with 1.0
print("\nnp.ones()")
print(np.ones(3))                   # [1. 1. 1.]
print(np.ones((5, 2)))              # 5x2 array of 1.0

# np.full() — array filled with a constant value
print("\nnp.full()")
print(np.full(4, 7))                # [7 7 7 7]
print(np.full((2, 3), 3.14))        # 2x3 array of 3.14

# np.arange() — evenly spaced values within a range
print("\nnp.arange()")
print(np.arange(5))                 # [0 1 2 3 4]
print(np.arange(0, 10, 2))          # [0 2 4 6 8]
print(np.arange(1, 6))              # [1 2 3 4 5]

# np.empty() — uninitialised array (values are arbitrary)
print("\nnp.empty()")
print(np.empty(3))                  # arbitrary float values
print(np.empty((2, 2)))             # 2x2 arbitrary values

# np.linspace() — evenly spaced values between two endpoints
print("\nnp.linspace()")
print(np.linspace(0, 1, 5))         # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, 3))        # [ 0.  5. 10.]

# np.fromstring() — array from a delimited string
print("\nnp.fromstring()")
print(np.fromstring('1 2 3 4', dtype=int, sep=' '))     # [1 2 3 4]
print(np.fromstring('1.5,2.5,3.5', dtype=float, sep=','))  # [1.5 2.5 3.5]


# -------------------------------------------------------------
# SECTION 2: ARRAY PROPERTIES
# -------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 2: ARRAY PROPERTIES")
print("=" * 50)

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# np.shape() — dimensions of the array
print("\nnp.shape()")
print(np.shape(arr_2d))             # (3, 4)
print(arr_2d.shape)                 # (3, 4) — also accessible as attribute

# np.size() — total number of elements
print("\nnp.size()")
print(np.size(arr_2d))              # 12 — total elements
print(np.size(arr_2d, 0))           # 3  — size along axis 0 (rows)
print(np.size(arr_2d, 1))           # 4  — size along axis 1 (columns)

# np.dtype — data type of the array elements
print("\nnp.dtype")
print(arr_2d.dtype)                 # int64
print(np.array([1.0, 2.0]).dtype)   # float64
print(np.array([True, False]).dtype)  # bool


# -------------------------------------------------------------
# SECTION 3: ARRAY MANIPULATION
# -------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 3: ARRAY MANIPULATION")
print("=" * 50)

# np.reshape() — change shape without changing data
print("\nnp.reshape()")
arr = np.arange(1, 13)              # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(arr)
reshaped = np.reshape(arr, (3, 4))  # 3 rows, 4 columns
print(reshaped)
reshaped_2 = np.reshape(arr, (2, 6))  # 2 rows, 6 columns
print(reshaped_2)

# np.split() — split array into sub-arrays
print("\nnp.split()")
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(arr, 3)            # Split into 3 equal parts
print(parts)                        # [array([1,2]), array([3,4]), array([5,6])]

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
rows = np.split(arr_2d, 3, axis=0)  # Split into 3 rows
print(rows)

# np.asarray() — convert input to array (no copy if already compatible)
print("\nnp.asarray()")
python_list = [1, 2, 3, 4]
arr = np.asarray(python_list)
print(arr)                          # [1 2 3 4]
print(type(arr))                    # <class 'numpy.ndarray'>

existing_arr = np.array([1.0, 2.0, 3.0])
same_arr = np.asarray(existing_arr) # No copy made — same object in memory
print(same_arr)                     # [1. 2. 3.]


# -------------------------------------------------------------
# SECTION 4: STATISTICAL METHODS
# -------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 4: STATISTICAL METHODS")
print("=" * 50)

scores = np.array([55, 70, 82, 90, 63, 74, 88, 95, 61, 77])

print(f"\nDataset: {scores}")

# np.mean() — arithmetic mean
print("\nnp.mean()")
print(np.mean(scores))              # 75.5

arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60]])
print(np.mean(arr_2d))              # 35.0 — overall mean
print(np.mean(arr_2d, axis=0))      # [25. 35. 45.] — mean per column
print(np.mean(arr_2d, axis=1))      # [20. 50.] — mean per row

# np.sum() — sum of elements
print("\nnp.sum()")
print(np.sum(scores))               # 755
print(np.sum(arr_2d, axis=0))       # [50 70 90] — sum per column
print(np.sum(arr_2d, axis=1))       # [ 60 150] — sum per row

# np.min() — minimum value
print("\nnp.min()")
print(np.min(scores))               # 55
print(np.min(arr_2d, axis=0))       # [10 20 30] — min per column

# np.max() — maximum value
print("\nnp.max()")
print(np.max(scores))               # 95
print(np.max(arr_2d, axis=1))       # [30 60] — max per row

# np.std() — standard deviation
print("\nnp.std()")
print(np.std(scores))               # spread of values around the mean
print(np.std([2, 4, 4, 6]))         # 1.4142...

# np.median() — middle value when sorted
print("\nnp.median()")
print(np.median(scores))            # 75.5
print(np.median([1, 3, 5, 7, 9]))   # 5.0

# np.percentile() — value at a given percentile
print("\nnp.percentile()")
print(np.percentile(scores, 25))    # 25th percentile (Q1)
print(np.percentile(scores, 50))    # 50th percentile (median)
print(np.percentile(scores, 75))    # 75th percentile (Q3)
print(np.percentile(scores, [25, 50, 75]))  # All three at once
