#!/usr/bin/env ruby

require 'pp'
$stdout.sync = true

input = ARGF.readline.chomp
match = input.match(%r{^(?<players>\d+).*?(?<points>\d+)})
players = match[:players].to_i
last_marblenum = match[:points].to_i

marblenum = 0
player = 1
score = Hash.new(0)
score[0] = 0
circle = []
while true
    #puts "#{marblenum}"
    if marblenum != 0 and marblenum % 23 == 0
        score[player] += marblenum
        score[player] += circle[-7]
        #puts "current=#{marblenum} -7=#{circle[-7]} score=#{marblenum+circle[-7]}"
        circle.delete_at(-7)
        circle.rotate!(-6)
    else
        circle.insert(2, marblenum)
        #p circle
        circle.rotate!(2)
        circle.delete(nil) if marblenum <= 1
    end
    #p circle
    break if marblenum == last_marblenum
    marblenum += 1
    player += 1
    player = 1 if player > players
end
puts "marble=#{marblenum} highscore: #{score.max_by{|k,v| v}[1]}"
