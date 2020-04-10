import bs4 as bs
from robobrowser import RoboBrowser
from w3lib.html import remove_tags


def get_html(): # Method to login on the page

    br = RoboBrowser()
    br.open("")
    form = br.get_form()
    form['username'] = ""
    form['password'] = ""
    br.submit_form(form)
    src = str(br.parsed())         # saves the parsed site to src which is wirtten to
    file = open("text.html", "w")  # the file text.html
    file.write(src)
    file.close()


def get_elements(counter=2):
    sauce = open("text.html", "r")              # opens the file and reads it to sauce. Fadded ( hardstyle remix) is nice xD
    soup = bs.BeautifulSoup(sauce, 'lxml')      # parses the site to beautifulsoup so that we can work with it
    url = []
    desc = []
    section = "section-" + str(counter)
      # is the number of the section as seen below
    for sections in soup.find_all('li', attrs={'id': section}):                 # goes through the section-{number}
        for link in sections.find_all('div', attrs={'class': 'content'}):       # finds the class content where everything we need is stored
            for links in link.find_all('a'):                                    # find all links by going through <a> and checks if href is in it and saves it to url
                if 'href' in links.attrs:
                    url = [links.attrs['href']] + url
            #url = list(dict.fromkeys(url))                                      # checks for duplicates cause we will have some
            for text in link.find_all('div', attrs={'class': 'no-overflow'}):   # find all <p> in which the text is stored
                desc = desc + [strip_html(text.find_all('p'))]                  # saves it to desc
            #desc = list(dict.fromkeys(desc))
            # checks for duplicates
    desc = list(dict.fromkeys(desc))
    url = list(dict.fromkeys(url))
    return url, desc                                                          # returns it to the mehtod main

def strip_html(input):
    return remove_tags(str(input))


def get_information_main(i):
    data = list(get_elements(i))
    links = data[0]
    text = data[1:-1]
    link = []
    links.reverse()
    indexer = 2
    section = "section-" + str(counter)
    textOut = ""
    for i_l in links:
        if i_l == "https://moodle.bk-technik-moers.de/course/view.php?id=688#" + section:
            indexer += 1
            section = "section-" + str(indexer)
        else:
            link = link + [i_l]
    link = list(dict.fromkeys(link))
    for i_t in range(len(text)):
        textOut = str(text[i_t])
    return textOut, linkin

if __name__ == '__main__':
    get_information_main(6)  # the number of the section that gets printed
