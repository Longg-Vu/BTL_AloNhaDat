from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import schedule

def initialize_driver():
   
    driver = webdriver.Chrome()
    return driver

def navigate_to_search_page(driver):
    #1. Vào website đã chọn
    driver.get('https://alonhadat.com.vn/')
    
    #2. Click chọn bất kì Tỉnh/TP(Hà Nội, Đà Nẵng, Hồ Chí Minh, …). Chọn bất kì loại nhà đất(Căn hộ chung cư, nhà, đất, …).
    selecter = '#ctl00_content_pc_content > div.search-news-box > div.search-box > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option:nth-child(4)'
    element = driver.find_element(By.CSS_SELECTOR, selecter)
    element.click()
    time.sleep(2)
    
    # 3. Bấm tìm kiếm
    class_search = 'btnsearch'
    element = driver.find_element(By.CLASS_NAME, class_search)
    element.click()
# 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá) hiển thị ở bài viết.
def scrape_page_data(driver):
    
    data = {
        'titles': [],
        'summaries': [],
        'characteristics': [],
        'sizes': [],
        'prices': [],
        'addresses': []
    }
    
    # Scrape each type of data
    data['titles'] = [el.text for el in driver.find_elements(By.CLASS_NAME, 'ct_title')]
    data['summaries'] = [el.text for el in driver.find_elements(By.CLASS_NAME, 'ct_brief')]
    data['characteristics'] = [el.text for el in driver.find_elements(By.CLASS_NAME, 'characteristics')]
    data['sizes'] = [el.text for el in driver.find_elements(By.CLASS_NAME, 'ct_dt')]
    data['prices'] = [el.text for el in driver.find_elements(By.CLASS_NAME, 'ct_price')]
    data['addresses'] = [el.text for el in driver.find_elements(By.CLASS_NAME, 'ct_dis')]
    
    return data
# 5. Lấy tất cả dữ liệu của các trang.

def scrape_all_pages(driver):
    
    all_data = {
        'titles': [],
        'summaries': [],
        'characteristics': [],
        'sizes': [],
        'prices': [],
        'addresses': []
    }
    
    page = 1
    while True:
        driver.get(f'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang/trang--{page}.html')
        time.sleep(2)
        
        page_data = scrape_page_data(driver)
        if not page_data['titles']:
            break 
        for key in all_data:
            all_data[key].extend(page_data[key])
            
        page += 1
    
    return all_data

def normalize_data_lengths(data):
    
    max_length = max(len(lst) for lst in data.values())
    
    for key in data:
        while len(data[key]) < max_length:
            data[key].append('')
    
    return data

def save_to_excel(data, file_path):
   
    df = pd.DataFrame({
        'Title': data['titles'], 
        'Summary': data['summaries'], 
        'Characteristics': data['characteristics'], 
        'Size': data['sizes'], 
        'Price': data['prices'], 
        'Address': data['addresses']
    })
    
    df.to_excel(file_path, index=False)

def job():

    try:
        
        driver = initialize_driver()
        
        navigate_to_search_page(driver)
        
        scraped_data = scrape_all_pages(driver)
        
        normalized_data = normalize_data_lengths(scraped_data)
        
        # 6. Lưu dữ liệu đã lấy được vào file excel hoặc csv.
        save_to_excel(normalized_data, r"C:\Users\admin\Desktop\RPA\Chapter_2\Day7\alonhadat.xlsx")
        
        print("Xuất dữ liệu thành công!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        
        if 'driver' in locals():
            driver.quit()

# 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
schedule.every().day.at("06:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(60)