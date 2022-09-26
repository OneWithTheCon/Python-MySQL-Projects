#Program to read value paise and display it in rupees and paise
Paise=float(input('Enter the Amount in Paise: '))
Rupees=Paise/100
Paise_Remaider=Paise%100
print("The Amount in Paise converted to Rupees is:",int(Rupees),"rupees and",int(Paise_Remaider),"paise")

