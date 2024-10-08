import rclpy
from math import pi
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import Header

class YourNode(Node):
    def __init__(self):
        super().__init__('YourNode')
        self.ackermann_publisher = self.create_publisher(AckermannDriveStamped, '/drive', 10)
        self.scan_subscription = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
        #include below line if you intend to use odometry data in your solution
        #self.odom_subscription = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
        self.get_logger().info('YourNode has been started.')

    def scan_callback(self, msg):
        '''
        The scan_callback function will be called every time that a scan is recieved
        
        to access lidar distance data, use msg.ranges -- ranges is just a list

        there are 1080 scans, so 540 is straight ahead

        the car has a maximum turn angle of 30 degrees

        the simulator expects turns in radians. i've left deg2rad() for that purpose

        assume 22.8 (m/s) is the maximum possible speed of the car, although this is VERY
        fast. Our absolute best algorithms are capped at 8

        you can print to console with self.get_logger().info(f'whatever string or {data}')

        '''

        speed = 'Calculate this!'
        steering_angle = 'Calculate this!'

        self.publish_ackermann_drive(speed, self.deg2rad(steering_angle))


    #this function publishes your speed and steering data to the drive topic
    #you shouldn't have to modify this!
    def publish_ackermann_drive(self, speed, steering_angle):
        ackermann_msg = AckermannDriveStamped()
        ackermann_msg.header = Header()
        ackermann_msg.header.stamp = self.get_clock().now().to_msg()
        ackermann_msg.drive.speed = float(speed)
        ackermann_msg.drive.steering_angle = float(steering_angle)

        self.ackermann_publisher.publish(ackermann_msg)
        self.get_logger().info(f'Published AckermannDriveStamped message: speed={speed}, steering_angle={steering_angle}')


#don't need to mess with this either -- it just starts the node
def main(args=None):
    rclpy.init(args=args)
    node = YourNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()