using namespace std;
#include <iostream>
#include <ctime>
#include <vector>
vector<int> global_array;

int fact(int n){
    if (n == 1 or n == 0)
    {
        return 1;
    } else{
        return fact(n-1) + fact(n-2);
    }
}

int fast_fact(int n){
    if( global_array[n] != 0){
        return global_array[n];
    }
    
    if (n == 1 or n == 0)
    {
        return 1;
    } else{
        global_array[n] = fast_fact(n-1) + fast_fact(n-2);
        return global_array[n];
    }
}

int main(int argc, char const *argv[])
{
    int n1 = 20;
    cout << n1 << endl;
    global_array.resize(n1);
    clock_t t1 = clock();
    fact(n1);
    clock_t t2 = clock();
    cout << "fact: " << t2 - t1 << endl;
    clock_t t3 = clock();
    fast_fact(n1);
    clock_t t4 = clock();
    cout << "fast_fact: " << t4 - t3 << endl;

    int n2 = 40;
    cout << n2 << endl;

    global_array.resize(n2);
    clock_t t5 = clock();
    fact(n2);
    clock_t t6 = clock();
    cout << "fact: " << t6 - t5 << endl;
    clock_t t7 = clock();
    fast_fact(n2);
    clock_t t8 = clock();
    cout << "fast_fact: " << t8 - t7 << endl;
    
    return 0;
}
