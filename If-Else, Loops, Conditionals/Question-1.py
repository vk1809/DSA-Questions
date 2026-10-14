# FizzBuzz Leetcode 412

def fizzBuzz(self, n: int) -> list[str]:
        ans = [0] * (n)
        x = 1
        for i in range(1,n+1):
            ans[i-1] = str(x)
            if i%3 == 0 and i % 5 == 0:
                ans[i-1] = "FizzBuzz"
            elif i%5 == 0:
                ans[i-1] = "Buzz"
            elif i%3 == 0:
                ans[i-1] = "Fizz"

            x=x+1

        return ans 