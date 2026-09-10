def main():
    print("=== ยินดีต้อนรับสู่ร้าน Cafe ===")
    
    # เมนูเครื่องดื่ม
    drinks = {
        1: ("มัจฉะดูไบช็อกโกแล็ต", 80),
        2: ("เอสเพรสโซ", 50),
        3: ("ลาเต้", 50),
        4: ("แฟลตไวท์", 40)
    }
    
    # เมนูล็อปปิ้ง
    toppings = {
        1: ("วิปครีม", 15),
        2: ("ไข่มุก", 10)
    }
    
    # แสดงเมนูเครื่องดื่ม
    print("\n--- เมนูเครื่องดื่ม ---")
    for key, val in drinks.items():
        print(f"{key}. {val[0]} - {val[1]} บาท")
        
    choice_drink = int(input("เลือกเครื่องดื่ม (1-4): "))
    drink_name, drink_price = drinks.get(choice_drink, ("ไม่ถูกต้อง", 0))
    
    # แสดงเมนูล็อปปิ้ง
    print("\n--- เมนูล็อปปิ้ง ---")
    print("0. ไม่รับท็อปปิ้ง")
    for key, val in toppings.items():
        print(f"{key}. {val[0]} - {val[1]} บาท")
        
    choice_topping = int(input("เลือกท็อปปิ้ง (0-2): "))
    if choice_topping in toppings:
        topping_name, topping_price = toppings[choice_topping]
    else:
        topping_name, topping_price = ("ไม่รับท็อปปิ้ง", 0)

    # คำนวณราคารวมเบื้องต้น
    subtotal = drink_price + topping_price
    discount = 0
    
    # เช็คเงื่อนไขส่วนลด (ถ้าซื้อเกิน 100 บาท แถมฟรีท็อปปิ้ง 1 อย่าง)
    if subtotal > 100 and topping_price > 0:
        discount = topping_price  # ส่วนลดเท่ากับราคาท็อปปิ้ง
        print("\n🎉 โปรโมชั่น: ยอดซื้อเกิน 100 บาท ฟรีท็อปปิ้ง 1 อย่าง!")
    elif subtotal > 100 and topping_price == 0:
        print("\n💡 ยอดซื้อเกิน 100 บาท แต่คุณไม่ได้เลือกท็อปปิ้ง จึงไม่ได้ใช้สิทธิ์แถมฟรี")

    # ยอดรวมสุทธิ
    total_price = subtotal - discount

    # แสดงใบเสร็จ/สรุปรายการ
    print("\n==============================")
    print("        สรุปรายการสั่งซื้อ       ")
    print("==============================")
    print(f"เครื่องดื่ม: {drink_name} ({drink_price} บาท)")
    print(f"ท็อปปิ้ง  : {topping_name} ({topping_price} บาท)")
    print(f"ราคารวม  : {subtotal} บาท")
    print(f"ส่วนลด   : -{discount} บาท")
    print(f"ยอดที่ต้องชำระจริง: {total_price} บาท")
    print("==============================")

    # รับเงินจากลูกค้าและคิดเงินทอน
    while True:
        cash_received = float(input("\nรับเงินจากลูกค้า (บาท): "))
        
        if cash_received >= total_price:
            change = cash_received - total_price
            print(f"เงินทอน: {change:.2f} บาท")
            print("ขอบคุณที่อุดหนุนครับ/ค่ะ! 🙏")
            break
        else:
            print(f"❌ จำนวนเงินไม่พอ! ขาดอีก {total_price - cash_received:.2f} บาท กรุณารับเงินเพิ่ม")

if __name__ == "__main__":
    main()
