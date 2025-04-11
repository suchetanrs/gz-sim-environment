# bt2_lttng_live.py

import datetime
import sys
from typing import List

import bt2


def handle_trace_event(msg: bt2._EventMessageConst) -> None:
    event = msg.event
    ns_from_origin = msg.default_clock_snapshot.ns_from_origin
    timestamp = datetime.datetime.fromtimestamp(ns_from_origin / 1e9)
    print(f'{timestamp} {event.name}')
    # Accces field with event['field_name']
    # See:
    #   https://babeltrace.org/docs/v2.0/python/bt2/examples.html#get-a-specific-event-field-s-value
    # TODO
    if event.name == 'ros2:rclcpp_intra_publish':
        publisher_handle = event['publisher_handle']
        print(f'\tpub handle: {publisher_handle}')
    elif event.name == 'ros2:rclcpp_ring_buffer_dequeue':
        buffer = event['buffer']
        print(f'\tbuffer: {buffer}')


def process_live_trace(uri: str) -> None:
    # See example here:
    #   https://babeltrace.org/docs/v2.0/python/bt2/examples.html#create-explicit-source-components

    # Just switch source component to lttng-live:
    #   https://babeltrace.org/docs/v2.0/man7/babeltrace2-source.ctf.lttng-live.7/
    msg_it = bt2.TraceCollectionMessageIterator(
        bt2.ComponentSpec.from_named_plugin_and_component_class('ctf', 'lttng-live', {
            # See:
            #   https://babeltrace.org/docs/v2.0/man7/babeltrace2-source.ctf.lttng-live.7/#doc-_initialization_parameters
            'inputs': [uri],
        }),
    )

    # Ignore exception raised when we run out of events (i.e., consume too quickly)
    # TODO(christophebedard) not sure if there is a better way to do this
    while True:
        try:
            for msg in msg_it:
                if type(msg) is bt2._EventMessageConst:
                    handle_trace_event(msg)
        except bt2.TryAgain:
            # print("Ignoring exception")
            pass


def main(argv: List[str]) -> int:
    if 1 != len(argv):
        print('provide 1 LTTng live path, e.g.: net://localhost/host/$HOSTNAME/session-name')
        print('print available session: babeltrace2 --input-format=lttng-live net://localhost')
        return 1
    live_uri = argv[0]
    print(f'LTTng live URI: {live_uri}')
    process_live_trace(live_uri)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
