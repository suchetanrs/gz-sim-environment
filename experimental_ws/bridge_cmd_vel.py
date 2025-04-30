#!/usr/bin/env python3
"""
A simple ROS2 node that subscribes to /cmd_vel_nav (TwistStamped)
and republishes its Twist to /cmd_vel.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped, Twist

class CmdVelBridge(Node):
    """Node that bridges TwistStamped -> Twist topics."""

    def __init__(self):
        super().__init__('cmd_vel_bridge')
        # Subscriber to cmd_vel_nav (TwistStamped)
        self.subscription = self.create_subscription(
            TwistStamped,
            'cmd_vel_nav',
            self.cmd_vel_nav_callback,
            10
        )
        # Publisher to cmd_vel (Twist)
        self.publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )

        self.get_logger().info(
            'CmdVelBridge initialized: subscribing to "cmd_vel_nav", publishing to "cmd_vel"'
        )

    def cmd_vel_nav_callback(self, msg: TwistStamped):
        # Extract the Twist from TwistStamped and republish
        twist_msg = Twist()
        twist_msg.linear = msg.twist.linear
        twist_msg.angular = msg.twist.angular
        self.publisher.publish(twist_msg)
        self.get_logger().debug(
            f'Republished cmd_vel: linear={twist_msg.linear}, angular={twist_msg.angular}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt: shutting down')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
