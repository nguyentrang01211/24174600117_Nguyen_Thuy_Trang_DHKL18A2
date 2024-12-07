def tinh_dien_tich_tam_giac(x1, y1, x2, y2, x3, y3):
    # Công thức tính diện tích
    S = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return S

# Nhập tọa độ 3 đỉnh từ người dùng
print("Nhập tọa độ 3 đỉnh của tam giác:")
x1, y1 = map(float, input("Nhập tọa độ đỉnh A (x1 y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ đỉnh B (x2 y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ đỉnh C (x3 y3): ").split())

# Tính diện tích
dien_tich = tinh_dien_tich_tam_giac(x1, y1, x2, y2, x3, y3)
print("Diện tích tam giác là: {dien_tich}")



# input("Nhập lệnh: ")

# Kiểm tra lệnh
if () == "in ra màn hình":
    print("Tên của bạn là: Nguyễn thùy trang")  
else:
    print("Lệnh không hợp lệ.")
