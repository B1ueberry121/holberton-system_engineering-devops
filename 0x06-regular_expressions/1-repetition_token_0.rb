#!/usr/bin/env ruby
# Match and reapeat token tpreciding n using {}

puts ARGV[0].scan(/hbt{2,5}n/).join
