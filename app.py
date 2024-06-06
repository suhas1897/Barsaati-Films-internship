from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from bson.objectid import ObjectId
import uuid
from datetime import datetime
import time

app = Flask(__name__)

# Initialize WebDriver and MongoDB client globally
options = Options()
options.add_argument("--proxy-server=http://suhas_7981:Srinu@7981@proxy.proxyMesh.com:31280")
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 30)

client = MongoClient("mongodb://localhost:27017/")
db = client["twitterTrendsDB"]
collection = db["trends"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape_data():
    try:
        # Maximize the window and navigate to the login page
        driver.maximize_window()
        driver.get("https://x.com/")

        #x-button

        # driver.find_element(By.XPATH,"//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']").click()
        #login-button
        driver.find_element(By.XPATH, "//a[@href='/login']" ).click()
        #input username
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))

        # Login to the website
        username = driver.find_element(By.XPATH, "//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")
        username.click()
        username.send_keys("SUHASCHALA26617")

        driver.find_element(By.XPATH, "(//button[@class = 'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l'])[1]").click()


        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))
        password = driver.find_element(By.XPATH, "//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")
        password.click()
        password.send_keys("Srinu@7981")

        driver.find_element(By.XPATH, "//button[@class = 'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']").click()


        # Wait for the page to load after login
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'What’s happening')]")))

        

        # Scroll down and click on "Show More"
        driver.execute_script("window.scrollBy(0,400);")
        showmore = driver.find_element(By.XPATH, "//a[@href='/explore/tabs/for-you']")
        showmore.click()

        # Wait for trending topics to load
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Timeline: Explore']//div[@data-testid='trend']//div[@style = 'text-overflow: unset; color: rgb(231, 233, 234);'] //span[@style ='text-overflow: unset;']")))

        # Get trending topics
        trending_topics = driver.find_elements(By.XPATH, "//div[@aria-label='Timeline: Explore']//div[@data-testid='trend']//div[@style = 'text-overflow: unset; color: rgb(231, 233, 234);'] //span[@style ='text-overflow: unset;']")

        
        # Extract up to 5 trending topics
        trends = [topic.text for topic in trending_topics[:5]]

        # MongoDB data insertion
        unique_id = str(uuid.uuid4())
        end_time = datetime.now()

        document = {
            "_id": unique_id,
            "trend1": trends[0] if len(trends) > 0 else None,
            "trend2": trends[1] if len(trends) > 1 else None,
            "trend3": trends[2] if len(trends) > 2 else None,
            "trend4": trends[3] if len(trends) > 3 else None,
            "trend5": trends[4] if len(trends) > 4 else None,
            "endTime": end_time.isoformat(),
            "ipAddress": "http://suhas_7981:Srinu@7981@proxy.proxyMesh.com:31280"  # Proxy address
        }

        collection.insert_one(document)
        print(f"Data inserted successfully with id: {document['_id']}")
        print(document)

        # Prepare data to return as JSON
        date_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
        response_data = {
            "status": "success",
            "date_time": date_time,
            "trends": trends,
            "ipAddress": document["ipAddress"]
        }

        #x - button
        if driver.find_elements(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']"):
            driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']").click()
        logout_button = driver.find_element(By.XPATH, "//button[@class = 'css-175oi2r r-1awozwy r-sdzlij r-6koalj r-18u37iz r-xyw6el r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
        logout_button.click()
        driver.find_element(By.XPATH, "(//a[@class='css-175oi2r r-18u37iz r-1mmae3n r-3pj75a r-13qz1uu r-o7ynqc r-6416eg r-1ny4l3l r-1loqt21'])[2]").click()
        driver.find_element(By.XPATH,"(//button[@class = 'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-16y2uox r-6gpygo r-1udh08x r-1udbk01 r-3s2u2q r-peo1c r-1ps3wis r-cxgwc0 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l'])[1]" ).click()
        return jsonify(response_data)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
