#bài tập 1: Tính năng "Chia tiền hóa đơn"(Bill Splitter) trên app ngân hàng

#1. Nhập thông tin đầu vào (X,Y,N)
total_bill = float(input("Nhập tổng số tiền hóa đơn X (VND): "))
tip_percent = float(input("Nhập % tiền tip Y (ví dụ; 10 cho 10%):"))
num_people = int(input("Nhập số người chia N: "))

#2. xử lư tính toán
# Tính số tiền tip dựa trên tỉ lệ %
tip_amount = total_bill * (tip_percent / 100)

# Tính tổng số tiền phải thanh toán (Hóa đơn gốc + Tiền tip)
total_amount = total_bill + tip_amount

# Tính số tiền mỗi người phải trả
amount_per_person = total_amount / num_people

# Làm tronf đến số nguyên (0 chữ số thập phân) theo yêu cầu
amount_per_person_rounded = round(amount_per_person)

#3. Xuất kết quả
print("\n--- KẾT QUẢ CCHIA TIỀN HÓA ĐƠN ---")
print(f"Tổng hóa đơn gốc              : {round(total_bill):,.0f} VND")
print(f"Tiền tip ({tip_percent}%)                  : {round(tip_amount):,.0f} VND")
print(f"Tổng thanh toán (bao gồm tip)  : {round(total_amount):,.0f} VND")
print(f"Số tiền mỗi người phải trả     : {amount_per_person_rounded:,.0f} VND")

