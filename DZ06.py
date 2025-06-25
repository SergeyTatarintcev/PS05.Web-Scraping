import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()  # или Chrome()
wait = WebDriverWait(driver, 15)

driver.get('https://www.divan.ru/category/divany-i-kresla')

# Ждём появления хотя бы одной карточки
wait.until(EC.presence_of_element_located((
    By.CSS_SELECTOR, 'div[data-testid="product-card"]'
)))

cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card"]')
parsed = []

for card in cards:
    try:
        # Название: любой элемент с itemprop="name"
        title_el = card.find_element(By.CSS_SELECTOR, '[itemprop="name"]')
        title = title_el.text.strip()

        # Ссылка: первый <a> с href, начинающимся на "/product"
        a = card.find_element(By.CSS_SELECTOR, 'a[href^="/product"]')
        href = a.get_attribute('href')
        link = href if href.startswith('http') else 'https://www.divan.ru' + href

        # Цена: любой элемент с data-testid="price"
        price_el = card.find_element(By.CSS_SELECTOR, '[data-testid="price"]')
        price = price_el.text.strip()

    except Exception as e:
        # если что-то не нашли — пропускаем карточку
        print(f'— не смог спарсить одну карточку: {e}')
        continue

    parsed.append([title, price, link])

driver.quit()

# Сохраняем в CSV с BOM для Excel
with open('divany_i_kresla.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed)

print(f'Готово, бро! Спарсено {len(parsed)} товаров, файл divany_i_kresla.csv.')
