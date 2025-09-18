#include <ros/ros.h>
#include<std_msgs/String.h>
int main(int argc, char *argv[])
{
    ros::init(argc,argv,"pub_c_node");
    printf("c++实现消息的发布与接收\n");

    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("cpp",10);

    ros::Rate loop_rate(10);

    while(ros::ok())
    {
        printf("c开始发布\n");
        std_msgs::String msg;
        msg.data = "2023112108";
        pub.publish(msg);
        loop_rate.sleep();
    }
    return 0;
}
