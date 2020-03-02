# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60):
  from random import randrange
  train = list()
  train_size = split * len(dataset)
  dataset_copy = list(dataset)
  while len(train) < train_size:
    index = randrange(len(dataset_copy))
    train.append(dataset_copy.pop(index))
  return train, dataset_copy

# Split a dataset into $k$ folds
def cross_validation_split(dataset, folds=3):
  from random import randrange
  dataset_split = list()
  dataset_copy = list(dataset)
  fold_size = int(len(dataset) / folds)
  for i in range(folds):
    fold = list()
    while len(fold) < fold_size:
      index = randrange(len(dataset_copy))
      fold.append(dataset_copy.pop(index))
    dataset_split.append(fold)
  return dataset_split
