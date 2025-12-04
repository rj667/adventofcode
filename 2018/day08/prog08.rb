#!/usr/bin/env ruby

require 'pp'

def readnode(input)
    child_node_q = input.shift
    metadata_entries_q = input.shift
    child_nodes = []
    child_node_values = []
    child_node_q.times do
        child_node, child_node_value = readnode(input)
        child_nodes.push(child_node)
        child_node_values.push(child_node_value)
    end
    metadata = input.shift(metadata_entries_q)
    value = 0
    if child_nodes.empty?
        value = metadata.sum
    else
        metadata.each do |i|
            next if i == 0
            next if child_node_values[i-1].nil?
            value += child_node_values[i-1]
        end
    end
    node = {:child_nodes => child_nodes, :metadata => metadata}
    p value
    return node, value
end

input = ARGF.readline.chomp.split.map{|x| x.to_i}
rootnode, value = readnode(input)
pp rootnode
p value
