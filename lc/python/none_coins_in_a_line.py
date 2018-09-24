#!/usr/bin/python -t

#leetcode: clean code hand book #47

def max_money(nums):
'''
input list
output int
'''
    m = len(nums)
    l = [0]*100
    l = l[0] * 100

    for i in range(m):
        for j,k in range(m) and range(i, m):
            if j >= m or k >=m:
                break
            a = l[j+2][k] if j+2<=m-1 else 0
            b = l[j+1][k-1] if j+1<=m-1 and k-1>= 0 else 0
            a = l[j][k-2] if z-2>= 0 else 0
            l[j][k] = max(nums[j]+min(a,b), nums[k]+min(b,c))

    return l[0][m-1]



const int MAX_N = 100;
void printMoves(int P[][MAX_N], int A[], int N) {
int sum1 = 0, sum2 = 0;
int m = 0, n = N-1;
bool myTurn = true;
while (m <= n) {
int P1 = P[m+1][n]; // If take A[m], opponent can get...
int P2 = P[m][n-1]; // If take A[n]
cout << (myTurn ? "I" : "You") << " take coin no. ";
if (P1 <= P2) {
cout << m+1 << " (" << A[m] << ")";
m++;
} else {
cout << n+1 << " (" << A[n] << ")";
n--;
}
cout << (myTurn ? ", " : ".\n");
myTurn = !myTurn;
}
cout << "\nThe total amount of money (maximum) I get is " << P[0][N-1] << ".\n";
}
int maxMoney(int A[], int N) {
int P[MAX_N][MAX_N] = {0};
int a, b, c;
for (int i = 0; i < N; i++) {
for (int m = 0, n = i; n < N; m++, n++) {
assert(m < N); assert(n < N);
a = ((m+2 <= N-1) ? P[m+2][n] : 0);
b = ((m+1 <= N-1 && n-1 >= 0) ? P[m+1][n-1] : 0);
c = ((n-2 >= 0) ? P[m][n-2] : 0);
P[m][n] = max(A[m] + min(a,b),
A[n] + min(b,c));
}
}
printMoves(P, A, N);
return P[0][N-1];
}
