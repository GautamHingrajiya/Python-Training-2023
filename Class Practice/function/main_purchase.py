import logic

product_name =input("product Name : ")
category =  input("product category : ")
qty = int(input("Qty : "))
price = int(input("price : "))

print(logic.purchase(product_name,category,qty,price))
