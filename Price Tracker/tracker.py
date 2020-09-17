from selenium import webdriver
import smtplib
import time

option = webdriver.chrome.options.Options()
option.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=option)

def check_amazon_price(url):
    driver.get(url)

    data = driver.find_element_by_xpath("//*[@id='priceblock_ourprice']")
    price = int(''.join(data.text[2:-3].split(',')))
    return price

def check_flipkart_price(url):
    driver.get(url)

    data = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div/div[1]")
    price = int(''.join(data.text[1:].split(',')))
    return price

def send_mail(url, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    sender_email = input('Enter sender email:')
    sender_password = input('Enter gmail app password:')

    receiver_email = input('Enter receiver email:')

    server.login(sender_email, sender_password)

    title = 'Hey the product is within your price range!!'
    body = 'Visit the link below to check updated price \n' + url
    info = 'The current price is:' + price

    server.sendmail(sender_email, receiver_email, title + '\n' + info + '\n' +body)

    print('MAIL SENT!!')
    server.close()

if __name__ == "__main__":
    a_link = input('Enter Amazon link:')
    f_link = input('Enter Flipkart link:')

    while True:
        amazon_price = check_amazon_price(a_link)
        flipkart_price = check_flipkart_price(f_link)
        range = input('Enter your maximum price:')

        print(amazon_price, flipkart_price)

        if amazon_price <= range and flipkart_price <= range:
            send_mail(a_link, amazon_price)
            send_mail(f_link, flipkart_price)
        elif amazon_price <= range:
            send_mail(a_link, amazon_price)
        elif flipkart_price <= range:
            send_mail(f_link, flipkart_price)
        else:
            print('Still out of your price range!!')

        time.sleep(21600)