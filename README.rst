Publisher
=========

The main class is defined in pub.py.  The scripts listen.py and
test_udp.py are just for test and demo.

To test/demo, run::

  $ python listen.py &
  $ python test_udp.py  

Discussion
==========

The Publisher class helps with adding an output channel to a set of
scripts that will be spawned through some unknown intelligent entity
that wants to collect structured information from the script.
Normally a script prints information to stdout, and error messages to
stderr... and with this Publisher the script can also push
JSON-formatted data to anyone who is listening in the right way.

The design approach for the Publisher class are:

- The use of Publisher in the scripts should be concise and intuitive.
  Script writers will not want to waste effort wrestling with an
  output engine that they are not using.
- Configuration or special handling for different output engines
  within the calling script should be unnecessary and discouraged.

