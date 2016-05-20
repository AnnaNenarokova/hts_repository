TRIM_EXEC = 'java -jar /home/nenarokova/tools/Trimmomatic-0.36/trimmomatic-0.36.jar'
ADAPTERS_PATH = '/media/4TB1/kinetoplastids_hinxton/illumina_adapters.fa'
PARAMS = {
    0 => { name: :some_name, value: "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30" },
    1 => { name: :some_name, value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30" },
    2 => { name: :some_name, value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:50" },
    3 => { name: :some_name, value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30" },
    4 => { name: :some_name, value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:50" }
}.freeze

def run_program(folder, input_filename, params)
    file_fw = "#{folder}/raw_reads/#{input_filename}_1.fastq"
    file_rv = "#{folder}/raw_reads/#{input_filename}_2.fastq"

    p_out_fw = "#{folder}/trimmed_reads/#{input_filename}_paired_out_fw_#{params[:name]}.fastq"
    u_out_fw = "#{folder}/trimmed_reads/#{input_filename}_unpaired_out_fw_#{params[:name]}.fastq"
    p_out_rv = "#{folder}/trimmed_reads/#{input_filename}_paired_out_rv_#{params[:name]}.fastq"
    u_out_rv = "#{folder}/trimmed_reads/#{input_filename}_unpaired_out_rv_#{params[:name]}.fastq"
    trimming_log = "#{folder}/trimming_logs/#{input_filename}_trimming_#{params[:name]}.log"
    output_log = "#{folder}/trimming_logs/#{input_filename}_output_#{params[:name]}.log"

    exec = "#{TRIM_EXEC} PE -threads 1 -trimlog #{trimming_log} #{file_fw} #{file_rv} #{p_out_fw} #{u_out_fw} #{p_out_rv} #{u_out_rv} #{params[:value]}"
    puts " >>> run_program: #{folder} - #{input_filename} <<<"
    puts "executing #{exec}"
    puts
    # Process.fork do
    #     `#{exec} > #{output_log}`
    # end
end

def process_folder(folder)
    Dir.glob("#{folder}/raw_reads/*.fastq").map{ |f| f.split('/').last.gsub(/_[12]\.fastq/, '') }.uniq.each do |name|
        PARAMS.each{ |k,v| run_program folder, name, v}
    end
end

def perform
    process_folder '/media/4TB1/kinetoplastids_hinxton/illumina/miseq'
    process_folder '/media/4TB1/kinetoplastids_hinxton/illumina/hiseq'
end
