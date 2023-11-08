// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lab02_interfaces:srv/ComputeTrajectory.idl
// generated code does not contain a copyright notice

#ifndef LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__BUILDER_HPP_
#define LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lab02_interfaces/srv/detail/compute_trajectory__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lab02_interfaces
{

namespace srv
{

namespace builder
{

class Init_ComputeTrajectory_Request_y
{
public:
  explicit Init_ComputeTrajectory_Request_y(::lab02_interfaces::srv::ComputeTrajectory_Request & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::srv::ComputeTrajectory_Request y(::lab02_interfaces::srv::ComputeTrajectory_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::srv::ComputeTrajectory_Request msg_;
};

class Init_ComputeTrajectory_Request_x
{
public:
  Init_ComputeTrajectory_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ComputeTrajectory_Request_y x(::lab02_interfaces::srv::ComputeTrajectory_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_ComputeTrajectory_Request_y(msg_);
  }

private:
  ::lab02_interfaces::srv::ComputeTrajectory_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::srv::ComputeTrajectory_Request>()
{
  return lab02_interfaces::srv::builder::Init_ComputeTrajectory_Request_x();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace srv
{

namespace builder
{

class Init_ComputeTrajectory_Response_direction
{
public:
  explicit Init_ComputeTrajectory_Response_direction(::lab02_interfaces::srv::ComputeTrajectory_Response & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::srv::ComputeTrajectory_Response direction(::lab02_interfaces::srv::ComputeTrajectory_Response::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::srv::ComputeTrajectory_Response msg_;
};

class Init_ComputeTrajectory_Response_distance
{
public:
  Init_ComputeTrajectory_Response_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ComputeTrajectory_Response_direction distance(::lab02_interfaces::srv::ComputeTrajectory_Response::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_ComputeTrajectory_Response_direction(msg_);
  }

private:
  ::lab02_interfaces::srv::ComputeTrajectory_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::srv::ComputeTrajectory_Response>()
{
  return lab02_interfaces::srv::builder::Init_ComputeTrajectory_Response_distance();
}

}  // namespace lab02_interfaces

#endif  // LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__BUILDER_HPP_
