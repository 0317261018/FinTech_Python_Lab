# Bài tập 2: Tính Tỷ suất sinh lời trên vốn đầu tư (ROI - Return on Investment)
# 1.Nhập thông tin từ người dùng
initial_investment = float(input("Nhập tổng vốn đầu tư ban đầu (VND): "))
final_value = float(input("Nhập tổng giá trị thu về khi bán (VND): "))

# 2. Xử lý tính toán
# Lợi nhuận ròng= Tổng giá trị bán ra - Tổng vốn ban đầu
net_profit = final_value - initial_investment

# Tỷ lệ ROI (%) = (Lợi nhuận ròng / Tổng vốn ban đầu) * 100
roi_percent = (net_profit / initial_investment) * 100

# 3. Xuất kết quả
print("\n--- BÁO CÁO HIỆU QUẢ ĐẦU TƯ (ROI) ---")
print(f"Tổng vốn ban đầu     :{initial_investment:,.0f} VND")
print(f"Tổng giá trị bán ra  : {final_value:,.0f} VND")
print(f"Lợi nhuận ròng (Profit): {net_profit:,.0f} VND")
print(f"Tỷ suất sinh lời (ROI) : {roi_percent:.2f}%")
