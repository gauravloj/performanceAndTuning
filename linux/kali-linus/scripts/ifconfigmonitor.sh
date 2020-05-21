#!/bin/bash

ifconfig en0 down
iwconfig en0 mode monitor
ifconfig en0 up
iwconfig en0 | grep mode
