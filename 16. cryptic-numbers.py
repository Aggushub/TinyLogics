#TCS TAG Qn #1
'''
🕵️‍♂️🔐 The Enigma of the Cryptic Number 🔐🕵️‍♂️

In the ancient digital kingdom of Numeria, there existed a secret order known as
The Keepers of the Crypt.

They believed that not every number was worthy of carrying hidden meaning.
Only a rare few possessed the qualities of secrecy, strength, and unpredictability.

These were called — Cryptic Numbers.

To identify one, the Keepers followed four sacred laws:

⚔️ Law 1: A Cryptic Number must never mirror itself.
        If it reads the same forward and backward,
        it is predictable — and predictability is weakness.
        (It must NOT be a palindrome.)

🧬 Law 2: No digit may repeat.
        A number that repeats itself cannot guard secrets.
        Every digit must stand alone, unique and independent.

🪙 Law 3: It must be aligned with the Power of Seven.
        Only numbers divisible by 7 resonate with the ancient frequency.

🚫 Law 4: It must reject the Mark of Five.
        Any number divisible by 5 is considered corrupted
        and must be discarded.

When two boundaries are declared — L and R —
the Keepers scan every number between them.

Those that survive all four trials are gathered into a sacred list:
The List of Cryptic Numbers.

Now the task falls to you, Seeker.

Given two integers L and R,
identify every number within this range that passes all four trials.

Return them.

For only the worthy shall be called Cryptic.
'''
def cryptic_numbers(l, r):
    result = []
    
    for n in range(l, r + 1):
        s = str(n)
        
        if (
            s != s[::-1] and                 # not palindrome
            len(set(s)) == len(s) and        # unique digits
            n % 7 == 0 and                   # divisible by 7
            n % 5 != 0                       # not divisible by 5
        ):
            result.append(n)
    
    return result