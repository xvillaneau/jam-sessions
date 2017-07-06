# Alphabet Cipher

In 1868, Lewis Carroll published an encryption scheme call the 
"Alphabet Cipher" in a children's magazine.

The Alphabet Cipher is a variant of a Caesar cipher, which uses letter
substitution to encrypt a message.  The Alphabet Cipher relies on a
table of letters called a "tabula recta" in which each row contains the
entire alphabet, shifted over by one position for each new row.  The
result looks like:

```
   ABCDEFGHIJKLMNOPQRSTUVWXYZ
 A abcdefghijklmnopqrstuvwxyz A
 B bcdefghijklmnopqrstuvwxyza B
 C cdefghijklmnopqrstuvwxyzab C
 D defghijklmnopqrstuvwxyzabc D
 E efghijklmnopqrstuvwxyzabcd E
 F fghijklmnopqrstuvwxyzabcde F
 G ghijklmnopqrstuvwxyzabcdef G
 H hijklmnopqrstuvwxyzabcdefg H
 I ijklmnopqrstuvwxyzabcdefgh I
 J jklmnopqrstuvwxyzabcdefghi J
 K klmnopqrstuvwxyzabcdefghij K
 L lmnopqrstuvwxyzabcdefghijk L
 M mnopqrstuvwxyzabcdefghijkl M
 N nopqrstuvwxyzabcdefghijklm N
 O opqrstuvwxyzabcdefghijklmn O
 P pqrstuvwxyzabcdefghijklmno P
 Q qrstuvwxyzabcdefghijklmnop Q
 R rstuvwxyzabcdefghijklmnopq R
 S stuvwxyzabcdefghijklmnopqr S
 T tuvwxyzabcdefghijklmnopqrs T
 U uvwxyzabcdefghijklmnopqrst U
 V vwxyzabcdefghijklmnopqrstu V
 W wxyzabcdefghijklmnopqrstuv W
 X xyzabcdefghijklmnopqrstuvw X
 Y yzabcdefghijklmnopqrstuvwx Y
 Z zabcdefghijklmnopqrstuvwxy Z
   ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Process

The encryption process works as follows:
1) Choose a key phrase.  This is shared between the message sender
and the message receiver ahead of time.

```
PYTHON IS GREAT
```

2) Choose a plaintext message you wish to encrypt.

```
NEXT THURSDAY AT SEVEN THIRTY
```

3) Write the letters of the key phrase above the letters of the
plaintext message, repeating the key phrase as many times as necessary.

```
PYTHONISGREATPYTHONISGREA
NEXTTHURSDAYATSEVENTHIRTY
```

4) Using the table, look up the column for each letter in the key
phrase and the row for each corresponding letter in the plaintext, and
write the letter in that position below the plaintext message.

```
PYTHONISGREATPYTHONISGREA
NEXTTHURSDAYATSEVENTHIRTY
CCQAHUCJYUEYTIQXCSABZOIXY
```

5) Send the bottom row (the ciphertext) to the receiver. The receiver
simply reverses the steps above using the pre-shared key phrase to
decode the message.

## Coding Exercise

### Step 1:
Write a program to encode an arbitrary message given a pre-selected key
phrase.

### Step 2:
Modify your program to also decode messages that have been encoded by
your program.  
Bonus: Try giving a ciphertext and key phrase to someone else nearby
and testing whether each of your encoding / decoding programs works.

### Step 3 (Advanced):
It's been shown that these types of encryption schemes are vulnerable
to several types of cryptanalysis attacks.  Write a program to attempt
to find possible keys for a given ciphertext and use those keys to try
to decode the message.

### BONUS SECRET MESSAGE:
- Key Phrase:  PYATLJAMSESSION
- Cipher Text: LFAMTBTTWEAJADRTBVXWXCULCGXIBHCJAWPWSISPDGE
