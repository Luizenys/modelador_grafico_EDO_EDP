#!/usr/bin/env bash

python3 main.py 
julia dem.jl "points_list.json"
julia mdf.jl 