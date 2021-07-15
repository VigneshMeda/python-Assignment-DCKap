ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen",	"fourteen",	"fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
number = int(input())
res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while number > 0:
    res[i] = number % 10
    i = i + 1
    number = number // 10
main = ""
if res[9]!=0:
    main += ones[res[9]]+" Billion "
if res[8]!=0:
    main += ones[res[8]]+" Hundred Millon "
if res[7]!=0:
    if(res[7]==1):
        main += teens[res[6]]+ " Thousand Million "
    else:
        main += tens[res[7]]+" "+ones[res[6]]+  " Thousand Million "
else:
    if res[6]!=0:
        main += ones[res[6]]+ " Million "

if res[5]!=0:
    main += ones[res[5]]+" Hundred "
if res[4]!=0:
    if(res[4]==1):
        main += teens[res[3]]+ " Thousand "
    else:
        main += tens[res[4]]+" "+ones[res[3]]+  " Thousand "
else:
    if res[3]!=0:
        main += ones[res[3]]+ " Thousand "
if res[2]!=0:
    main += ones[res[2]]+" Hundred "
if res[1] != 0:
    if (res[1] == 1):
        main += teens[res[0]]
    else:
        main += tens[res[1]] + " " + ones[res[0]]
else:
    if res[0] != 0:
        main += ones[res[0]]
            
print(main+ " dollars ")