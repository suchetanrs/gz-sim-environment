#!/usr/bin/env python3
import os
import sys
import socket
from lttngpy import impl as lttngpy

def main():
    if len(sys.argv) < 2:
        print("Provide trace session name")
        sys.exit(1)
    session_name = sys.argv[1]
    hostname = socket.gethostname()

    trace_dir = os.path.join("/root/lttng-traces", session_name)

    # Create a live session
    ret = lttngpy.lttng_create_session_live(session_name=session_name, url="net://localhost", timer_interval=1000000)
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to create live session '{session_name}': {error}")

    # Enable channel ros
    ret = lttngpy.enable_channel(
        session_name=session_name,
        domain_type=lttngpy.LTTNG_DOMAIN_UST,
        buffer_type=lttngpy.LTTNG_BUFFER_PER_UID,
        channel_name="ros",
        overwrite=0,
        subbuf_size=8 * 4096,
        num_subbuf=2,
        switch_timer_interval=200,
        read_timer_interval=200,
        output=lttngpy.LTTNG_EVENT_MMAP,
    )
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to enable channel 'ros': {error}")

    # enable events ros2:*
    ret = lttngpy.enable_events(
        session_name=session_name,
        domain_type=lttngpy.LTTNG_DOMAIN_UST,
        event_type=lttngpy.LTTNG_EVENT_TRACEPOINT,
        channel_name="ros",
        events={"ros2:*"},
    )
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to enable event 'ros2:*': {error}")

    # add more context fields to trace
    ret = lttngpy.add_contexts(
        session_name=session_name,
        domain_type=lttngpy.LTTNG_DOMAIN_UST,
        channel_name="ros",
        context_fields={"vtid", "vpid", "procname"},
    )
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to add context fields: {error}")

    # start tracing
    ret = lttngpy.lttng_start_tracing(session_name=session_name)
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to start tracing: {error}")

    print("")
    print(f"Live trace URI: net://localhost/host/{hostname}/{session_name}")
    input("Press Enter to stop & destroy...")

    # stop tracing
    ret = lttngpy.lttng_stop_tracing(session_name=session_name)
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to stop tracing: {error}")

    # destroy session
    ret = lttngpy.lttng_destroy_session(session_name=session_name)
    if ret < 0:
        error = lttngpy.lttng_strerror(ret)
        raise RuntimeError(f"failed to destroy session: {error}")

if __name__ == '__main__':
    if not lttngpy.is_available():
        print("LTTng control is not available.")
        sys.exit(1)
    main()