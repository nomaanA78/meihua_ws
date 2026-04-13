import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('meihua_description')
    
    # 1. Include the Robot State Publisher (your URDF)
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(pkg_path,'launch','rsp.launch.py')]),
        launch_arguments={'use_sim_time': 'false'}.items()
    )

    # 2. Run the Sliders (GUI)
    jsp_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # 3. Run RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(pkg_path, 'config', 'view_bot.rviz')] # If you have a config file
    )

    return LaunchDescription([rsp, jsp_gui, rviz])