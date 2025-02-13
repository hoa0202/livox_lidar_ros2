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
lvx_file_path2 = '/home/livox/livox_test2.lvx'
# 각 노드에 대해 다른 cmdline_bd_code 지정
cmdline_bd_code2 = 'livox0000000002'

cur_path        = os.path.split(os.path.realpath(__file__))[0] + '/'
cur_config_path = os.path.join(cur_path, '../config')
user_config_path2 = os.path.join(cur_config_path, 'MID3602_config.json')
################### user configure parameters for ros2 end #####################

livox_ros2_params2 = [
    {"xfer_format": xfer_format},
    {"multi_topic": multi_topic},
    {"data_src": data_src},
    {"publish_freq": publish_freq},
    {"output_data_type": output_type},
    {"frame_id": "lidar_2"},
    {"lvx_file_path": lvx_file_path2},
    {"user_config_path": user_config_path2},
    {"cmdline_input_bd_code": cmdline_bd_code2}
]

def generate_launch_description():
    mid360_right = Node(
        package='livox_ros_driver2',
        executable='livox_ros_driver2_node',
        namespace='mid360_right_node',  # 네임스페이스 설정 (토픽 구분 용도)
        name='mid360_right_node',
        output='screen',
        parameters=livox_ros2_params2
    )
    return LaunchDescription([mid360_right])
