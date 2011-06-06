#include <stdio.h>

class Base
{
public:
    virtual int f(int) =0;
    virtual int f(){ return f(0); }

    virtual ~Base(){ }
};

class Derived : public Base
{
public:
    int f(int i)
    {
        return (10 + i);
    }

    // without a using statement, Base::f is hidden
    using Base::f;
};

int main(void)
{
    Derived obj;
    printf("%d\n", obj.f(1));// This works, and returns 11
    printf("%d\n", obj.f()); // Adding this line gives me the error listed below
}
