#include <ros/ros.h>
#include<std_msgs/String.h>
void sub_callback(std_msgs::String msg)
{
    ROS_INFO(msg.data.c_str());
}

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"sub_c_node");
    
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("cpp",10,sub_callback);

    ros::Rate loop_rate(10);

    while(ros::ok())
    {
        ros::spinOnce();
    }
    return 0;
}
