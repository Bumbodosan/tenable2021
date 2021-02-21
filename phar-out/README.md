# Phar Out!  

> 125 points

Find the vulnerability using the provided source code. Dockerfile included.

Exploit the vulnerability in http://challenges.ctfd.io:30455 to recover the flag. Please, no scanners, brute force, DoS against the live site.

Server is Ubuntu/Apache2/PHP7.4



## Solution

Create a PHAR that "acts" like it includes an instance of the Wrapper class.

The embedded PHP gets executed with the malicious code, which prompts PHP to print the flag.

### Flag
```
flag{scooby}
```
https://pentest-tools.com/blog/exploit-phar-deserialization-vulnerability/