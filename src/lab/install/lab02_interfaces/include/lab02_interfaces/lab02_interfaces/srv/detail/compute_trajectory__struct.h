// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from lab02_interfaces:srv/ComputeTrajectory.idl
// generated code does not contain a copyright notice

#ifndef LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__STRUCT_H_
#define LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ComputeTrajectory in the package lab02_interfaces.
typedef struct lab02_interfaces__srv__ComputeTrajectory_Request
{
  double x;
  double y;
} lab02_interfaces__srv__ComputeTrajectory_Request;

// Struct for a sequence of lab02_interfaces__srv__ComputeTrajectory_Request.
typedef struct lab02_interfaces__srv__ComputeTrajectory_Request__Sequence
{
  lab02_interfaces__srv__ComputeTrajectory_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lab02_interfaces__srv__ComputeTrajectory_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ComputeTrajectory in the package lab02_interfaces.
typedef struct lab02_interfaces__srv__ComputeTrajectory_Response
{
  double distance;
  double direction;
} lab02_interfaces__srv__ComputeTrajectory_Response;

// Struct for a sequence of lab02_interfaces__srv__ComputeTrajectory_Response.
typedef struct lab02_interfaces__srv__ComputeTrajectory_Response__Sequence
{
  lab02_interfaces__srv__ComputeTrajectory_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lab02_interfaces__srv__ComputeTrajectory_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__STRUCT_H_
