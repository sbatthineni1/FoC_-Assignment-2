from ast import While
import hashlib
import string
import itertools

def input_method(Inputfile):
  with open(Inputfile) as input:
    lines = input.readlines()
  const=[]
  for Input in lines:
    const.append(Input.split('\n')[0])
  return const

UID =  input_method('UID.txt')
Password = input_method('Password.txt')
Hash = input_method('Hash.txt')
Salt = input_method('Salt.txt')

class CrackerSystem():
  def SaltedHash(input,UIDval):
    return input.data[UIDval]['Password']+input.data[UIDval]['Salt']

  def HashValue(input,UIDval):
    m = hashlib.md5()
    inputstr = CrackerSystem().SaltedHash(UIDval)
    m.update(inputstr.encode("utf-8"))
    return m.hexdigest()
 

  def __init__(input):
    input.data = {}
    for Input in range(len(UID)):
      input.data.update({UID[Input]:{'Salt':Salt[Input],'Password':Password[Input],'Hash':Hash[Input]}})

  def Verify(input, UIDval):
    hashval = CrackerSystem().HashValue(UIDval)
    if input.data[UIDval]['Hash'] ==  hashval:
      print('UID: {},Password: {}, Salt: {},Hash: {}, GeneratedHash: {}'.format(UIDval,input.data[UIDval]['Password'],input.data[UIDval]['Salt'],input.data[UIDval]['Hash'],hashval))
      print('The input password and salt matches the hash value in the database')
    else:
      print('The input password and salt does not match the hash value in the database')
  
class Cracker():
  def __init__(input):
    chars = '0123456789'
    input.passwords=[]
    input.salts=[]
    input.data = {}
    
    for Count in itertools.product(chars, repeat=4):
      input.passwords.append(''.join(Count))
      if ''.join(Count) == '1000':
        break
      
    for Count in itertools.product(chars, repeat=3):
      input.salts.append(''.join(Count))
      if ''.join(Count) == '100':
        break

    for Input in range(len(UID)):
      input.data.update({UID[Input]:{'Salt':Salt[Input],'Password':Password[Input],'Hash':Hash[Input]}})

  def HashValue(input,UIDval):
    for password in input.passwords:
      for salt in input.salts:
        inputstr = password+salt
        m = hashlib.md5()
        m.update(str(inputstr).encode("utf-8"))
        hashval = m.hexdigest()
        if hashval == input.data[UIDval]['Hash']:
            print('Password:{},\nSalt:{},\nHash:{}\n'.format(password,salt,hashval))
            break
        
def main():
  checker = 'True'
  vs = CrackerSystem()
  while checker == 'True':
    UIDval = input('Please Enter the UID for generating the Hash: ')
    vs.Verify(UIDval)
    checker=input('\nType True / False for verifing the UID: ')

  checker = 'True'
  while checker == 'True':  
    cr = Cracker()
    UIDval = input('Please Enter the UID for generating the Hash: ')
    cr.HashValue(UIDval)
    checker=input('\nType True / False for verifing the UID: ')

if __name__ == "__main__":
    main()