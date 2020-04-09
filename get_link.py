import bs4 as bs
from robobrowser import RoboBrowser
from w3lib.html import remove_tags


def get_html(): # Method to login on the page

    br = RoboBrowser()
    br.open("")     # you might change the url to your course page, the direkt link to the page
    form = br.get_form()
    form['username'] = ""
    form['password'] = ""
    br.submit_form(form)
    src = str(br.parsed())         # saves the parsed site to src which is wirtten to
    file = open("text.html", "w")  # the file text.html
    file.write(src)
    file.close()


def get_elements(number):
    sauce = open("text.html", "r")              # opens the file and reads it to sauce. Fadded ( hardstyle remix) is nice xD
    soup = bs.BeautifulSoup(sauce, 'lxml')      # parses the site to beautifulsoup so that we can work with it
    url = []
    desc = []
    if number == 2:            # is the number of the section as seen below
        for sections in soup.find_all('li', attrs={'id': 'section-2'}):             # goes through the section-{number}
            for link in sections.find_all('div', attrs={'class': 'content'}):       # finds the class content where everything we need is stored
                for links in link.find_all('a'):                                    # find all links by going through <a> and checks if href is in it and saves it to url
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))                                      # checks for duplicates cause we will have some
                for text in link.find_all('div', attrs={'class': 'no-overflow'}):   # find all <p> in which the text is stored
                    desc = desc + [strip_html(text.find_all('p'))]                  # saves it to desc
                desc = list(dict.fromkeys(desc))                                    # checks for duplicates
        return [url], desc                                                            # returns it to the mehtod main
    # the code for every section is the same so no comments

    if number == 3:
        for sections in soup.find_all('li', attrs={'id': 'section-3'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 4:
        for sections in soup.find_all('li', attrs={'id': 'section-4'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 5:
        for sections in soup.find_all('li', attrs={'id': 'section-5'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 6:
        for sections in soup.find_all('li', attrs={'id': 'section-6'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 7:
        for sections in soup.find_all('li', attrs={'id': 'section-7'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 8:
        for sections in soup.find_all('li', attrs={'id': 'section-8'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return url + desc

    if number == 9:
        for sections in soup.find_all('li', attrs={'id': 'section-9'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 10:
        for sections in soup.find_all('li', attrs={'id': 'section-10'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 11:
        for sections in soup.find_all('li', attrs={'id': 'section-11'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 12:
        for sections in soup.find_all('li', attrs={'id': 'section-12'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc

    if number == 13:
        for sections in soup.find_all('li', attrs={'id': 'section-13'}):
            for link in sections.find_all('div', attrs={'class': 'content'}):
                for links in link.find_all('a'):
                    if 'href' in links.attrs:
                        url = [links.attrs['href']] + url
                url = list(dict.fromkeys(url))

                for text in link.find_all('div', attrs={'class': 'no-overflow'}):
                    desc = desc + [strip_html(text.find_all('p'))]
                desc = list(dict.fromkeys(desc))
        return [url] + desc


def strip_html(input):
    return remove_tags(str(input))


def get_information_main(i):
    text = get_elements(i)
    test = ""
    for x in range(len(text)): # this sorts the lists returned by get_elements. [0] holds always the links, that makes it easier to format the text
        if x != 0:
            test = str(text[0]) + "\n" + str(text[x])+"\n"

    return test # if the script is started standalone comment this line out and uncomment the line below
    #print(test)

if __name__ == '__main__':
    get_information_main(2) # the number of the section that gets printed
