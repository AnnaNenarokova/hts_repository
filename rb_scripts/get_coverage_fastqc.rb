#!/usr/bin/ruby
require 'csv'

def get_read_length(file)
    f = File.open(file, "r")
    total_length = 0
    re_header = /#Length\tCount/
    re_count = /(?<l1>\d+)-(?<l2>\d+)\t(?<n>(\d{2,}\.\d)|(\d\.\d+E\d+))/
    in_len_block = false
    f.each_line do |line|
        if in_len_block
            if re_count =~ line
                match = line.match(re_count)
                avl = (match[:l1].to_f + match[:l2].to_f)/2.0
                total_length += avl * match[:n].to_f
            else
                break
            end
        elsif re_header =~ line
            in_len_block = true
        end
    end
    f.close
    return total_length
end

def write_hash_array(data, file, keys=nil)
    CSV.open(file, "wb") do |csv|
        if not keys
            keys = data.first.keys
            csv << keys
        end
        data.each do |element|
            csv << keys.map{ |k| element[k] }
        end
    end
end


Dir.chdir("/media/4TB1/kinetoplastids_hinxton/illumina/miseq/fastqc_results/zip/trimmed_reads")
Dir.glob('*/').each do folder
    re_folder = /(?<name>(18021|18098)_\d#\d)_(paired|unpaired)_out_(fw|rv)_(?<params>(?<adapter>(ad_)?)q(?<qual>\d+)_l(?<minlen>\d+)_fastqc)\//
end

threads = 32

perform(folders, threads)
