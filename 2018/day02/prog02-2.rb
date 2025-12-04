#!/usr/bin/env ruby

input = []
ARGF.each do |line|
    line.chomp!
    input.push(line)
end

letters = ''
catch :found_it do
    0.upto(input[0].length() -1).each do |i|
        seen = Hash.new(0)
        input.each do |id|
            letters = id.dup
            letters[i] = ''
            puts "i=#{i} id=#{id} => #{letters}"
            throw :found_it if seen[letters] != 0
            seen[letters] += 1
        end
    end
end
puts "common letters are #{letters}\n"
