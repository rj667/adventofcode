#!/usr/bin/env ruby

require 'digest'

secret = ARGF.readline.chomp
int = 0
while true
    sum = Digest::MD5.hexdigest(secret + int.to_s)
    if sum.start_with?("00000")
        puts "int=#{int} md5sum=#{sum}"
        break
    end
    int += 1
end
