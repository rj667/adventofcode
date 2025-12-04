#!/usr/bin/env ruby

require 'pp'

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
    min_x = point[:pos][:x] if min_x > point[:pos][:x]
    max_x = point[:pos][:x] if max_x < point[:pos][:x]
    min_y = point[:pos][:y] if min_y > point[:pos][:y]
    max_y = point[:pos][:y] if max_y < point[:pos][:y]
    points.push(point)
end
#pp points

#grid = Array.new(max_y+1){ Array.new(max_x+1, '.') }
#grid[y][x] = closest[0]
#puts grid.map { |a| a.map { |i| i.to_s.rjust(2) }.join }


while true
    dx = min_x < 0 ? min_x.abs : 0
    dy = min_y < 0 ? min_y.abs : 0
    puts "min_x=#{min_x} max_x=#{max_x} dx=#{dx} min_y=#{min_y} max_y=#{max_y} dy=#{dy}"
    grid = Array.new(max_y+dy+1){ Array.new(max_x+dx+1) }
    #puts grid.map { |a| a.map { |i| i.to_s.rjust(2) }.join }
    points.each do |point|
        x = point[:pos][:x] + dx
        y = point[:pos][:y] + dy
        puts "x=#{x} y=#{y}"
        grid[y][x] = "#"
        point[:pos][:x] += point[:vel][:x]
        point[:pos][:y] += point[:vel][:y]
        min_x = point[:pos][:x] if min_x > point[:pos][:x]
        max_x = point[:pos][:x] if max_x < point[:pos][:x]
        min_y = point[:pos][:y] if min_y > point[:pos][:y]
        max_y = point[:pos][:y] if max_y < point[:pos][:y]
    end
    puts grid.map { |a| a.map { |i| i.to_s.rjust(1) }.join }
end
