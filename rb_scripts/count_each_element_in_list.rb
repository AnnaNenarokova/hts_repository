#!/usr/bin/ruby
a = ['a', 'a', 'b', 'b', 'b', 'c']

a.uniq.each { |e| puts "#{e} - #{a.count(e)}" }
