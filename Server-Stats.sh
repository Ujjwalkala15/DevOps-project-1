#!/bin/bash

# Print a message
echo "Hello World"

# Total CPU usage
echo "Total CPU usage:"
top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8"%"}'

# Total memory usage (Free vs Used including percentage)
echo "Total memory usage:"
free -m | awk 'NR==2{printf "Used: %sMB (%.2f%%), Free: %sMB (%.2f%%)\n", $3, $3*100/$2, $4, $4*100/$2 }'

# Total disk usage (Free vs Used including percentage)
echo "Total disk usage:"
df -h | awk '$NF=="/"{printf "Used: %dGB (%s), Free: %dGB (%s)\n", $3, $5, $4, $5}'

# Top 5 processes by CPU usage
echo "Top 5 processes by CPU usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6

# Top 5 processes by memory usage
echo "Top 5 processes by memory usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6