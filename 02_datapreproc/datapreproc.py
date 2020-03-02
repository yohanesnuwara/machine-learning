# Find the min and max values for each column
def dataset_minmax(dataset):
  minmax = list()
  for i in range(len(dataset[0])):
    col_values = [row[i] for row in dataset]
    value_min = min(col_values)
    value_max = max(col_values)
    minmax.append([value_min, value_max])
  return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
  for row in dataset:
    for i in range(len(row)):
      row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Calculate mean
def mean(numbers):
  return sum(numbers)/float(len(numbers))

# Calculate column mean
def column_mean(dataset):
  mean_col = [(mean(column)) for column in zip(*dataset)]
  # del(mean_col[-1])
  return mean_col

# Calculate the standard deviation of a list of numbers
def stdev(numbers):
  from math import sqrt
  avg = mean(numbers)
  variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
  return sqrt(variance)

# Calculate column standard deviation
def column_stdev(dataset):
  stdev_col = [(stdev(column)) for column in zip(*dataset)]
  # del(stdev_col[-1])
  return stdev_col

# standardize dataset
def standardize_dataset(dataset, means, stdevs):
  for row in dataset:
    for i in range(len(row)):
      row[i] = (row[i] - means[i]) / stdevs[i]
