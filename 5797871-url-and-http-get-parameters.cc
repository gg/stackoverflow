#include <iostream>
#include <string>

// Returns the relative Request-URI from url. For example, given the url
// "http://www.google.com/search?q=xyz", it will return "/search?q=xyz".
//
// url need not be prefixed with a protocol; i.e. "google.com" is valid.
//
// If url contains a protocol (i.e. "http://"), the Request-URI begins with the
// first "/" after the protocol. Otherwise, the Request-URI begins with the
// first "/".
//
// If url does not contain a Request-URI, its Request-URI is "/", the server
// root.
std::string ParseRequestUri(const std::string& url) {
  const std::string protocol_identifier("://");

  std::size_t pos = url.find(protocol_identifier);

  if (pos != std::string::npos)
    pos = url.find_first_of("/", pos + protocol_identifier.length());
  else
    pos = url.find_first_of("/");

  if (pos != std::string::npos)
    return url.substr(pos);

  return "/";
}

int main() {
  const std::string test_url = "http://google.com/search?hl=en&source=hp&biw=1422&bih=700&q=blabla&btnG=Google+Search&aq=f&aqi=&aql=&oq=";
  const std::string test_url2 = "example.com/path/to/foo/bar/baz.tar.gz";

  std::cout << ParseRequestUri(test_url) << std::endl;
  std::cout << ParseRequestUri(test_url2) << std::endl;
}
