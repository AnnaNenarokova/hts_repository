#!/usr/bin/env ruby
require 'bio'
require 'pathname'
require 'slop'

params = Slop.parse do |o|
  o.string '-fasta', '(required) Input file.'
  o.string '-bed', 'input bed file.'
  o.on '-h', '--help', 'Print options' do
    puts o
    exit
  end
end

output_path = params[:bed].split('.').insert(-2, 'clean').join('.')
bad_output_path = params[:bed].split('.').insert(-2, 'deleted').join('.')

genome_dict = {}

Bio::FlatFile.open(Bio::FastaFormat, params[:fasta]).each do |fasta_format|
  genome_dict[fasta_format.entry_id] = fasta_format.nalen
end

File.open(output_path, 'w') do |f|
  File.open(bad_output_path, 'w') do |bad_f|
    File.open(params[:bed], 'r').each do |line|
      splitted = line.split("\t")
      id = splitted[0]
      start = splitted[1].to_i
      finish = splitted[2].to_i

      unless genome_dict.include?(id)
        raise "fasta file not includes #{id}"
      end

      if start < 0 || finish > genome_dict[id]
        bad_f.puts line
      else
        f.puts line
      end
    end
  end
end
