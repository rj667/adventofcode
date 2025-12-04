#!/usr/bin/env ruby

names = ('A'..'Z').to_a + ('a'..'z').to_a
max_mdist_sum = 10000

coord = Hash.new
min_x = min_y = max_x = max_y = 0
ARGF.each do |line|
    x,y = line.split(/\D+/).map {|s| s.to_i}
    max_x = x if max_x < x
    max_y = y if max_y < y
    puts "#{x}, #{y}"
    coord[names.shift] = { :x => x, :y => y }
end
#max_x += 1

#grid = Array.new(max_y+1){ Array.new(max_x+1, '.') }
size = Hash.new(0)
size_safe_area = 0
infinite = Hash.new(false)
min_y.upto(max_y).each do |y|
    min_x.upto(max_x).each do |x|
        mdists = Hash.new
        coord.keys.each do |n|
            mdists[n] = (coord[n][:x]-x).abs + (coord[n][:y]-y).abs
        end
        closest = mdists.select{|k,v| v == mdists.values.min}.keys
        #puts "x=#{x} y=#{y} closest=#{closest}"
        if closest.count == 1
            #grid[y][x] = closest[0]
            size[closest[0]] += 1
            if [min_x, max_x].include?(x) or [min_y, max_y].include?(y)
                infinite[closest[0]] = true
            end
        end
        if mdists.values.sum < max_mdist_sum
            size_safe_area += 1
        end
    end
end
#puts grid.map { |a| a.map { |i| i.to_s.rjust(2) }.join }
maxsize = size.reject {|k,v| infinite[k]}.values.max
puts "largest non-infinite area is #{maxsize}"
puts "size of the safe area is #{size_safe_area}"
