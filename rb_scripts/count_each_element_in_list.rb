#!/usr/bin/ruby
f_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/trypanosomatids/novymonas/blast_reports/E262_endosymbiont_gen/count.txt'
l = IO.readlines(f_path)
puts l.uniq.length
l.uniq.each { |e| puts "#{e} - #{l.count(e)}" }
