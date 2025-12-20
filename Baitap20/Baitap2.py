while True : 
    diem = float(input("Nhập vào điểm của bạn : "))
    if 0 <= diem <= 10 :
        print("Điểm của bạn là ",diem)
        break 
    else :
        print("Điểm không hợp lệ . Vui lòng nhập lại ")
        