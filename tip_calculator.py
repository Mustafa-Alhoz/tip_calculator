print('''
  o        o                                            o                            o                 o                             
 <|>     _<|>_                                         <|>                          <|>               <|>                            
 < >                                                   / \                          / \               < >                            
  |        o    \o_ __o            __o__     o__ __o/  \o/      __o__   o       o   \o/     o__ __o/   |        o__ __o    \o__ __o  
  o__/_   <|>    |    v\          />  \     /v     |    |      />  \   <|>     <|>   |     /v     |    o__/_   /v     v\    |     |> 
  |       / \   / \    <\       o/         />     / \  / \   o/        < >     < >  / \   />     / \   |      />       <\  / \   < > 
  |       \o/   \o/     /      <|          \      \o/  \o/  <|          |       |   \o/   \      \o/   |      \         /  \o/       
  o        |     |     o        "           o      |    |    "          o       o    |     o      |    o       o       o    |        
  <\__    / \   / \ __/>         _\o__</    <\__  / \  / \    _\o__</   <\__ __/>   / \    <\__  / \   <\__    <\__ __/>   / \       
                \o/                                                                                                                  
                 |                                                                                                                   
                / \                                                                                                                 

''')

print("\nWELCOME TO THE TIP CALCULATOR")
print("\nTHIS GAME WAS MADE BY THE BEST PROGRAMMER EVER ===> @mustafa_alhoz ")
bill_amount=float(input("\nplease enter your bill amount: "))
tip_percentage=float(input("\nplease enter the tip percentage you want to give: "))
people_number=float(input("\nplease enter the number of people you want to share the bill with: "))
each_person_payment=float(((bill_amount*tip_percentage/100)+bill_amount)/people_number)
print(f"\neach person have to pay {each_person_payment} dollars")

