#!/usr/bin/env ruby

grid = Hash.new(0)
sx = sy = 0
rx = ry = 0
grid[[sx,sy].join(",")] += 1
grid[[rx,ry].join(",")] += 1
count = 0
ARGF.readline.chomp.chars.each do |c|
    if count.even?
        sy -= 1 if c == '^'
        sy += 1 if c == 'v'
        sx += 1 if c == '>'
        sx -= 1 if c == '<'
        grid[[sx,sy].join(",")] += 1
    else
        ry -= 1 if c == '^'
        ry += 1 if c == 'v'
        rx += 1 if c == '>'
        rx -= 1 if c == '<'
        grid[[rx,ry].join(",")] += 1
    end
    count += 1
end
p grid.select{|k,v| v >= 1}.keys.count
