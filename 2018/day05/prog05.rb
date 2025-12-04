#!/usr/bin/env ruby

def react(polymer, ignore)
    result = ''
    last_unit = ''
    polymer.each do |unit|
        #puts "result=#{result} | last_unit=#{last_unit} | unit=#{unit}"
        next if ignore.include?(unit)
        if last_unit != unit and last_unit.upcase == unit.upcase
            #puts "BOOM"
            last_unit = ''
            if result != ''
                last_unit = result[-1]
                result = result[0..-2]
            end
        else
            result << last_unit
            last_unit = unit
        end
    end
    result << last_unit
    return result
end

polymer = ARGF.readline.chomp.chars
result = react(polymer, [])
puts "resulting polymer is #{result.length} units long"

results = []
'A'.upto('Z').each do |letter|
    results.push(react(polymer, [letter, letter.downcase]).length)
end
puts "shortest resulting polymer is #{results.min} units long"
