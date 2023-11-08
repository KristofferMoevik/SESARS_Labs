// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lab02_interfaces:action/MoveDistance.idl
// generated code does not contain a copyright notice

#ifndef LAB02_INTERFACES__ACTION__DETAIL__MOVE_DISTANCE__BUILDER_HPP_
#define LAB02_INTERFACES__ACTION__DETAIL__MOVE_DISTANCE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lab02_interfaces/action/detail/move_distance__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_Goal_distance
{
public:
  Init_MoveDistance_Goal_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lab02_interfaces::action::MoveDistance_Goal distance(::lab02_interfaces::action::MoveDistance_Goal::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_Goal>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_Goal_distance();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_Result_traveled_distance
{
public:
  explicit Init_MoveDistance_Result_traveled_distance(::lab02_interfaces::action::MoveDistance_Result & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::action::MoveDistance_Result traveled_distance(::lab02_interfaces::action::MoveDistance_Result::_traveled_distance_type arg)
  {
    msg_.traveled_distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_Result msg_;
};

class Init_MoveDistance_Result_elapsed_time_s
{
public:
  Init_MoveDistance_Result_elapsed_time_s()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveDistance_Result_traveled_distance elapsed_time_s(::lab02_interfaces::action::MoveDistance_Result::_elapsed_time_s_type arg)
  {
    msg_.elapsed_time_s = std::move(arg);
    return Init_MoveDistance_Result_traveled_distance(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_Result>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_Result_elapsed_time_s();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_Feedback_remaining_distance
{
public:
  Init_MoveDistance_Feedback_remaining_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lab02_interfaces::action::MoveDistance_Feedback remaining_distance(::lab02_interfaces::action::MoveDistance_Feedback::_remaining_distance_type arg)
  {
    msg_.remaining_distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_Feedback>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_Feedback_remaining_distance();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_SendGoal_Request_goal
{
public:
  explicit Init_MoveDistance_SendGoal_Request_goal(::lab02_interfaces::action::MoveDistance_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::action::MoveDistance_SendGoal_Request goal(::lab02_interfaces::action::MoveDistance_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_SendGoal_Request msg_;
};

class Init_MoveDistance_SendGoal_Request_goal_id
{
public:
  Init_MoveDistance_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveDistance_SendGoal_Request_goal goal_id(::lab02_interfaces::action::MoveDistance_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_MoveDistance_SendGoal_Request_goal(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_SendGoal_Request>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_SendGoal_Request_goal_id();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_SendGoal_Response_stamp
{
public:
  explicit Init_MoveDistance_SendGoal_Response_stamp(::lab02_interfaces::action::MoveDistance_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::action::MoveDistance_SendGoal_Response stamp(::lab02_interfaces::action::MoveDistance_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_SendGoal_Response msg_;
};

class Init_MoveDistance_SendGoal_Response_accepted
{
public:
  Init_MoveDistance_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveDistance_SendGoal_Response_stamp accepted(::lab02_interfaces::action::MoveDistance_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_MoveDistance_SendGoal_Response_stamp(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_SendGoal_Response>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_SendGoal_Response_accepted();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_GetResult_Request_goal_id
{
public:
  Init_MoveDistance_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lab02_interfaces::action::MoveDistance_GetResult_Request goal_id(::lab02_interfaces::action::MoveDistance_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_GetResult_Request>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_GetResult_Request_goal_id();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_GetResult_Response_result
{
public:
  explicit Init_MoveDistance_GetResult_Response_result(::lab02_interfaces::action::MoveDistance_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::action::MoveDistance_GetResult_Response result(::lab02_interfaces::action::MoveDistance_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_GetResult_Response msg_;
};

class Init_MoveDistance_GetResult_Response_status
{
public:
  Init_MoveDistance_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveDistance_GetResult_Response_result status(::lab02_interfaces::action::MoveDistance_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_MoveDistance_GetResult_Response_result(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_GetResult_Response>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_GetResult_Response_status();
}

}  // namespace lab02_interfaces


namespace lab02_interfaces
{

namespace action
{

namespace builder
{

class Init_MoveDistance_FeedbackMessage_feedback
{
public:
  explicit Init_MoveDistance_FeedbackMessage_feedback(::lab02_interfaces::action::MoveDistance_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::lab02_interfaces::action::MoveDistance_FeedbackMessage feedback(::lab02_interfaces::action::MoveDistance_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_FeedbackMessage msg_;
};

class Init_MoveDistance_FeedbackMessage_goal_id
{
public:
  Init_MoveDistance_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveDistance_FeedbackMessage_feedback goal_id(::lab02_interfaces::action::MoveDistance_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_MoveDistance_FeedbackMessage_feedback(msg_);
  }

private:
  ::lab02_interfaces::action::MoveDistance_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab02_interfaces::action::MoveDistance_FeedbackMessage>()
{
  return lab02_interfaces::action::builder::Init_MoveDistance_FeedbackMessage_goal_id();
}

}  // namespace lab02_interfaces

#endif  // LAB02_INTERFACES__ACTION__DETAIL__MOVE_DISTANCE__BUILDER_HPP_
