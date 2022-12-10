
#include <iostream>
#include <thread>
#include <mutex>  


using namespace std;


long long int a = 0;
std::mutex mtx;

void foo()
{
    mtx.lock();   
	for (long int i = 1; i <= 5000000000; i++) {
        a += i;
	}
    mtx.unlock();
}
void foo1()
{
    mtx.lock();
	for (long int i = 5000000001; i <= 10000000000; i++) {
        a += i;
	}
    mtx.unlock();
}

int main()
{
	thread th1(foo);
	thread th2(foo1);

    th1.join();
    th2.join();
    cout << a;
	return 0;
}
