#!/usr/bin/env ruby

require "pp"

points = Array.new
min_x = min_y = max_x = max_y = 0
ARGF.each do |line|
    position = line.match(/position=<\s*(?<x>-?\d+),\s*(?<y>-?\d+)>/)
    velocity = line.match(/velocity=<\s*(?<x>-?\d+),\s*(?<y>-?\d+)>/)
    point = {
        :pos => { :x => position[:x].to_i, :y => position[:y].to_i },
        :vel => { :x => velocity[:x].to_i, :y => velocity[:y].to_i },
    }
    p point
    points.push(point)
end
pp points

#grid = Array.new(max_y+1){ Array.new(max_x+1, '.') }
#grid[y][x] = closest[0]
#puts grid.map { |a| a.map { |i| i.to_s.rjust(2) }.join }

prev_area = nil
steps = 0
while true
    min_x = max_x = min_y = max_y = nil
    points.each do |point|
        min_x = [min_x, point[:pos][:x]].compact.min
        max_x = [max_x, point[:pos][:x]].compact.max
        min_y = [min_y, point[:pos][:y]].compact.min
        max_y = [max_y, point[:pos][:y]].compact.max
    end
    area = (max_x - min_x) * (max_y - min_y)
    #pp area
    if ! prev_area.nil? and prev_area < area
        points.each do |point|
            point[:pos][:x] -= point[:vel][:x]
            point[:pos][:y] -= point[:vel][:y]
        end
        break
    end
    prev_area = area
    points.each do |point|
        point[:pos][:x] += point[:vel][:x]
        point[:pos][:y] += point[:vel][:y]
    end
    steps += 1
end
puts "min_x=#{min_x} max_x=#{max_x} min_y=#{min_y} max_y=#{max_y}"
grid = Array.new(max_y + min_y.abs + 1){ Array.new(max_x + min_y.abs + 1) }
#pp grid
points.each do |point|
    puts "x=#{point[:pos][:x]} y=#{point[:pos][:y]}"
    grid[point[:pos][:y] + min_y.abs][point[:pos][:x] + min_x.abs] = "#"
end
puts grid.map { |a| a.map { |i| i.to_s.rjust(1) }.join }
puts steps
