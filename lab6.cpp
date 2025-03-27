#include <iostream>


double func(int n) {
    static double x = 0;
    if (n == 0) {
        return x;
    }

    x += 1 / static_cast<double>(n);
    return func(n - 1);
}
double func() {
    int n;
    std::cout << "please input a number:";
    std::cin >>n;
   return  func(n);

}


int main() {
   std::cout << func(5);
    std::cout << func();
    return 0;
}
