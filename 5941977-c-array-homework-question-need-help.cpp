#include <cassert>
#include <cstddef>
#include <iostream>
#include <limits>

int findLargest(int array[], std::size_t size) {
  // your code here
  int largest = std::numeric_limits<int>::min();
  for (int i = 0; i < size; ++i) {
    if (array[i] > largest)
      largest = array[i];
  }
  return largest;
}

int main() {
  int test[12] = {3, 5, 7, 10, 4, 2, 9, 1, 0, -23, 10, 8};
  int largest = findLargest(test, 12);
  assert(largest == 10);
}
