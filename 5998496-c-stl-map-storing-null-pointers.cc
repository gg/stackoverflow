#include <iostream>
#include <map>
#include <string>

struct C {
 C(const std::string& text) : text(text) {}
 std::string text;
};

int main() {
  typedef std::map<std::string, C*> MapType;

  MapType others;
  others["hello"] = new C("hello");
  others["world"] = new C("world");

  MapType elements;

  for (MapType::const_iterator it = others.begin(); it != others.end(); ++it) {
    C* c = it->second;
    std::cout << std::hex << c << std::endl;

    elements[it->first] = c;
    std::cout << std::hex << elements[it->first] << std::endl;
  }
}
