import os

# Read and prep the input
input_file = os.path.join(os.path.dirname(__file__), '2-in.txt')
passwords = []
with open(input_file, encoding='utf-8') as f:
    for line in f:
        passwords.append(line)

passwords_new = []
for password in passwords:
    password = password.split()
    password[0] = [int(x) for x in password[0].split('-')]
    password[1] = password[1][:1]
    passwords_new.append(password)
passwords = passwords_new

# Part 1
def is_valid_password(password):
    count = password[2].count(password[1])
    return count <= password[0][1] and count >= password[0][0]

def count_valid(validity):
    nbr_valid = 0
    for password in passwords:
        nbr_valid += validity(password)
    return nbr_valid

print(count_valid(is_valid_password))

# Part 2
def is_valid_password_2(password):
    return ((password[2][password[0][0] - 1] == password[1]) + (password[2][password[0][1] - 1] == password[1])) == 1

print(count_valid(is_valid_password_2))
