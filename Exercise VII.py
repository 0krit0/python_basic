# สร้างรายการเพื่อเก็บเลขคู่และเลขคี่
even_numbers = []
odd_numbers = []

# วนลูปเพื่อตรวจสอบเลขคู่และเลขคี่ในช่วงตัวเลข 1-20
for number in range(1, 21):
    if number % 2 == 0:
        even_numbers.append(number)  # เพิ่มเลขคู่เข้าไปในรายการ even_numbers
    else:
        odd_numbers.append(number)   # เพิ่มเลขคี่เข้าไปในรายการ odd_numbers

# แสดงผลลัพธ์
print("เลขคู่:", even_numbers)
print("เลขคี่:", odd_numbers)

#นายกฤษณพงศ์ ปรีชามาตร์ เลขที่ 1 6749010001