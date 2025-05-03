run_group() {
  local desc="$1"; shift
  local exes=("$@")
  echo
  echo "==================================== Group: $desc ======================================="
  echo "==========================================================================="
  echo "==========================================================================="
  echo "==========================================================================="
  echo "==========================================================================="
  pids=()
  for exe in "${exes[@]}"; do
    echo "launching: $exe"
    ros2 run demo_nodes_cpp "$exe" &  
    pids+=($!)
  done
  echo
  read -rp "Press…"
  kill "${pids[@]}" 2>/dev/null
  wait "${pids[@]}" 2>/dev/null
}

run_group "Basic Talker & Listener" \
  talker \
  listener \
  listener_best_effort

run_group "Basic Server & Clients" \
  add_two_ints_server \
  add_two_ints_client \
  add_two_ints_client_async

run_group "Timers (one_off_timer)" \
  one_off_timer

run_group "Timers (reuse_timer)" \
  reuse_timer

run_group "Serialized Messaging" \
  talker_serialized_message \
  listener_serialized_message

run_group "Content‐Filter Messaging" \
  content_filtering_subscriber \
  content_filtering_publisher

run_group "List Parameters (sync & async)" \
  list_parameters \
  list_parameters_async

run_group "Set & Get Parameters (sync & async)" \
  set_and_get_parameters \
  set_and_get_parameters_async

run_group "Allocator Tutorial" \
  allocator_tutorial

run_group "Parameter Events (sync)" \
  parameter_events

run_group "Parameter Events (async)" \
  parameter_events_async

run_group "Even Parameters Node" \
  even_parameters_node

run_group "Set Parameters Callback" \
  set_parameters_callback

run_group "Parameter Blackboard" \
  parameter_blackboard

run_group "Parameter Event Handler" \
  parameter_event_handler

run_group "Loaned-Message Talker" \
  talker_loaned_message

run_group "Matched Event Detect" \
  matched_event_detect

echo
