#!/usr/bin/env python
"""
Example Python file for use with the User Scripts plugin.
"""

try:
    import indigo  # noqa
except ImportError:
    ...

indigo.server.speak("Hello World!")
indigo.server.log("Hello World! (from python)")
