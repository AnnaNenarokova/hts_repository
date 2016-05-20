def run_program(dir, input_filename)
    trim_exec = 'java -jar /home/nenarokova/tools/Trimmomatic-0.36/trimmomatic-0.36.jar'

    file_fw = "#{dir}/illumina/raw_reads/#{input_filename}_1.fastq"
    file_rv = "#{dir}/illumina/raw_reads/#{input_filename}_2.fastq"

    p_out_fw = "#{dir}/illumina/trimmed_reads/#{input_filename}_paired_out_fw.fastq"
    u_out_fw = "#{dir}/illumina/trimmed_reads/#{input_filename}_unpaired_out_fw.fastq"
    p_out_rv = "#{dir}/illumina/trimmed_reads/#{input_filename}_paired_out_rv.fastq"
    u_out_rv = "#{dir}/illumina/trimmed_reads/#{input_filename}_unpaired_out_rv.fastq"
    trimlog = "#{dir}/illumina/trimmed_reads/#{input_filename}_trimming.log"

    # DODO: exec trim_exec with params
    params = 'LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:50'

    exec = "#{trim_exec} PE -threads 1 -trimlog #{trimlog} #{file_fw} #{file_rv} #{p_out_fw} #{u_out_fw} #{p_out_rv} #{u_out_rv} #{params} &"
    puts "executing #{dir} - #{input_filename}"
    Process.fork { system "#{exec}" }
end

def do_trim
    Dir.glob("*").each do |dir|
        input_files = Dir.glob("#{dir}/illumina/raw_reads/*")

        input_files = input_files.map{ |f| f.split('/').last.gsub(/_\d\.fastq/, '') }.uniq
        input_files.each do |f|
            run_program dir, f
        end
    end
end
