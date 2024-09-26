import time
from plyer import notification
 
 
if __name__=="__main__":
 while True:
        notification.notify(
            title = "TIME FOR A HYDRATION BREAK",
            message=" Please take a moment to have a glass of water" ,
           
            # displaying time
            timeout=2
)
        # waiting time
        time.sleep(60*60)