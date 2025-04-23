from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

def check_url_alert(target_url):
    options = Options()
    options.headless = True 
    driver = webdriver.Chrome(options=options)

    try:
        print(f"[🔍] Visiting {target_url}")
        driver.get(target_url)
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            print("[✅] Alert triggered! XSS executed.")
            print("Alert text:", alert.text)
            alert.accept()
        except:
            print("[❌] No alert detected. Payload may not have executed.")
    except UnexpectedAlertPresentException:
        print("[⚠️] Alert appeared automatically — XSS likely executed.")
    except Exception as e:
        print(f"[⚠️] Error occurred: {e}")
    finally:
        driver.quit()
