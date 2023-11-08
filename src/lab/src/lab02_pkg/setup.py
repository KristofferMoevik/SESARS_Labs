from setuptools import find_packages, setup

package_name = 'lab02_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='kristoffersmovik@live.no',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle1_compute_trajectory = lab02_pkg.turtle1_compute_trajectory:main',
            'turtle1_move_forward = lab02_pkg.turtle1_move_forward:main',
        ],
    },
)
