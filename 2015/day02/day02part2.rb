#!/usr/bin/env ruby

paper = 0
ribbon = 0
ARGF.each do |line|
    l,w,h = line.split('x').map{|x| x.to_i}
    paper += 2*l*w + 2*w*h + 2*h*l + [l*w, w*h, h*l].min
    [l,w,h].min(2).each do |x|
        ribbon += 2*x
    end
    ribbon += l*w*h
end
puts "#{paper} square feet of paper"
puts "#{ribbon} feet of ribbon"
