guess_count = 0

print('Welcome To Adder Solutions')
ans = input('Do You Have an Account With Us? ').lower()
print('')

if ans == 'no': 
  print('Create An Account Below.')
  print('')
  username = input('Choose Your Username: ')
  passw = input('Password: ')
  conf_pass = input('Confirm Your Password ')

  while passw != conf_pass:
    print('Passwords Do Not Match, Try Again.') 
    
    passw = input('Password: ')
    conf_pass = input('Confirm Your Password ')


  if passw == conf_pass:
    print('')
    print('Account Created Successfully.')
    print('')
            
  else:    
    print('Users passwords did not match')



  user_login = input('Username: ')    
  user_password = input('Password: ')
  


  if user_login == username and user_password == passw and conf_pass:
    print('')
    print('Login Successful!')
    print('')
    print('Welcome to Adder Solutions!')     

  else:
    while guess_count < 2 and user_login != username or user_password != passw and conf_pass:
      print('')
      print('Invalid Username or Password, Try Again')
      guess_count += 1
      user_login = input('Username: ')
      user_password = input('Password: ')
      
      if guess_count == 2 and user_password != passw and conf_pass:
        print('')
        print('Too Many Invalid Entries, Your Account is Now Locked')
        print('')
        print('Goodbye')
        break

      elif user_login == username and user_password == passw and conf_pass:
        print('')
        print('Login Successful!')
        print('')
        print('Welcome to Adder Solutions!') 
        break
       
         
      else:
        
        print('')
        print('Invalid username or password')
        print('')
        print('Please Try Again')
        

elif ans == 'yes':
  print('Enter Username and Password')

  user_login = input('Username: ')
  user_password = input('Password: ')

  print('This Account Does Not Exist.')


#Make it So That If They don't Enter y/n it re-Asks
else:
  #while ans != 'yes' or 'no':
   
      
    print('Invalid Entry, Good-Bye:')

    #ans = input('Do You Have an Account With Us? ').lower()
    #print('')



  


#Add Password Must Include Number in Password
#
#Yes and No Prompt Doesn't Loop Back After Invalid Entry
