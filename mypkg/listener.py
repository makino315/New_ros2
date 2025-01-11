# SPDX-FileCopyrightText: 2025 Kazuki Makino
# SPDX-License-Identifier:BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


rclpy.init()
node=Node("listener")


def cb(msg):
    global node
    node.get_logger().info("%s" % msg.data)


def main():
    pub=node.create_subscription(String,"weather",cb,10)
    rclpy.spin(node)

