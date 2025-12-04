#!/usr/bin/env ruby

require 'pp'
require 'algorithms'

input = ARGF.readline.chomp
match = input.match(%r{^(?<players>\d+).*?(?<points>\d+)})
players = match[:players].to_i
last_marblenum = match[:points].to_i

marblenum = 0
player = 1
score = Hash.new(0)
score[0] = 0
circle = Containers::Deque.new(0)
while (marblenum += 1) <= last_marblenum
    #puts "#{marblenum}"
    if marblenum % 23 == 0
        score[player] += marblenum
        7.times{ circle.push_front(circle.pop_back) }
        score[player] += circle.pop_front
    else
        2.times{ circle.push_back(circle.pop_front) }
        circle.push_front(marblenum)
    end
    #p circle
    player += 1
    player = 1 if player > players
end
puts "marble=#{marblenum} highscore: #{score.max_by{|k,v| v}[1]}"

