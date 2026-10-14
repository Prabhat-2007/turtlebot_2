from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. RPLIDAR Driver Node (Lightweight serial bridge)
        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 115200,
                'frame_id': 'laser_link',
                'angle_compensate': True
            }],
            output='screen'
        ),

        # 2. OAK-D Stereo Camera Node (Pointcloud disabled to optimize CPU)
        Node(
            package='depthai_ros_driver',
            executable='camera',
            name='oak_camera',
            parameters=[{
                'camera_model': 'oak-d',
                'enable_pointcloud': False,
                'i_max_usb_speed': 'HIGH'
            }],
            output='screen'
        )
    ])
