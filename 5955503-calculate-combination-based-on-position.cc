#include <cstddef>
#include <iostream>
#include <string>
#include <boost/lexical_cast.hpp>
#include <boost/math/special_functions/binomial.hpp>


std::size_t Choose(double n, double k) {
  using boost::math::binomial_coefficient;
  if (n < k) return 0;
  return static_cast<std::size_t>(binomial_coefficient<double>(n, k));
}

// Returns the largest n such that Choose(n, k) <= pos.
int CombinationElement(int k, int pos) {
  int n = k;
  int coeff = 1, prev_coeff = 0;

  while (coeff <= pos) {
    coeff = Choose(++n, k);
    prev_coeff = coeff;
  }

  return n - 1;
}

// Returns an k-combination at position pos.
std::vector<int> Combination(int k, int pos) {
  std::vector<int> combination;
  for (; k > 0; --k) {
    int n = CombinationElement(k, pos);
    combination.push_back(n);
    pos -= Choose(n, k);
  }
  return combination;
}

int main(int argc, char** argv) {
  using std::cout;
  using std::endl;

  if (argc != 3) {
    cout << "Usage:  $ " << argv[0] << " K POS" << endl;
    cout << "Prints the K-combination at position POS." << endl;
    return 1;
  }

  int k = boost::lexical_cast<int>(argv[1]);
  int pos = boost::lexical_cast<int>(argv[2]);

  std::vector<int> combination = Combination(k, pos);

  for (int i = 0; i < k; i++)
    cout << combination[i] << " ";
  cout << std::endl;
}
