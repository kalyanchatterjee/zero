function selection_sort(unsortedArray, startIndex = 0) {
  if (startIndex >= unsortedArray.length) return unsortedArray;

  let temp; // temp variable is needed for swap
  let currentMinValue = unsortedArray[startIndex];
  let currentMinIndex = startIndex;
  for (let i = startIndex + 1; i < unsortedArray.length; i++) {
    if (unsortedArray[i] <= currentMinValue) {
      currentMinValue = unsortedArray[i];
      currentMinIndex = i;
    }
  }
  temp = unsortedArray[startIndex];
  unsortedArray[startIndex] = currentMinValue;
  unsortedArray[currentMinIndex] = temp;
  startIndex++;
  // Recursively call sort
  selection_sort(unsortedArray, startIndex);

  return unsortedArray;
}

console.log(selection_sort([5, 1, 3, 2, 4, -99, -98, -1]));
