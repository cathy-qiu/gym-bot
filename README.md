# Gym Booking Bot

<img src="https://user-images.githubusercontent.com/36112125/113499920-e8431a00-94e7-11eb-977a-0f0810a3a0e8.png" alt="Your image title" width="120"/>

:muscle: I wrote a Python script that automates my gym time bookings at midnight everyday.

Due to the COVID-19 pandemic, gyms in Ontario have implemented an online sign-up system that requires members to book for a specific workout time.  
The gym I go to allow members to start booking their gym times at midnight everyday, which is an inconvenient time for me.  
So, I decided to create a bot that does it for me.

##Tools/Technologies:##  
[Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)  
[Amazon EC2](https://aws.amazon.com/ec2/)

##How I built it:##  
:arrow_right:	I web scraped my gym's website by inspecting its **HTML** elements.  
:arrow_right:	I used **Selenium** to automate the booking process, more specifically, 
I used [**ChromeDriver**](https://chromedriver.chromium.org/) which is a standalone server that is used by **Selenium WebDriver** to control tests on Chrome.  
:arrow_right:	I set up an **AWS EC2** instance that runs the script on the cloud.  
:arrow_right:	I installed [**Putty**](https://www.putty.org/) to allow me to connect to the instance.
:arrow_right:	I scheduled a **cron job** that automatically runs the script at a specified time in my **EC2** instance.

##To use:##  
:arrow_right:	Clone this repo and set up your local copy of the repository.  
:arrow_right:	Download [**ChromeDriver**](https://chromedriver.chromium.org/) so you can run the automated script on Chrome.  
:arrow_right:	If you do not wish to run the script on the cloud, you can set up a task scheduler (Windows only) and it will run the script only if your machine is turned on

####Go get your booking slot!####
