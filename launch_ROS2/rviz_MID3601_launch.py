import os
from launch import LaunchDescription
from launch_ros.actions import Node

################### user configure parameters for ros2 start ###################
xfer_format    = 0    # 0: Pointcloud2 (PointXYZRTL), 1: customized pointcloud format
multi_topic    = 1    # 0: All LiDARs share the same topic, 1: One LiDAR per topic
data_src       = 0    # 0: LiDAR, others: Invalid data source
publish_freq   = 10.0 # publish frequency (e.g., 5.0, 10.0, 20.0, 50.0, etc.)
output_type    = 0

# 서로 다른 LVX 파일 경로 지정
lvx_file_path1 = '/home/livox/livox_test1.lvx'
# 각 노드에 대해 다른 cmdline_bd_code 지정
cmdline_bd_code1 = 'livox0000000001'

cur_path        = os.path.split(os.path.realpath(__file__))[0] + '/'
cur_config_path = os.path.join(cur_path, '../config')
user_config_path  = os.path.join(cur_config_path, 'MID360_config.json')
################### user configure parameters for ros2 end #####################

livox_ros2_params = [
    {"xfer_format": xfer_format},
    {"multi_topic": multi_topic},
    {"data_src": data_src},
    {"publish_freq": publish_freq},
    {"output_data_type": output_type},
    {"frame_id": "lidar_1"},
    {"lvx_file_path": lvx_file_path1},
    {"user_config_path": user_config_path},
    {"cmdline_input_bd_code": cmdline_bd_code1}
]

def generate_launch_description():
    livox_driver = Node(
        package='livox_ros_driver2',
        executable='livox_ros_driver2_node',
        namespace='livox_lidar_publisher',  # 네임스페이스 설정 (토픽 구분 용도)
        name='livox_lidar_publisher',
        output='screen',
        parameters=livox_ros2_params
    )
    return LaunchDescription([livox_driver])
