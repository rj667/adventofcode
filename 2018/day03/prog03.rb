#!/usr/bin/env ruby

fabric_x = 1000
fabric_y = 1000
fabric = Array.new(fabric_y){ Array.new(fabric_x){ Array.new }}
regex = %r{^#(?<id>\d+)\s+@\s+(?<x0>\d+),(?<y0>\d+)\s*:\s+(?<dx>\d+)x(?<dy>\d+)}
claims = Hash.new(0)
ARGF.each do |line|
    if match = line.match(regex)
        id = match[:id].to_i
        x0 = match[:x0].to_i
        y0 = match[:y0].to_i
        dx = match[:dx].to_i
        dy = match[:dy].to_i
        x0.upto(x0+dx-1).each do |x|
            y0.upto(y0+dy-1).each do |y|
                fabric[y][x].push(id)
            end
        end
        claims[id] += 1
    end
end
width = fabric.flatten.max.to_s.size+8
#puts fabric.map { |a| a.map { |i| i.to_s.rjust(width) }.join }

overlap = 0
(0..fabric_x-1).each do |x|
    (0..fabric_y-1).each do |y|
        if fabric[y][x].size > 1
            overlap += 1
            fabric[y][x].each do |id|
                claims.delete(id)
            end
        end
    end
end

puts "#{overlap} inches overlap\n"
puts "non-overlapping claims: #{claims.keys}\n"
