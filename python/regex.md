strings and regex

regex tutorial
    https://docs.python.org/3/howto/regex.html#regex-howto

pulling out patterns - basics

    estimate = report[0][0]  #'Estimated Per-Host Requirements: Memory=1.12GB VCores=1'
    mem_text = re.match(".*Memory=(\S+)\s.*", estimate).groups()[0] #'1.12GB'
    mem = re.match("([0-9\.]+)([A-Z]+)", mem_text).groups() #('1.12', 'GB')


