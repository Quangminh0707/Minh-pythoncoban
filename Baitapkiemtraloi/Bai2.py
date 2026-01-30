def doc_file(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Lỗi: File '{ten_file}' không tồn tại.")

doc_file("data.txt")