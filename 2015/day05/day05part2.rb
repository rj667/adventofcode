#!/usr/bin/env ruby

nice = 0
ARGF.each do |line|
    line.chomp.chars
    next if line.match(%r{ab|cd|pq|xy})
end
