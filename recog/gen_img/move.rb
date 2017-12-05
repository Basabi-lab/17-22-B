num = ["0","1","2","3","4","5","6","7","8","9","A","B","C","=","dust"]
tmp = Array.new(20)
cclass = [14,8,9,3,6,7,11,10,1,4,5,2,13,12,14,8,9,10,11,1,4,6,3,5,7,12,2,13,8,10,6,11,1,7,3,9,5,4,2,12,13]

def move(num,cclass)
  cclass.length.times do |i|
    # puts "#{i}, #{num[cclass[i]}]"
    `mv #{i}.png raw_data/#{num[cclass[i]]}/`
  end
end

tmp.length.times do |i|
  tmp[i] = 0
end

for item in cclass do
  tmp[item] += 1
end

tmp.length.times do |i|
  print num[i]
  print " "
  puts tmp[i]
end

puts cclass.length
move(num,cclass)


