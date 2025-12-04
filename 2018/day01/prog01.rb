#!/usr/bin/env ruby

input = []
#while line = gets
#    if match = /(^[-+]?[0-9]+)/.match(line)
#        input.push(match.to_s.to_i)
#    end
#end
ARGF.each do |line|
    input.push(line.to_i)
end
puts "read #{input.count} numbers"

total = 0
round = 0
seen = Hash.new(0)
catch :found_it do
    while true
        round += 1
        input.each do |num|
            total += num
            seen[total] += 1
            throw :found_it if seen[total] >= 2
        end
        puts "total is #{total} after round #{round}\n"
    end
end
puts "reached #{total} twice in round #{round}\n"
