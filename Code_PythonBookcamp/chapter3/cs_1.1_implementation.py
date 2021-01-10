# Seller information
seller_name = " Spencer Retail"
seller_address = " 136, Garia Station Road,\n Kolkata:700084"
seller_contact = "123-456-789"

#Decorating top segment
print("-" * 50)
print(f"{seller_name}")
print(f"{seller_address}")

print("-" * 50)
apricot_price = 300
dates_price = 400
almonds_price = 500
apri_dates_combo = (apricot_price + dates_price) * .9  # 10% discount
dates_almon_combo = (dates_price + almonds_price) * .9  # 10% discount
almon_apri_combo = (almonds_price + apricot_price) * .9  # 10% discount
gift_pack = (apricot_price + dates_price + almonds_price) * .75  # 25% discount
print("Product(s) \tPrice (per pack)")
print(f"Apricot\t\t{apricot_price}")
print(f"Dates\t\t{dates_price}")
print(f"Almond\t\t{almonds_price}")
print(f"Combo-1\t\t{apri_dates_combo}")
print(f"Combo-2\t\t{dates_almon_combo}")
print(f"Combo-3\t\t{almon_apri_combo}")
print(f"GiftBox\t\t{gift_pack}")

# Decorating the bottom segment.
# It contains the contact information.
print("*" * 50)
print(f"For free delivery, contact {seller_contact} ")
print("*" * 50)
