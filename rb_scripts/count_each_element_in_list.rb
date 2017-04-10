#!/usr/bin/ruby
f_path = '/home/anna/bioinformatics/blasto/triat_all_found_taxids.txt'
l = IO.readlines(f_path)
puts l.uniq.length
l.uniq.each { |e| puts "#{e}#{l.count(e)}" }
