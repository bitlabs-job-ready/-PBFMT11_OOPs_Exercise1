Exercise 1:  
  
   WAP create a Bank class and create following instance methods and static methods into it.

instance methods:
    1. deposite(self)
    2. withdraw(self)
    3. balEnquiry(self)
    4. viewOptions(self)

Static method:
    1. validate(self)



class Bank:
       // declaring and initilizing instance variable called ac_bal
       ac_bal=10000;
    
               // declare deposite(self) method --instance method
               // accept the deposite amount from the user and add it to ac_bal
               // print error message if user entered amount is invalid.[Accept multiples of 100 only]

     
              // declare withdraw(self) method -- instance method
              // accept the withdraw amount from the user and detuct it from the ac_bal 
             // print error message if user entered amount is invalid.[Accept multiples of 100 only]

   
              // declare balEnquiry(self) method   -- instance method
             // print available balance
       
              // declare validate(self) method  -- static method       
             // accept the pin number and call viewOptions() method if pin is correct  else print Error message.

 
       def viewOptions(self):
	print("1. Deposite")
	print("2. Withdraw")
	print("3. Balance Enquiry")
	print("0. Choose your option : ")


bank=Bank()


