import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    desc_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('tz_turtlebot4_description'), 'launch', 'description.launch.py')
        ])
    )

    sensors_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('tz_turtlebot4_control'), 'launch', 'control_and_sensors.launch.py')
        ])
    )

    return LaunchDescription([
        desc_launch,
        sensors_launch
    ])
