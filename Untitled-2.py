"""Cyber Security"""
# This example file uses some Python modules
import hashlib
import string

# region: Example Code
# You don't need to edit anything in this section, but you can to see how
# things work.
# - Also, notice the 'region:' and 'endregion:' comments.
#   These let you hide segments of code easily. Hover the mouse between the
#   line number and where the region starts to see a dropdown arrow to hide/show
#   the lines of text within the region. (Only works in VS Code)

def basic_brute_force():
    """Show simplified brute force.

    When brute forcing 10 variations then there is a 1 in 10 (1/10=10%) chance
    that you will find the password immediately.
    When brute forcing 100 variations then there is a 1 in 100 (1/100=1%) chance
    that you will find the password immediately.
    When brute forcing 1,000 variations then there is a 1 in 1,000 (1/1,000=0.1%) chance
    that you will find the password immediately.

    As you can see, the chance of finding a password quickly shrinks based on
    the total number of variations you have to try. This is why brute forcing
    long passwords is so slow.

    Example output of this function:
    Guessing: aaa
    Guessing: aab
    Guessing: aac
    Guessing: aad
    ...
    Guessing: car
    Guessing: cas
    Guessing: cat
    We found it after 1372 tries!
    """
    secret_password = 'aaa' # Simple short password as an example
    # Now imagine we don't know what this password is, but we somehow learn that
    # it is only 3 characters long, and of only lowercase characters.
    # So, we just need to brute force all the lowercase letters of the alphabet.
    # Python has a list of lowercase letters in the 'string' module:
    variations = string.ascii_lowercase # a-z
    total_tries = 0 # Keep track of how often we guessed
    for first_letter in variations:
        for second_letter in variations:
            for third_letter in variations:
                password_guess = first_letter + second_letter + third_letter
                total_tries += 1 # Add 1 more guess to total
                print("Guessing: {}".format(password_guess))
                if password_guess == secret_password:
                    print("We found it after {} tries!".format(total_tries))
                    return # Don't keep looping anymore

    # If the above return was never reached, then this print statement will run
    print("Password not found!")

    # How many total variations of 3 lowercase letters are there?
    # Remember, to find total iterations of nested loops, you multiply by each
    # iteration length.
    # We have 3 nested loops that each have the same number of iterations.
    # The number of lowercase characters is 26 so we have 26 * 26 * 26 = 17,576
    # total variations.
    # Try changing secret_password to 'zzz', which is the last password it would
    # guess, to see the total variations for yourself.


def hash_brute_force():
    """Show brute forcing to crack a hashed password.

    A hash is when you convert text into a short string of text that is a
    constant length. It is one-way, as in you can't convert the hash back into
    the text, unlike with encryption.

    Hashes are useful when you want to see if two things are equal, but don't
    care about storing the actual things. So, programs can store the hashed
    version of a password because they only need to check if a password matches,
    they never print out the password (at least in principle).

    There are different types of hashing algorithms. This example uses MD5 which
    is NOT secure because it frequently has collisions. Collisions are where two
    very different words/text end up with the same hash.
    See https://www.mscs.dal.ca/~selinger/md5collision/ if you are interested.

    Here's some examples of MD5 hashes:
    Text        MD5 Hash
    cat         d077f244def8a70e5ea758bd8352fcd8
    dog         06d80eb0c50b49a509b49f2424e8c805
    secret      5ebe2294ecd0e0f08eab7690d2a6ee69
    P@ssw0rd!   8a24367a1f46c141048752f2d5bbd14b

    Example output of this function:
    The hash of 'cat' is: d077f244def8a70e5ea758bd8352fcd8
    Guessing: aaa - 47bce5c74f589f4867dbd57e9ca9f808
    Guessing: aab - e62595ee98b585153dac87ce1ab69c3c
    Guessing: aac - a9ced3dad556814ed46042de696e1849
    ...
    Guessing: car - e6d96502596d7e7887b76646c5f615d9
    Guessing: cas - f90721c90de9bd9ef516bea0b184fd30
    Guessing: cat - d077f244def8a70e5ea758bd8352fcd8
    The password must be cat, we found it after 1372 tries!
    """
    secret_password = 'cat' # Simple short password as an example
    # Get the hash that would be stored by a program
    hash = hashlib.md5(secret_password.encode()).hexdigest()
    print("The hash of {!r} is: {}".format(secret_password, hash))
    del secret_password # Delete it so we aren't tempted to use it below

    variations = string.ascii_lowercase # a-z
    total_tries = 0 # Keep track of how often we guessed
    for first_letter in variations:
        for second_letter in variations:
            for third_letter in variations:
                password_guess = first_letter + second_letter + third_letter
                hash_guess = hashlib.md5(password_guess.encode()).hexdigest()
                total_tries += 1 # Add 1 more guess to total
                print("Guessing: {} - {}".format(password_guess, hash_guess))
                # We compare the hashes, since we normally won't know the secret_password
                if hash_guess == hash:
                    print("The password must be {}, we found it after {} tries!".format(
                        password_guess, total_tries))
                    return # Don't keep looping anymore

    # If the above return was never reached, then this print statement will run
    print("Password not found!")

# endregion: Example Code


def crack_password(hash):
    """Write logic here to return the password that matches the given MD5 hash.

    This time brute force lowercase passwords of 4 characters instead of 3.

    Example:
    crack_password('36846677e3a8f4c0b16d8bdf8ef18608') -> 'duck'
    """
    password = 'duck'

    # Do logic here to find the password
    # You will probably have some code similar to the following:
    # if hash_guess == hash:
    #     password = password_guess
    #     return password # to prevent looping

    return password

# If you want, try and crack passwords that have symbols too.
# For example a password of 3 characters with lowercase and an @ sign has hash: 5725a8290947652ee1b966765c25f2f5
# Can you figure out the password? (not required for points)


if __name__ == '__main__':
    # You can add/remove a '#' before each line to toggle whether to run each
    # function when you run the file.
    basic_brute_force()
    #hash_brute_force()
   # password = crack_password('36846677e3a8f4c0b16d8bdf8ef18608')
   # print("Cracked password: {} (should be duck)".format(password))
