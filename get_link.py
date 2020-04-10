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
    text = list(get_elements(i))
    links = ""
    test2 = []
    linkin = []
    for x in range(len(text)): # this sorts the lists returned by get_elements. [0] holds always the links, that makes it easier to format the text
        if x != 0:
            test2 = test2 + text[x]
            links = text[0] #+ "\n" + test2#+ "\n" + str(text[x])+"\n"

    links.reverse()
    counter = 2
    section = "section-" + str(counter)
    blabla = ""
    for link in links:
        if link == "https://moodle.bk-technik-moers.de/course/view.php?id=688#" + section:
            counter += 1
            section = "section-" + str(counter)
            #print(newLinks)
        else:
            #print(section + ":" + link)
            linkin = linkin + [link]
    linkin = list(dict.fromkeys(linkin))
    for i_t in range(len(test2)):
        blabla = str(test2[i_t])
    return blabla, linkin

if __name__ == '__main__':
    get_information_main(6)  # the number of the section that gets printed
