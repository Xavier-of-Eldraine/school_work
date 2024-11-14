import string
import hashlib
from time import sleep
def brute_basic(password):
    variations = string.ascii_lowercase
    tries = 0
    for first in variations:
        for second in variations:
            for third in variations:
                for fourth in variations:    
                    tries += 1
                    guess = first+second+third+fourth
                    print(guess, end = '\r')
                    if guess == password:
                        print("Password is:{} \n Total guesses:{}".format(guess,tries), )
                        return

def brute_hash(password):
    hashed_pass = hashlib.md5(password.encode()).hexdigest()

    print("Your hashed pass:{}\n Now let's get cracking!".format(hashed_pass))
    print("Please hold...") 

    variations = string.ascii_lowercase
    tries = 0
    for first in variations:
        for second in variations:
            for third in variations:    
                tries += 1
                guess = first + second + third 
                hashed_guess = hashlib.md5(guess.encode()).hexdigest()
                print(hashed_guess, end = '\r')
                del guess
                trys = 'try'
                if tries > 1:
                    trys = 'tries'
                if hashed_guess == hashed_pass:
                    print("Hash cracked, and it only took {} {}!".format(tries,trys))
                    return
    print("Password not found :(")
    
def md5_hashpass_finder(hash):
    tries = 0
    variations = string.ascii_lowercase + string.punctuation
    for first in variations:
        for second in variations:
            for third in variations:
                for fourth in variations:
                    guess = first + second + third + fourth
                    guess_hashed = hashlib.md5(guess.encode()).hexdigest()
                    tries += 1
                    if guess_hashed == hash:
                        trys = 'try'
                        if tries > 1:
                            trys = 'tries'
                        print("Success, we found a match!:{}\n It took {} {}!".format(guess,tries,trys))
                        return
    print("No luck, sorry.")
                        
    



if __name__ == '__main__':
    chooser = input("Welcome to the program. Your choices are as follows: \n 1)Basic Brute \n 2)Hash Brute \n 3)Hash Reverser\n Your choice(1,2,3): ")
    match chooser:
        case "1":   
            pass2guess = str(input("Choose a 4 letter pass, all lowercase:"))
            brute_basic(pass2guess)
        case "2":
            pass3guess = str(input("Choose a 3 letter pass, all lowercase:"))
            brute_hash(pass3guess)
        case "3":
            userinput = str(input("Give a password to guess, no uppercase, no spaces, 4 characters:"))

            hash2guess = hashlib.md5(userinput.encode()).hexdigest
            print(hash2guess)
            md5_hashpass_finder(hash2guess)
