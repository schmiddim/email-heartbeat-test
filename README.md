# Email Hearbeat Test

Test your SMTP Setup. 


# Configuration

Copy [.env.dist](.env.dist) to .env and modify the Variables

## Commands
1. check if there is mail with a defined topic that is not older than *TRESHHOLD_SECONDS*
    
    *bash*
    ```
    source .env && python3 check_inbox.py 
    ```
    *docker*
    ```
    docker run  --env-file .env  email-heartbeat-test python3 check_inbox.py
    ```
2. send mail a mail - use this with a cronjob

    *bash*
    ```
    source .env && python3 send_mail.py
    ```
    *docker*
    ```
    docker run  --env-file .env email-heartbeat-test python3 send_mail.py
    
    ```
You're in trouble if the return Code != 0.

## Installation
### Local
you just need python
### Docker

#### build
```
docker build . -t email-heartbeat-test
```
#### pull
```
docker pull itschmitt/email-heartbeat-test
```
