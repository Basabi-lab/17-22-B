def rename_tmp(letter)
  i = 0
  # puts `ls #{letter}`.split(/\R/)
  `ls #{letter}/`.split(/\R/).each do |img|
    # puts sprintf("mv %s %s.png", [letter,"/",img].join, [letter,"/","TMP:",letter,i.to_s].join)
    `#{sprintf("mv %s %s.png", [letter,"/",img].join, [letter,"/","TMP:",letter,i.to_s].join)}`
    i += 1
  end
end

def rename(letter)
  i = 0
  # puts `ls #{letter}`.split(/\R/)
  `ls #{letter}/`.split(/\R/).each do |img|
    # puts sprintf("mv %s %s.png", [letter,"/",img].join, [letter,"/",letter,i.to_s].join)
    `#{sprintf("mv %s %s.png", [letter,"/",img].join, [letter,"/",letter,":",i.to_s].join)}`
    i += 1
  end
end

`ls`.split(/\R/).each do |letter|
  if letter != "numeric.rb"
    rename_tmp(letter)
    rename(letter)
  end
end

