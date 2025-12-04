#!/usr/bin/env ruby

regex = %r{^\[(?<year>\d+)-(?<mon>\d+)-(?<day>\d+) (?<hour>\d+):(?<min>\d+)\] (?<msg>.*)}
records = Hash.new
ARGF.each do |line|
    if match = line.match(regex)
        datetime = "#{match[:year].to_s}#{match[:mon].to_s}#{match[:day].to_s}#{match[:hour].to_s}#{match[:min].to_s}"
        records[datetime] = {:min => match[:min].to_i, :msg => match[:msg].to_s}
    end
end

sleep = Hash.new
schedule = Hash.new
guard = 0
begin_sleep = 0
records.keys.sort.each do |datetime|

    puts "#{datetime} #{records[datetime][:msg]}"

    if match = records[datetime][:msg].match(%r{#(?<guard>\d+) begins shift})
        guard = match[:guard].to_i
        sleep[guard] ||= 0
        schedule[guard] ||= Array.new(60, 0)
    end

    if records[datetime][:msg] == "falls asleep"
        begin_sleep = records[datetime][:min]
    end

    if records[datetime][:msg] == "wakes up"
        end_sleep = records[datetime][:min] - 1
        begin_sleep.upto(end_sleep).each do |min|
            sleep[guard] += 1
            schedule[guard][min] += 1
        end
    end

end

guard = sleep.max_by{|guard, total| total}[0]
min = schedule[guard].find_index(schedule[guard].max)

puts "guard #{guard} sleeps the most, and most in minute #{min}. Answer: #{guard * min}"

minute = Hash.new
schedule.keys.each do |guard|
    minute[guard] = schedule[guard].max
end
guard, maxmin = minute.max_by{|guard, min| min}
min = schedule[guard].find_index(maxmin)
puts "guard #{guard} is most frequently asleep in minute #{min}. Answer: #{guard * min}"
