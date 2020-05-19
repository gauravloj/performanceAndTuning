#!/bin/bash

ifconfig en0 down
ifconfig en0 mode monitor
ifconfig en0 down up
ifconfig en0 | grep mode
