const sort = (unsorted_list) => {
  if (unsorted_list.length === 0 || unsorted_list.length === 1) {
    return unsorted_list;
  }

  for (i = 1; i < unsorted_list.length; i++) {
    k = i;
    while (k > 0) {
      if (unsorted_list[k] < unsorted_list[k - 1]) {
        temp = unsorted_list[k - 1];
        unsorted_list[k - 1] = unsorted_list[k];
        unsorted_list[k] = temp;
      }
      k--;
    }
  }

  return unsorted_list;
};

console.log(sort([]));
console.log(sort([1]));
console.log(sort([5, 3, 2, 1, 6, 7, 4, -9]));
