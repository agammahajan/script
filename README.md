# script
`grep ' /api/catalog' practo.access.log | grep -v '^10\.' | cut -d' ' -f1- 4 | sort | uniq -c | sort -nr `
