#!/usr/bin/ruby
f_path = '/media/anna/data/Dropbox/PhD/projects/trypanosoma/mito/bsf_mito_alena/pcf.csv'
l = IO.readlines(f_path)
puts l.uniq.length
l.uniq.each { |e| puts "#{e}#{l.count(e)}" }
