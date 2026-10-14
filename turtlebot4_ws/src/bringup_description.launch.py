import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('turtlebot4_description')
    urdf_path = os.path.join(pkg_share, 'urdf', 'standard', 'turtlebot4.urdf.xacro') # or processed urdf path

    # Using xacro or pre-compiled urdf string
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': os.popen(f'xacro {urdf_path}').read(),
                'use_sim_time': False
            }]
        )
    ])
