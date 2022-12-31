#SPDX-FileCopyrightText: 2022 Makido1910
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16



    
def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)
        

rclpy.init()
node = Node("listener")
sub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)

if __name__ == '__main__':
   main()
