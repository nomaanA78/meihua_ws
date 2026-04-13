import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    # 1. Specify the package name and find its install path
    package_name = 'meihua_description'
    pkg_share = get_package_share_directory(package_name)

    # 2. Correctly locate the URDF file inside the 'urdf' folder
    # This prevents the "meihua_bot.urdf.urdf" error by using the exact path
    urdf_file_path = os.path.join(pkg_share, 'urdf', 'meihua_bot.urdf') 
    
    # 3. Read the URDF content
    with open(urdf_file_path, 'r') as infp:
        robot_desc = infp.read()

    # 4. Robot State Publisher Node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 5. Include Gazebo Launch (Starts the simulator)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
    )

    # 6. Spawn Entity Node (Puts the robot into the simulator)
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'meihua_sandwich_bot', '-z', '0.2'],
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        gazebo,
        spawn_entity
    ])