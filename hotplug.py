# hotplug.py
#
# This file is part of dfmon.
#
# dfmon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dfmon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dfmon.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Ingo Bressler (April 2010)

import sys
import os
import getopt

from hotplugCmd import consoleMenu
from hotplugQt import qtMenu

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def cmdName(argv):
    if not argv or len(argv) <= 0:
        return ""
    else:
        return os.path.basename(argv[0])

def showUsage(argv):
    msg = "USAGE: " + cmdName(argv) + " <option>\n"
    msg += "    Where <option> is one of:\n"
    msg += "    -c      command line mode\n"
    msg += "    No option starts the GUI mode."
    return msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hc", ["help", "console"])
        except getopt.error, msg:
             raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, cmdName(argv)+": For help use --help"
        return 2
#    print "opts:", opts, "args:", args
    if (unicode("-h"), "") in opts or (unicode("--help"), "") in opts:
        print >>sys.stdout, showUsage(argv)
        return 0
    elif (unicode("-c"), "") in opts or (unicode("--console"), "") in opts:
        return consoleMenu()
    else:
        return qtMenu(argv)

if __name__ == "__main__":
    sys.exit(main())
