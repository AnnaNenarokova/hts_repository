#!/usr/bin/ruby
f_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/ko.txt'
l = IO.readlines(f_path)
puts l.uniq.length
# l.uniq.each { |e| puts "#{e} - #{l.count(e)}" }
