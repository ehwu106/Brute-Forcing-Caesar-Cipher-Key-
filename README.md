# Brute-Forcing-Encrypted-Caesar-Cipher-Message
Simple Python script that brute force the key of an encrypted message with caesar cipher algorithm. Since Caesar Cipher is a weak encryption algorithm, it is not advise to use such algorithm to encrypt your data. This script will try all combinations of keys and using ASCII decimals to determine the appropriate letters to output. 

# Ethics
This is a simple example and demonstration of how one might tackle a bruteforce technique when it comes to penetration testing or just hacking in general. Brute forcing is usually not the most efficient way of doing things. However in a case like this where an algorithm is small enough for us to try every single combination, this technique is relatively a straight forward approach. This is soley for educational purposes, hacking in general is illegal. You should always learn the laws of your state as well as get permissions before testing within a network or machine that is not your own. This script is simply a way for me to learn and an introduction for me to start writing my own scripts to help me tackle Capture the Flag machines in Hack The Box.

# Run
1.) `python encode.py` - Enter your message and key to retrieve the encrypted message.

2.) `python brute.py` - enter the encrypted message and get a lists of brute forced results.

# License
[GNU General Public License v3.0](LICENSE)
