import sys

from .AFK import AFK

duration = sys.argv[1]


print("Press Ctrl+C to stop")

try:
    AFK(duration=duration)
except KeyboardInterrupt:
    print("Stopped by user")
