# Pi Prime Palindromes Challenge

I saw this challenge for the first time on sigmageek.com and them I've made some changes on it to make it funnier and reproducible if you don't have 82T of storage space for the first 100 trillion digits of π (pi).

The original challenge has 3 levels:
 - level 1: find the first occurence of an 9-digits palindromic prime contained in the decimal expansion of π (3,1415…).
 - level 2: find the first occurence of an 21-digits palindromic prime contained in the decimal expansion of π (3,1415…).
 - level 3: find the largest palindromic prime contained in the decimal expansion of π (3,1415…), considering the first 100T digits.

For this repo, I've considered the **first 100B digits of π**, because it's easy to download and reproduce the results i've found here.
And the actual tasks for my version of this challenge are:
 - 1: Find the first occurence of all possible length of palindromic prime numbers from 9 contained in the decimal expansion of π (3,1415…).
 - 2: Count the occurences of all possible length of palindromic prime numbers from 9 contained in the decimal expansion of π (3,1415…) and group them by its length.
 - 3: Find the greatest palindromic prime contained in the decimal expansion of π (3,1415…).

You can find the digits [here](https://storage.googleapis.com/pi100t/index.html) in case of you want do reproduce this challenge.

### Notes

 - Since Python is the language I'm more proficient, I had to make some improvements in my code to make it run in a reasonable time window. To do that, I made use of Numpy and Numba to access memory chunks and iterate over them in a more efficient way.

 - If you want to run this code against multiple files, make sure that you are looking for palindromes in the intersection of all files. This is important.

 - My first approach to check for primes was iterate over all possible factor of the palindrome square root, like the following code, but it becomes stale when I faced very large numbers.

```
def is_prime(n):
    return all(n % i for i in range(2, int(n ** 0.5) + 1))
```

## Results

My approach is to access chunks of the file that fits in-memory and iterate over characters in the sequence considering a given distance between elements, in order to find palindromes.Then I check if those palindromes are prime numbers and save the results in a .txt file. 

And finally, I use the jupyter notebook to easily inspect the results and got the answers that we're looking for.

The results that I've found are:
 - 1: Find the first occurence of all possible length of palindromic prime numbers from 9 contained in the decimal expansion of π (3,1415…).
   -  9 digits: 3-182-7-281-3 found at 129,080;
   - 11 digits: 74-670-7-076-47 found at 5,793,498;
   - 13 digits: 102-077-6-770-201 found at 25,803,984;
   - 15 digits: 1-768-606-9-606-867-1 found at 298,503,034;
   - 17 digits: 30-948-834-1-438-849-03 found at 6,604,858,610;
   - 19 digits: 724-042-818-4-818-240-427 found at 72,075,707,768.

 - 2: Count the occurences of all possible length of palindromic prime numbers from 9 contained in the decimal expansion of π (3,1415…) and group them by its length. Consider the first 100B digits.
   -  9 digits: found 516,435 palindromes.
   - 11 digits: found 41,828 palindromes.
   - 13 digits: found 3,524 palindromes.
   - 15 digits: found 305 palindromes.
   - 17 digits: found 29 palindromes.
   - 19 digits: found 2 palindromes.
  
 - 3: Find the largest palindromic prime contained in the decimal expansion of π (3,1415…), considering the first 100B digits.
   - Palindrome: 912-501-055-0-550-105-219 (9,125,010,550,550,105,219)
   - Index: 78,833,628,391