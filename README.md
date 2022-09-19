# Aliexpress Splash It
A small project on multi-threaded automation of cutting the price of goods using the `Python` language and `SELENIUM IDE` and the `Harakirimail` temporary mail service.

## Features
* Creates many accounts using Harakirimail
* Allows you to bring down the price on the main account

## How to install
1. Clone this repository on your computer
`https://github.com/Genya45/Aliexpress_Splash_It.git`
2. Install all the requirements `pip install -r requirements.txt`
3. For the program to work, the folder must also contain the current version of the chromedriver.exe file (it must match the current version of the Chrome browser), since the parser works on SELENIUM. You can download from the link `https://chromedriver.chromium.org/downloads`
4. On the main account, get a link from Splash It like `https://a.aliexpress.com/_uQVeli` and add it to the `LINK_HELP_FRIEND` variable
5. Replace the `MAIL_NAME` and `PASSWORD_LABEL` fields with your desired values. Optionally change the number of threads in the `number_of_threads` variable (default `2`)
6. Run the program
`python main.py`


## Also
Also, the `accounts.txt` file will be created in the folder with the program, in which the logins and passwords of the created accounts will be recorded.

By default, program works in "headless mode". Therefore, if you need process visibility, you must comment out the line `options.add_argument("--headless")`

## Result

![alt text](https://github.com/Genya45/Aliexpress_Splash_It/blob/main/Screenshot.png)
