
## How does it work


It generates a random key of 30 lowercase letters and concatenates them into a single string. Then it splits the key into 6-letter parts and creates a list of these parts called `key_parts`. It also joins the key parts into a single string separated by dashes, creating a formatted key called `key_formatted`. After that, it calculates a random number between 1 and 25 based on the 2nd and 30th letters of the key called `rnd_key`. It takes the absolute difference between their positions in the alphabet string, adds 1 to each position to get a number between 1 and 26, then takes the absolute difference between those two numbers to calculate a variable called `key_var` based on the random number calculated above. It takes the letter at the position specified by the random number in the key, finds its position in the alphabet string, and adds 1 to get a number between 1 and 26 again. The `encoding_factor` calculates an encoding factor based on the 19th letter of the key and the `key_var` variable. It finds the positions of these letters in the alphabet string, adds 1 to each position, and then adds those two numbers together to get the encoding factor. For every single character of the input text, it multiplies the number corresponding to each letter (for example `a=1 - b=2 - c=3` etc.) with the `encoding_factor` and prints it out. The key and the numbers generated are used to decrypt the original text


## How to run the script

Clone the project

```bash
  git clone https://github.com/4r1ss/Encryption-Algorithm
```

Go to the project directory

```bash
  cd Encryption-Algorithm
```

Install dependencies

```python
  pip install ttkthemes
```

Run the script

```python
  python EncryptionAlgorithm.py
  python DecryptionAlgorithm.py
```
## Authors

- [@4r1ss](https://github.com/4r1ss)


