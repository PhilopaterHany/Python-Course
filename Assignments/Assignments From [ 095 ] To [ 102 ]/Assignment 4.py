# regex => ((https?)://(www.)?(\w+):?(\d+)?/?(.com|.org)(\S+))

# String Test:
# http://www.elzero.org:8888/link.php   (Matched)
# https://elzero.org:8888/link.php      (Matched)
# http://www.elzero.com/link.py         (Matched)
# https://elzero.com/link.py            (Matched)
# http://www.elzero.net
# https://elzero.net
