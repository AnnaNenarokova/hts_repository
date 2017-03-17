#!/usr/bin/ruby
f_path = '/home/anna/Dropbox/PhD/bioinformatics/euglena/final_prediction/summary.csv'
l = IO.readlines(f_path)
puts l.uniq.length
l.uniq.each { |e| puts "#{e}#{l.count(e)}" }
