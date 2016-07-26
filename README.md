# script
`grep '<pttern>' <file_name> | grep -v '^10\.' | cut -d' ' -f1- 4 | sort | uniq -c | sort -nr `

grep ‘<pattern>’ <file_name> -: It finds pattern ‘<pattern>’ in the file <file_name> and put all that lines having that pattern in the pipe.

grep -v ‘^10\.’ -: It finds the lines given as input from previous function starting with expression ‘10’ and because of -v it reverses the result and put all lines not having this expression at the start into the next pipe.


cut -d’ ‘ -f1-4 -: In every line it cuts the characters after 4th space (‘  ‘).

sort-: simply sort the lines

uniq-c -: report or filter out repeated lines in a file
     -c means Precede each output line with the count of the number of times
             the line occurred in the input, followed by a single space.

sort -nr -:sorts the lines
-nr  means according to numeric value of string in reverse order
