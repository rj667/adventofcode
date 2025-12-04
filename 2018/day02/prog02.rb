#!/usr/bin/env ruby

has_exactly = Hash.new(0)
ARGF.each do |line|
    seen = Hash.new(0)
    line.each_char do |c|
        seen[c] += 1
    end
    has_exactly[2] +=1 if seen.values.include?(2)
    has_exactly[3] +=1 if seen.values.include?(3)
end
checksum = has_exactly[2] * has_exactly[3]
puts "#{has_exactly[2]} * #{has_exactly[3]} is #{checksum}\n"
