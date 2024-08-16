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
##########################################################

NONE=0
FATAL=1
ERROR=2
WARNING=3
INFO=4
DEBUG=5
TRACE=6

##########################################################

gl_log_level=INFO
gl_has_color=True

##########################################################

try:
    from termcolor import colored
except ModuleNotFoundError:
    gl_has_color=False

##########################################################

def set_log_level( log_level: int ):
    global gl_log_level
    gl_log_level = log_level

##########################################################

def _colorize( s: str, color: str, attrs: [] ):
    if gl_has_color:
        return colored( s, color, None, attrs )
    return s

##########################################################

def pref_fatal( s: str ):
    pref = _colorize( 'FATAL: ', 'magenta', [] )
    return pref + s

def pref_error( s: str ):
    pref = _colorize( 'ERROR: ', 'red', [] )
    return pref + s

def pref_warning( s: str ):
    pref = _colorize( 'WARNING: ', 'yellow', [] )
    return pref + s

def pref_info( s: str ):
    return "INFO: " + s

def pref_debug( s: str ):
    pref = _colorize( 'DEBUG: ' + s, 'grey', attrs=['bold'] )
    return pref

def pref_trace( s: str ):
    pref = _colorize( 'TRACE: ' + s, 'grey', attrs=['bold'] )
    return pref

##########################################################

def print_fatal( s ):
    if gl_log_level < FATAL:
        return
    print( pref_fatal( s ) )

##########################################################

def print_error( s ):
    if gl_log_level < ERROR:
        return
    print( pref_error( s ) )

##########################################################

def print_warning( s ):
    if gl_log_level < WARNING:
        return
    print( pref_warning( s ) )

##########################################################

def print_info( s ):
    if gl_log_level < INFO:
        return
    print( pref_info( s ) )

##########################################################

def print_debug( s, end_par = "\n", flush_par = False ):
    if gl_log_level < DEBUG:
        return
    print( pref_debug( s ), end=end_par, flush=flush_par )

##########################################################

def print_trace( s ):
    if gl_log_level < TRACE:
        return
    print( pref_trace( s ) )

##########################################################
