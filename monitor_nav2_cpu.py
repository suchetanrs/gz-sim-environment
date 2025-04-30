#!/usr/bin/env python3
"""
monitor_cpu.py: Monitor CPU usage of specified processes.

Usage:
    python monitor_cpu.py process_name [process_name ...]
"""

import psutil
import time
import argparse
import sys


def get_monitored_procs(names):
    procs = []
    for p in psutil.process_iter(['name']):
        try:
            if p.info['name'] and p.info['name'].lower() in names:
                procs.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procs


def main():
    parser = argparse.ArgumentParser(description="Monitor CPU usage of specified processes.")
    parser.add_argument('names', metavar='NAME', nargs='+', help='Process names to monitor')
    args = parser.parse_args()

    names = [n.lower() for n in args.names]

    # Prime CPU percent measurements
    try:
        monitored = get_monitored_procs(names)
        for p in monitored:
            p.cpu_percent(None)
    except Exception as e:
        print(f"Error initializing CPU percent: {e}", file=sys.stderr)

    print(f"Monitoring processes: {', '.join(args.names)}")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
            monitored = get_monitored_procs(names)
            total = 0.0
            print("=" * 40)
            print(time.strftime("%Y-%m-%d %H:%M:%S"))
            for p in monitored:
                try:
                    usage = p.cpu_percent(None)
                    total += usage
                    print(f"{p.info['name']} (PID {p.pid}): {usage:.2f}%")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            print("-" * 40)
            print(f"Total CPU usage: {total:.2f}%")
    except KeyboardInterrupt:
        print("Exiting.")
        sys.exit(0)


if __name__ == '__main__':
    main()
