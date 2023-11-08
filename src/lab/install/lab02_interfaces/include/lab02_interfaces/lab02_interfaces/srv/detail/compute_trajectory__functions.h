// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from lab02_interfaces:srv/ComputeTrajectory.idl
// generated code does not contain a copyright notice

#ifndef LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__FUNCTIONS_H_
#define LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "lab02_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "lab02_interfaces/srv/detail/compute_trajectory__struct.h"

/// Initialize srv/ComputeTrajectory message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * lab02_interfaces__srv__ComputeTrajectory_Request
 * )) before or use
 * lab02_interfaces__srv__ComputeTrajectory_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Request__init(lab02_interfaces__srv__ComputeTrajectory_Request * msg);

/// Finalize srv/ComputeTrajectory message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Request__fini(lab02_interfaces__srv__ComputeTrajectory_Request * msg);

/// Create srv/ComputeTrajectory message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * lab02_interfaces__srv__ComputeTrajectory_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
lab02_interfaces__srv__ComputeTrajectory_Request *
lab02_interfaces__srv__ComputeTrajectory_Request__create();

/// Destroy srv/ComputeTrajectory message.
/**
 * It calls
 * lab02_interfaces__srv__ComputeTrajectory_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Request__destroy(lab02_interfaces__srv__ComputeTrajectory_Request * msg);

/// Check for srv/ComputeTrajectory message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Request__are_equal(const lab02_interfaces__srv__ComputeTrajectory_Request * lhs, const lab02_interfaces__srv__ComputeTrajectory_Request * rhs);

/// Copy a srv/ComputeTrajectory message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Request__copy(
  const lab02_interfaces__srv__ComputeTrajectory_Request * input,
  lab02_interfaces__srv__ComputeTrajectory_Request * output);

/// Initialize array of srv/ComputeTrajectory messages.
/**
 * It allocates the memory for the number of elements and calls
 * lab02_interfaces__srv__ComputeTrajectory_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__init(lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * array, size_t size);

/// Finalize array of srv/ComputeTrajectory messages.
/**
 * It calls
 * lab02_interfaces__srv__ComputeTrajectory_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__fini(lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * array);

/// Create array of srv/ComputeTrajectory messages.
/**
 * It allocates the memory for the array and calls
 * lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence *
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__create(size_t size);

/// Destroy array of srv/ComputeTrajectory messages.
/**
 * It calls
 * lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__destroy(lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * array);

/// Check for srv/ComputeTrajectory message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__are_equal(const lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * lhs, const lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * rhs);

/// Copy an array of srv/ComputeTrajectory messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Request__Sequence__copy(
  const lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * input,
  lab02_interfaces__srv__ComputeTrajectory_Request__Sequence * output);

/// Initialize srv/ComputeTrajectory message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * lab02_interfaces__srv__ComputeTrajectory_Response
 * )) before or use
 * lab02_interfaces__srv__ComputeTrajectory_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Response__init(lab02_interfaces__srv__ComputeTrajectory_Response * msg);

/// Finalize srv/ComputeTrajectory message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Response__fini(lab02_interfaces__srv__ComputeTrajectory_Response * msg);

/// Create srv/ComputeTrajectory message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * lab02_interfaces__srv__ComputeTrajectory_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
lab02_interfaces__srv__ComputeTrajectory_Response *
lab02_interfaces__srv__ComputeTrajectory_Response__create();

/// Destroy srv/ComputeTrajectory message.
/**
 * It calls
 * lab02_interfaces__srv__ComputeTrajectory_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Response__destroy(lab02_interfaces__srv__ComputeTrajectory_Response * msg);

/// Check for srv/ComputeTrajectory message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Response__are_equal(const lab02_interfaces__srv__ComputeTrajectory_Response * lhs, const lab02_interfaces__srv__ComputeTrajectory_Response * rhs);

/// Copy a srv/ComputeTrajectory message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Response__copy(
  const lab02_interfaces__srv__ComputeTrajectory_Response * input,
  lab02_interfaces__srv__ComputeTrajectory_Response * output);

/// Initialize array of srv/ComputeTrajectory messages.
/**
 * It allocates the memory for the number of elements and calls
 * lab02_interfaces__srv__ComputeTrajectory_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__init(lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * array, size_t size);

/// Finalize array of srv/ComputeTrajectory messages.
/**
 * It calls
 * lab02_interfaces__srv__ComputeTrajectory_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__fini(lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * array);

/// Create array of srv/ComputeTrajectory messages.
/**
 * It allocates the memory for the array and calls
 * lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence *
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__create(size_t size);

/// Destroy array of srv/ComputeTrajectory messages.
/**
 * It calls
 * lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
void
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__destroy(lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * array);

/// Check for srv/ComputeTrajectory message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__are_equal(const lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * lhs, const lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * rhs);

/// Copy an array of srv/ComputeTrajectory messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab02_interfaces
bool
lab02_interfaces__srv__ComputeTrajectory_Response__Sequence__copy(
  const lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * input,
  lab02_interfaces__srv__ComputeTrajectory_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // LAB02_INTERFACES__SRV__DETAIL__COMPUTE_TRAJECTORY__FUNCTIONS_H_
