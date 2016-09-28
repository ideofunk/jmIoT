// practicing using overloaded functions
// averages two numbers

#include <iostream>

using namespace std;

int average (int, int);
long average (long, long);
float average (float, float);

int main()
{
    float input1, input2, answer;
    
    std::cout << "First number: ";
    std::cin >> input1;
    std::cout << "Second number: ";
    std::cin >> input2;
    answer = average(input1, input2);
    std::cout << "Average is: ";
    std::cout << answer << '\n';
    return 0;
}

int average (int input1, int input2)
{
    int answer;
    answer = (input1 + input2) / 2;
    return answer;
}
long average (long input1, long input2)
{
    long answer;
    answer = (input1 + input2) / 2;
    return answer;
}
float average (float input1, float input2)
{
    float answer;
    answer = (input1 + input2) / 2;
    return answer;
}

