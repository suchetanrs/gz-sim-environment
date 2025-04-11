# live_trace.sh

if [ $# -eq 0 ]; then
  echo "Provide trace session name"
  exit 1
fi

session_name="$1"
hostname=$(hostname)

#lttng create $session_name --live --ctrl-url="net://189.9.9.1" --data-url="net://189.9.9.1"
lttng create $session_name --live
#lttng enable-channel -u ros --subbuf-size=8M
#lttng enable-event -c ros -u 'ros2:*'
#lttng add-context -u -t vtid -t vpid -t procname
#lttng start

echo
echo "Live trace URI: net://localhost/host/$hostname/$session_name"
echo "Press any key to stop & destroy"
read
lttng stop
lttng destroy
