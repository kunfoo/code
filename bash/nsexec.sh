#!/bin/bash
# inspired by https://askubuntu.com/a/499850

NS_NAME="sandbox"
IF_ISOLATED="veth-isolated"
IF_HOST="veth-host"
IP_ISOLATED="192.168.200.2"
IP_HOST="192.168.200.1"
IP_NETMASK="24"

if [ $# -ne 1 ]; then
  cmd="bash"
else
  cmd="$1"
fi

if [ 0 -ne `id -u` -o -z $SUDO_USER ]; then
  echo "Error: Must be run with sudo. Expects SUDO_USER env variable."
  exit 1
fi

# setup
ip netns add $NS_NAME
ip link add $IF_ISOLATED type veth peer name $IF_HOST
ip link set $IF_ISOLATED netns $NS_NAME
ip netns exec $NS_NAME ip address add $IP_ISOLATED/$IP_NETMASK dev $IF_ISOLATED
ip address add $IP_HOST/$IP_NETMASK dev $IF_HOST
ip netns exec $NS_NAME ip link set dev $IF_ISOLATED up
ip link set dev $IF_HOST up
ip netns exec $NS_NAME ip route add default via $IP_HOST dev $IF_ISOLATED
iptables -t nat -A POSTROUTING -s $IP_ISOLATED -j MASQUERADE

# run command
echo "Running $cmd in isolated network namespace"
ip netns exec $NS_NAME sudo -u $SUDO_USER $cmd

# cleanup
iptables -t nat -D POSTROUTING -s $IP_ISOLATED -j MASQUERADE
ip netns del $NS_NAME
