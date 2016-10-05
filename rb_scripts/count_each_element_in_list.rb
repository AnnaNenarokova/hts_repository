#!/usr/bin/ruby
l = ['a', 'a', 'b', 'b', 'b', 'c']

l.uniq.each { |e| puts "#{e} - #{l.count(e)}" }
