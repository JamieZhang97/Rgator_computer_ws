from setuptools import setup

package_name = 'dbw'

setup(
    name=package_name,
    version='1.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jiaming Zhang',
    maintainer_email='jz73@illinois.edu',
    description='The ROS2 workspace of the supervisor computer of R-Gator.',
    license='GNU GENERAL PUBLIC LICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dbw_read = dbw.dbw_read:main',
            'dbw_read = dbw.dbw_read_vel:main'
        ],
    },
)
