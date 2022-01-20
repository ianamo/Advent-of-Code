data = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"

strings = data.split()
output = []
lengths = [7,4,2,3]

#for i, s in enumerate(strings):
#    if s == '|':
#        output.append(strings[i+1])
#        output.append(strings[i+2])
#        output.append(strings[i+3])
#        output.append(strings[i+4])

i=0
while ((i+15)<len(strings)):
  output.append(strings[i:i+15])
  i+=15

#c = 0
#for o in output:
#    if len(o) in lengths:
#        c+=1

#print(c)

for o in output:
  decode = 0
  key = {}
  while (decode ==0):
    if len(o)==2:
      key[1] = o
    if len(o)==8:
      key[8] =o
    if len(o)==4:
      key[4]=o
    if len(o)==3:
      key[7]=o
    if 1 in key.keys() and 4 in key.keys():
      k = []
      for c in key[4]:
        if c not in key[1]:
          k.append(c)
      key['db'] = "".join(k)
    if 1 in key.keys() and 7 in key.keys():
      for c in key[7]:
        if c not in key[1]:
          key['a'] = c
    if len(o)==6:
      if 1 in key.keys():
        if key[1][0] in o and key[1][1] in o:
          key[3] = o
      elif 'db' in key.keys():
        if key['db'][0] in o and key['db'][1] in o:
          key[5] = o
      elif 'db' in key.keys() and 1 in key.keys():
        key[2] = o
    if 2 in key.keys() and 3 in key.keys():
      for c in key[2]:
        if c not in key[3]:
          key['e'] = c
      for c in key[3]:
        if c not in key[2]:
          key['f'] = c
    if 4 in key.keys() and 5 in key.keys() and 'a' in key.keys():
      for c in key[5]:
        if c not in key[4] and c is not key['a']:
          key['g'] = c
    if 3 in key.keys() and 'a' in key.keys() and 'c' in key.keys() and 'f' in key.keys() and 'g' in key.keys():
      for c in key[3]:
        if c is not key['a'] and c is not key['c'] and c is not key['f'] and c is not key['g']:
          key['d'] = c