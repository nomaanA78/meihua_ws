from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'meihua_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # 1. Install Launch Files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        
        # 2. Install URDF Files
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.[ux][ra][dc][fr]*'))),

        # 3. Install World Files (ADD THIS LINE)
        # This tells ROS 2 to look in your 'worlds' folder and grab any .world files
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.world'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nomaan78',
    maintainer_email='nomaan78@todo.todo',
    description='12-wheel sandwich robot description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)