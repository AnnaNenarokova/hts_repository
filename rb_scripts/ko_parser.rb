require 'csv'

data = File.readlines('ko_modules.txt')

result = {}
current_key = nil

data.each do |entry|
  if entry.match(/\A\s/)
    result[current_key] ||= []
    result[current_key] << entry.strip
  else
    current_key = entry.strip
  end
end

elements = result.values.flatten.uniq.sort

CSV.open('ouput.csv', 'w') do |csv|
  csv << [nil, result.keys].flatten

  elements.each do |element|
    row = []
    row << element

    result.keys.each do |key|
      if result[key].include? element
        row << 1
      else
        row << 0
      end
    end

    csv << row
  end
end
