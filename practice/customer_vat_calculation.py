# A simple script that calculates total amount and total VAT 
# based on customer data and purchased products

customer_name = 'Admin'
customer_surname = 'Admin Lastname'
customer_number = 111222333
customer_email = 'admin@gmail.com'
customer_city = 'Texas'

product1_name = 'Wireless Mouse'
product1_price = 2000

product2_name = 'Wireless Keyboard'
product2_price = 4500

product3_name = 'Asus ROG Strix G16'
product3_price = 50000

product4_name = 'SteelSeries Arctic Nova 5'
product4_price = 8750

vat_rate = 0.18

total_amount= (
    product1_price +
    product2_price +
    product3_price +
    product4_price
)

total_vat = total_amount * vat_rate

print('Total Amount: ' + str(total_amount))
print('Total VAT: ' + str(total_vat))
