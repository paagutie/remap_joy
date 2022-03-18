import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    
    launch.actions.DeclareLaunchArgument('topic_name', default_value='/joy_bluerov'),
    launch.actions.DeclareLaunchArgument('other'),
    joystick0 = launch_ros.actions.Node(
        package='joy', 
        executable='joy_node', 
        name='joy0',
        output='screen',
        remappings = [('/joy', launch.substitutions.LaunchConfiguration('topic_name'))]
       
     )
     
    return launch.LaunchDescription([
        joystick0,
    ])


