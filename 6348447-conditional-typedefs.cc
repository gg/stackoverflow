template<int region>
struct Decider;

template<>
struct Decider<1> {
  typedef TSA TS;
  typedef FSA FS;
};

template<>
struct Decider<2> {
  typedef TSB TS;
  typedef FSB FS;
};
