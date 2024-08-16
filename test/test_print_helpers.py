#!/usr/bin/python3

'''
Test.

Copyright (C) 2024 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

import print_helpers.helpers as print_helpers

##########################################################

def test():

    print_helpers.set_log_level( print_helpers.TRACE )

    print_helpers.print_fatal( "test" )
    print_helpers.print_error( "test" )
    print_helpers.print_warning( "test" )
    print_helpers.print_info( "test" )
    print_helpers.print_debug( "test" )
    print_helpers.print_trace( "test" )

##########################################################

if __name__ == "__main__":
   test()
