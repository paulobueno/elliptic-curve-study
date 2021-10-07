# elliptic-curve-study
The main objective of this repository is to gather knowledge about elliptic curve used in Bitcoin protocol.<br>
1. Create functions that calculate data point's sum operations
2. Use these functions and Bitcoin's parameters to calculate a Public Key based on a Private Key
3. Understand the effort to simply create a relational database of Private Vs Public keys
<br>
Study mainly based on the book <a href='https://www.oreilly.com/library/view/mastering-bitcoin/9781491902639/'>Mastering Bitcoin</a><br>
Other references:<br>
- <a href='https://www.youtube.com/watch?v=F3zzNa42-tQ'>Elliptic Curve Diffie Hellman</a><br>
- <a href='https://www.youtube.com/watch?v=NF1pwjL9-DE'>Elliptic Curves - Computerphile</a><br>
- <a href='https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses'>Modular inverses</a><br>
- <a href='https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc'>Practical Cryptography for Developers</a><br>

# Explanation
## The Equation
![](http://www.plantuml.com/plantuml/png/SoWkIImgoKqioU1oLR1LgDQeqAdKLAXHg8mp0d8huemLj1KIAu14KYsNGsfU2aWb0000)  
![](http://www.plantuml.com/plantuml/png/SoWkIImgoKqioU1Ar4bIoCnJyEPoICrB0Oa00000)  
![](http://www.plantuml.com/plantuml/png/SoWkIImgoKqioU0gIQqeqIZ8pymhKKWiKSZCIylCooofjD9KA4iiAiZ8v798pKi1AGG0)  
![](http://www.plantuml.com/plantuml/png/SoWkIImgoKqioU0oIOmpLj1MC39FYZDIKBHLCE1oICrB0Ka10000)  
![](http://www.plantuml.com/plantuml/png/SoWkIImgoKqioU3ojbA8Yb9IK5B8pKzH0D45N0wfUIaWEG00)  
![](http://www.plantuml.com/plantuml/png/SoWkIImgoKqioU0gKB1LC8epCZLJUDGm6SWoDW8pBCtDkHnIyr90QW00)