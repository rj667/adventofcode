#!/usr/bin/env ruby

floor = 0
pos = 0
ARGF.readline.chomp.chars.each do |c|
    pos += 1
    floor += 1 if c == '('
    floor -= 1 if c == ')'
    puts "basement at position #{pos}" if floor == -1
end
puts "floor #{floor}"
