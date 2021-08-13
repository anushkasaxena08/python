import time
from plyer import notification


if __name__=="__main__":

		notification.notify(
			title = "wake up",
			message=" wake up babe!!!!!" ,
		
			# displaying time
			timeout=2
)
		# waiting time
		time.sleep(7)
