#!/usr/bin/python3

'''
Print Helpers.

Copyright (C) 2021 Dr. Sergey Kolevatov

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

from termcolor import colored

##########################################################

NONE=0
FATAL=1
ERROR=2
WARNING=3
INFO=4
DEBUG=5
TRACE=6

gl_log_level=INFO

##########################################################

def set_log_level( log_level: int ):
    global gl_log_level
    gl_log_level = log_level

##########################################################

def print_fatal( s ):
    if gl_log_level < FATAL:
        return
    pref = colored( 'FATAL: ', 'magenta' )
    print( pref + s )

##########################################################

def print_error( s ):
    if gl_log_level < ERROR:
        return
    pref = colored( 'ERROR: ', 'red' )
    print( pref + s )

##########################################################

def print_warning( s ):
    if gl_log_level < WARNING:
        return
    pref = colored( 'WARNING: ', 'yellow' )
    print( pref + s )

##########################################################

def print_info( s ):
    if gl_log_level < INFO:
        return
    print( "INFO: " + s )

##########################################################

def print_debug( s, end_par = "\n", flush_par = False ):
    if gl_log_level < DEBUG:
        return
    pref = colored( 'DEBUG: ' + s, 'grey', attrs=['bold'] )
    print( pref, end=end_par, flush=flush_par )

##########################################################

def print_trace( s ):
    if gl_log_level < TRACE:
        return
    pref = colored( 'TRACE: ' + s, 'grey', attrs=['bold'] )
    print( pref )

##########################################################
