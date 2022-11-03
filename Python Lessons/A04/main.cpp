// Cpp program to demonstrate the use of class template
#include <iostream>
using namespace std;
// Class template

class Whatever
{
    private:
    char ch;
    int   x;

    public:
    Whatever();
    Whatever(char ch, int x);
    char getLetter();
    int getValue();
    void setLetter(char ch);
    void setValue(int x);
};

// Constructor
Whatever::Whatever()
{
    this->ch = ch;
    this->x  = x;
}

Whatever::Whatever(char ch, int x)
{
    this->ch = ch;
    this->x  = x;
}

char Whatever::getLetter()
{
    return ch;
}

int Whatever::getValue()
{
    return x;
}

void Whatever::setLetter(char ch)
{
    this->ch = ch;
}

void Whatever::setValue(int x)
{
    this->x = x;
}

int main()
{
    Whatever w21;
    Whatever w1('A', 10);
    Whatever w2('B', 20);
    Whatever w3('C', 30);

    w21.setValue(100);
    cout << "w21: " << w21.getLetter() << " " << w1.getValue() << endl;
    cout << "w1: " << w1.getLetter() << " " << w1.getValue() << endl;
    cout << "w2: " << w2.getLetter() << " " << w2.getValue() << endl;
    cout << "w3: " << w3.getLetter() << " " << w3.getValue() << endl;

    return 0;
}
