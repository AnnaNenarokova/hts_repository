#!/usr/bin/ruby

def extract_stats(file)
    f = File.open(file, "r")
    re = /Input Read Pairs: (?<total>\d+) Both Surviving: (?<both>\d+) \((?<both%>\d+.\d+)%\) Forward Only Surviving: (?<forward>\d+) \((?<forward%>\d+.\d+)%\) Reverse Only Surviving: (?<reverse>\d+) \((?<reverse%>\d+.\d+)%\) Dropped: (?<dropped>\d+) \((?<dropped%>\d+.\d+)%\)/
    f.each_line do |line|
        puts line
        if re =~ line
            stats = Hash[ line.match(re).names.zip( line.match(re).captures ) ]
            puts stats
        end
        puts
    end
    f.close
end

def analyze_trimming(folder)
    Dir.chdir(folder)
    Dir.glob("*output*.log").each{ |f| puts f }
end

folder='/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/trimming_logs/short_logs'

file = '/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/trimming_logs/short_logs/E262_output_q15_l30.log'
extract_stats(file)
