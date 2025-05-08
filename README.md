# Web Scraping với Selenium: Alonhadat
## Yêu cầu
Trước khi chạy project, bạn cần cài đặt một số công cụ và thư viện sau:
1. **Python**: Project yêu cầu Python phiên bản 3.x.
2. **Chrome Driver**: Selenium yêu cầu trình điều khiển cho trình duyệt Chrome.
3. **Thư viện Python**: \selenium\, \pandas\, \schedule\.
   Cài đặt bằng lệnh: \pip install selenium pandas schedule\.
4. **Trình duyệt Google Chrome**: Cần cài đặt trình duyệt Google Chrome.
## Cách sử dụng
### Bước 1: Tải project về máy
Clone project về máy tính của bạn:
Giải nén **ChromeDriver** vào một thư mục và lấy đường dẫn tới file **chromedriver.exe**.
### Bước 3: Cấu hình đường dẫn cho file Excel
Thay đổi đường dẫn trong hàm \df.to_excel()\ trong file script để chỉ đến thư mục nơi bạn muốn lưu file Excel đầu ra.
### Bước 4: Chạy script
Chạy script bằng lệnh: \python selenium_script.py\.
## Tính năng
- **Thu thập dữ liệu** từ nhiều trang kết quả của website **alonhadat.com.vn**.
- **Lưu dữ liệu** vào file Excel.
- **Tự động chạy hàng ngày** vào lúc 06:00 sáng.
