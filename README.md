# Gym Booking Bot

<img src="https://user-images.githubusercontent.com/36112125/113499920-e8431a00-94e7-11eb-977a-0f0810a3a0e8.png" alt="Your image title" width="120"/>

:muscle: I wrote a Python script that automates my gym time bookings at midnight everyday.

Due to the COVID-19 pandemic, gyms in Ontario have implemented an online sign-up system that requires members to book for a specific workout time.  
The gym I go to allow members to start booking their gym times at midnight everyday, which is an inconvenient time for me.  
So, I decided to create a bot that does it for me.

**Tools/Technologies**:  
[Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)  
[Amazon EC2](https://aws.amazon.com/ec2/)

:arrow_right:	I web scraped my gym's website by inspecting its **HTML** elements.  
:arrow_right:	I ran **Selenium** tests on Chrome using **ChromeDriver**.  
:arrow_right:	I set up an **AWS EC2** instance that runs the script on the cloud.  
:arrow_right:	I scheduled a **cron job** that automatically runs the script at a specified time in my **EC2** instance.
