#!/usr/bin/env ruby

todo = Hash.new
steps = ("A".."Z").to_a
ARGF.each do |line|
    if match = line.match(%r{Step (\w) .* before step (\w)}i)
        todo[match[1]] ||= Array.new
        todo[match[2]] ||= Array.new
        todo[match[2]].push(match[1])
    end
end

#done = Array.new
#while ! todo.count.zero?
#    done.push(todo.select{|step,deps| deps.count.zero? }.keys.sort.shift)
#    todo.delete(done[-1])
#    todo.map{|step,deps| deps.delete(done[-1])}
#end

worker_count = 5
step_duration = 61

workers = Array.new(worker_count){ { :step => nil, :time => 0 } }
done = Array.new
seconds = 0
while true
    #puts "TODO: #{todo}"
    #puts "WORKERS: #{workers}"
    workers.each do |worker|
        if !worker[:step].nil?
            worker[:time] -= 1
            if worker[:time] == 0
                done.push(worker[:step])
                todo.map{|step,deps| deps.delete(worker[:step])}
                worker[:step] = nil
            end
        end
        if worker[:step].nil?
            if worker[:step] = todo.select{|step,deps| deps.count.zero? }.keys.sort.shift
                todo.delete(worker[:step])
                worker[:time] = steps.find_index(worker[:step]) + step_duration
            end
        end
    end
    puts "#{seconds.to_s.rjust(3)} #{workers.map{|w| w[:step] }} #{done.join}"
    break if workers.select{|w| !w[:step].nil?}.count.zero?
    seconds += 1
end
puts "steps: #{done.join} in #{seconds} seconds"
