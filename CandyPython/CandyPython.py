import rospy
import time
from std_msgs.msg import Int16
from kobuki_msgs.msg import Led

rospy.init_node('IntegerPub')
rospy.init_node('MessageReader')
servoPub = rospy.Publisher('servo', Int16,queue_size=1)
infraRedSub = rospy.Subscriber('rangedata', Int16,IrSensorData)
led = rospy.Publisher('/mobile_base/commands/led1',Led,queue_size=1)
rate = rospy.Rate(1)
count = 0
dispenserOpen = 180
dispenserClosed = 0

def IrSensorData(SomeMsg):
	print SomeMsg.data
	Lon = 2
	Loff = 0
	if Somemsg.data != 0
	    led.publish(Lon)
	else:
	    led.publish(Loff)
	   
def servo():
    global count
    count = count + 1
    servoPub.publish(dispensorOpen)
    time.sleep(5)
	servoPub.publish(dispensorClosed)
	
while count != 1:
    servo()
    time.sleep(300)
            
rospy.spin()

